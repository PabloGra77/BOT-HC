# 🔴 ERRORES Y PROBLEMAS ENCONTRADOS - BOT360 V9.2

## PRIORIDAD CRÍTICA 🔴

### 1. **CREDENCIALES EXPUESTAS EN config.json** ⚠️ SEGURIDAD
**Problema:**
- Credenciales en texto plano: "PGRANADOS", "Pablo56+"
- Múltiples credenciales HC con misma contraseña
- URLs de API expuestas
- Datos sensibles comprometidos

**Impacto:** Acceso no autorizado, fallo de seguridad

**Solución:**
- Mover credenciales a variables de entorno
- Crear archivo `config.example.json` sin credenciales
- Usar Python-dotenv para gestionar secretos

---

### 2. **CARPETA DUPLICADA: "BOT360 V9.2"** 📁
**Problema:**
```
BOT360 V9.2 (1)/BOT360 V9.2/BOT360 V9.2/BOT360/  ← TRIPLE NIVEL
```
**Impacto:** Confusión en estructura, rutas incorrectas

**Solución:**
- Eliminar carpeta duplicada `BOT360 V9.2`
- Reorganizar como: `BOT360/` al nivel superior

---

### 3. **.venv EN REPOSITORIO (~500MB)** 📦
**Problema:**
- Virtual environment en la rama
- Archivos .venv listados en carpetas

**Solución:**
- Eliminar .venv
- Recrear con `pip install -r requirements.txt`
- Agregar .venv al .gitignore

---

### 4. **CARPETA build ANTIGUA (~200MB)** 📦
**Problema:**
```
build/BotInpec360_Portable/
```
- Parece ser compilación antigua

**Solución:**
- Eliminar si no se usa
- Usar PyInstaller para .exe nuevo

---

## PRIORIDAD ALTA 🟠

### 5. **ARCHIVOS DE LOG DUPLICADOS** 📝
**Problema:**
```
logs/runtime/debug_visor.txt       ← Duplicado
docs/debug/debug_visor.txt         ← Original
logs/runtime/resumen_ejecucion.txt ← Duplicado
docs/debug/resumen_ejecucion.txt   ← Original
```

**Solución:**
- Consolidar en `logs/`
- Eliminar `docs/debug/`

---

### 6. **SELECTORES XPath NO VÁLIDOS EN inpec_bot.py** ❌
**Problema:**
```python
"login_usuario": (By.ID, "vUSUARIOSLOGIN"),          # Posible ID incorrecto
"menu_citas": (By.XPATH, "//span[contains(text(), 'Citas')]"),  # Puede no existir
"btn_buscar_prof": (By.NAME, "IMAGE1"),              # Genérico, poco confiable
```

**Impacto:** Selección de elementos falla, bot no funciona

**Solución:**
- Inspeccionar HTML actual del sitio
- Validar cada selector con F12
- Usar clases CSS más robustas

---

### 7. **INTERFAZ WEB (Flask) EN LUGAR DE DESKTOP** 🌐➜🖥️
**Problema:**
```python
# bot360_app/web/server.py
app.run(host="0.0.0.0", port=5000, debug=False)
```
- Interfaz web en puerto 5000
- Require browser para interactuar
- No es una aplicación de escritorio

**Solución:**
- Crear GUI con PyQt6 o Tkinter
- Reemplazar Flask por aplicación desktop
- Crear ventanas para panel de control

---

### 8. **SIN MANEJO DE ERRORES ROBUSTO** ❌
**Problema:**
```python
def _driver_operativo(self):
    if not self.driver:
        return False
    try:
        _ = self.driver.current_url
    except:  # ⚠️ BARE EXCEPT - muy genérico
        return False
```

**Solución:**
- Usar excepciones específicas
- Logging estructurado
- Mensajes de error claros

---

## PRIORIDAD MEDIA 🟡

### 9. **SIN ESTRUCTURA GITHUB-READY** 📚
**Problema:**
- Sin .gitignore
- Sin setup.py
- Sin pyproject.toml
- Sin CHANGELOG.md
- Sin CONTRIBUYENDO.md

**Solución:**
- Crear estructura estándar de Python
- Agregar archivos necesarios
- Documento README con instrucciones

---

### 10. **SIN VERSIONADO** 📌
**Problema:**
- Sin __version__ en código
- Sin changelog
- Sin tags de versión

**Solución:**
- Usar semver (1.0.0, 1.1.0, etc.)
- Crear CHANGELOG.md
- Git tags por versión

---

### 11. **SIN COMPILADOR .EXE** 🔨
**Problema:**
- No se puede generar ejecutable
- Solo archivos .bat

**Solución:**
- Configurar PyInstaller
- Crear script de build
- Generar .exe portable

---

### 12. **RATE LIMITING DÉBIL** ⚠️
**Problema:**
```python
# 10 intentos fallidos por IP en 60 segundos es muy débil
MAX_LOGIN_ATTEMPTS = 10
RATE_LIMIT_WINDOW = 60
```

**Solución:**
- Aumentar límite o usar Redis
- Implementar CAPTCHA
- Logging de intentos fallidos

---

## PROBLEMAS DE CÓDIGO 🐛

### 13. **TURBO MODE SIEMPRE ACTIVADO**
```python
self.turbo_mode = True  # Siempre ON, sin opción para desactivar
```
- Salta validaciones visuales
- Hace debugging más difícil

### 14. **IMPORTS INCOMPLETOS**
```python
from selenium.webdriver.ie.service import Service as IEService
# ⚠️ IE está deprecado en Selenium 4.x
```

### 15. **RUTAS HARDCODEADAS**
```python
CONFIG_PATH = CONFIG_DIR / "config.json"
CHROME_DOWNLOAD_DIR = DOWNLOADS_DIR / "browser"
```
- Debería ser configurable
- En Windows puede tener problemas con rutas

---

## RESUMEN DE ACCIONES 📋

| # | Acción | Prioridad | Tiempo Est. |
|---|--------|-----------|------------|
| 1 | Limpiar estructura (eliminar duplicados) | 🔴 | 15 min |
| 2 | Mover credenciales a .env | 🔴 | 20 min |
| 3 | Actualizar selectores XPath | 🟠 | 45 min |
| 4 | Crear GUI desktop | 🟠 | 2-3 hrs |
| 5 | Crear estructura GitHub | 🟠 | 30 min |
| 6 | Configurar PyInstaller | 🟡 | 20 min |
| 7 | Crear README y docs | 🟡 | 30 min |

---

**Total Estimado: 4-5 horas de trabajo**

