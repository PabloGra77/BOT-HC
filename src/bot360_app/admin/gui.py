import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import threading
import time
import os

from bot360_app.common.settings import (
    ALERTS_LOG_PATH,
    load_main_config,
    save_main_config,
)

class AdminPanelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Administración - BOT")
        self.root.geometry("800x700")
        
        self.maintenance_mode = tk.BooleanVar()
        self.last_log_size = 0
        
        self.setup_ui()
        self.load_config()
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor_alerts, daemon=True)
        self.monitor_thread.start()
        
        # Handle close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        # Frame Superior: Estado y Control Mantenimiento
        top_frame = ttk.LabelFrame(self.root, text="Control del Sistema", padding=10)
        top_frame.pack(fill="x", padx=10, pady=5)
        
        self.lbl_status = ttk.Label(top_frame, text="Estado: Cargando...", font=("Arial", 12, "bold"))
        self.lbl_status.pack(side="left", padx=5)
        
        self.btn_maintenance = ttk.Button(top_frame, text="Cambiar Modo", command=self.toggle_maintenance)
        self.btn_maintenance.pack(side="right", padx=5)

        # Frame Inferior: Alertas y Errores
        logs_frame = ttk.LabelFrame(self.root, text="Alertas y Errores Recientes", padding=10)
        logs_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.txt_logs = scrolledtext.ScrolledText(logs_frame, state='disabled', height=10)
        self.txt_logs.pack(fill="both", expand=True)
        self.txt_logs.tag_config("error", foreground="red")
        self.txt_logs.tag_config("info", foreground="blue")
        self.txt_logs.tag_config("success", foreground="green")
        
        ttk.Button(logs_frame, text="Limpiar Logs Vista", command=self.clear_logs_view).pack(pady=5)

    def load_config(self):
        try:
            self.config = load_main_config()
            self.maintenance_mode.set(self.config.get("maintenance_mode", False))
            self.update_status_label()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar config.json: {e}")

    def save_config(self):
        try:
            save_main_config(self.config)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar config.json: {e}")

    def update_status_label(self):
        if self.maintenance_mode.get():
            self.lbl_status.config(text="🔴 EN MANTENIMIENTO (Usuarios Bloqueados)", foreground="red")
            self.btn_maintenance.config(text="Desactivar Mantenimiento")
        else:
            self.lbl_status.config(text="🟢 OPERATIVO", foreground="green")
            self.btn_maintenance.config(text="Activar Mantenimiento")

    def toggle_maintenance(self):
        new_state = not self.maintenance_mode.get()
        self.maintenance_mode.set(new_state)
        self.config["maintenance_mode"] = new_state
        self.save_config()
        self.update_status_label()
        
        state_str = "ACTIVADO" if new_state else "DESACTIVADO"
        self.log_to_view(f"[SISTEMA] Modo Mantenimiento {state_str}", "info")

    def monitor_alerts(self):
        if not os.path.exists(ALERTS_LOG_PATH):
            open(ALERTS_LOG_PATH, 'w').close()
            
        while True:
            try:
                if os.path.exists(ALERTS_LOG_PATH):
                    current_size = os.path.getsize(ALERTS_LOG_PATH)
                    if current_size > self.last_log_size:
                        with open(ALERTS_LOG_PATH, 'r', encoding='utf-8') as f:
                            f.seek(self.last_log_size)
                            new_lines = f.readlines()
                            self.last_log_size = f.tell()
                            
                            for line in new_lines:
                                if line.strip():
                                    try:
                                        data = json.loads(line)
                                        self.process_alert(data)
                                    except:
                                        pass
            except Exception as e:
                print(f"Error monitor: {e}")
            
            time.sleep(2)

    def process_alert(self, data):
        timestamp = data.get("timestamp", "?")
        user = data.get("user", "Desconocido")
        uid = data.get("user_id", "")
        event_type = data.get("type", "ERROR") # Por defecto ERROR si no viene el campo (logs viejos)
        
        if event_type == "SUCCESS":
            msg_text = data.get("message", "Acción completada")
            details = data.get("details", "")
            display_text = (
                f"[{timestamp}] ✅ ACTIVIDAD - Usuario: {user} (ID: {uid})\n"
                f"Acción: {msg_text}\n"
                f"Detalles: {details}"
            )
            tag = "success"
        else:
            # Manejo de errores (soporte para formato viejo y nuevo)
            error = data.get("message") or data.get("error", "Error desconocido")
            display_text = (
                f"[{timestamp}] ❌ ERROR - Usuario: {user} (ID: {uid})\n"
                f"Fallo: {error}\n"
            )
            tag = "error"
        
        self.root.after(0, lambda: self.log_to_view(display_text, tag))

    def log_to_view(self, text, tag=None):
        self.txt_logs.config(state='normal')
        self.txt_logs.insert(tk.END, text + "\n" + "-"*50 + "\n", tag)
        self.txt_logs.see(tk.END)
        self.txt_logs.config(state='disabled')

    def clear_logs_view(self):
        self.txt_logs.config(state='normal')
        self.txt_logs.delete("1.0", tk.END)
        self.txt_logs.config(state='disabled')

    def on_closing(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = AdminPanelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
