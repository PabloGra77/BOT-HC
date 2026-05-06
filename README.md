# 🤖 BOT360 - Automatización INPEC

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Beta-orange)

Bot de automatización para el sistema INPEC Salud 360. Automatiza la creación de agendas y descarga de historias clínicas.

## 📋 Características

- ✅ **Automatización de Agendas**: Genera y gestiona agendas para profesionales
- ✅ **Descarga de Historias Clínicas**: Extrae documentos HC en PDF
- ✅ **API REST**: Integración con sistemas externos
- ✅ **Panel de Control Desktop**: Interfaz gráfica moderna
- ✅ **Versionado**: Control de versiones con Git
- ✅ **Ejecutable (.exe)**: Portable para Windows

## 🚀 Inicio Rápido

### Requisitos

- **Windows 7+** o **Windows 10/11**
- **Python 3.9+** (si instala desde código)
- **Git** (para clonar el repositorio)

### Opción 1: Descargar Ejecutable (Recomendado)

1. Descargar `BOT360-v1.0.0.exe` desde [Releases](https://github.com/tu-usuario/bot360/releases)
2. Ejecutar el instalador
3. Completar configuración inicial
4. ¡Listo!

### Opción 2: Instalar desde Código

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/bot360.git
cd bot360

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar credenciales
copy .env.example .env
# Editar .env con tus credenciales INPEC

# Ejecutar
python -m src.ui.desktop_app
```

## 📁 Estructura del Proyecto

```
BOT360/
├── src/
│   ├── agenda_app/           # Módulo de Agendas
│   │   ├── api/              # API REST endpoints
│   │   ├── application/      # Lógica de negocio
│   │   ├── domain/           # Modelos de datos
│   │   └── routes/           # Rutas web
│   ├── bot360_app/           # Automatización Selenium
│   │   ├── automation/       # Core del bot
│   │   ├── common/           # Configuración compartida
│   │   └── web/              # Servidor Flask
│   └── ui/                   # Interfaz Desktop
│       ├── desktop_app.py    # Aplicación principal
│       ├── components/       # Componentes UI
│       └── assets/           # Recursos (iconos, etc.)
├── config/
│   ├── config.json           # Configuración de sedes
│   └── requirements.txt       # Dependencias Python
├── tests/                    # Pruebas unitarias
├── docs/                     # Documentación
├── .github/
│   └── workflows/            # GitHub Actions CI/CD
├── .env.example              # Plantilla de variables de entorno
├── .gitignore                # Archivos a ignorar en Git
├── pyproject.toml            # Configuración del proyecto
├── setup.py                  # Script de instalación
├── CHANGELOG.md              # Historial de cambios
└── README.md                 # Este archivo
```

## ⚙️ Configuración

### 1. Credenciales INPEC

Editar `.env` con tus credenciales:

```env
INPEC_USER=tu_usuario_inpec
INPEC_PASSWORD=tu_contraseña
INPEC_VERIFICATION=Inpec
INPEC_URL=https://sisipec.salud360.app/Inpec360/servlet/ingreso
```

### 2. API Security

Generar claves seguras:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Actualizar `.env`:

```env
AGENDA_API_KEY=<clave_generada>
AGENDA_SECRET_KEY=<clave_generada>
AGENDA_RESET_TOKEN=<clave_generada>
```

### 3. Sedes y Profesionales

Editar `config/config.json` con los datos de tu institución.

## 🎯 Uso

### Interfaz Desktop

```bash
python -m src.ui.desktop_app
```

### API REST

```bash
python -m src.bot360_app.web.server
```

Luego acceder a: `http://localhost:5000`

### Línea de Comandos

```bash
# Crear job de agenda
curl -X POST http://localhost:5000/api/agenda \
  -H "Authorization: Bearer $AGENDA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{...}'

# Descargar historias clínicas
curl -X POST http://localhost:5000/api/hc \
  -H "Authorization: Bearer $AGENDA_API_KEY"
```

## 📚 API Documentation

Ver [API.md](docs/API.md) para documentación completa de endpoints.

## 🐛 Solución de Problemas

### Error: "No se pudo conectar a INPEC"

1. Verificar credenciales en `.env`
2. Revisar conexión a internet
3. Verificar que los selectores estén actualizados
4. Consultar logs en `logs/`

### Error: "Chrome Driver no encontrado"

1. Instalar Chrome/Chromium
2. O usar Edge: Editar config para usar Edge browser

### El bot se detiene

1. Revisar logs en `logs/runtime/`
2. Verificar que el sitio INPEC siga siendo accesible
3. Aumentar timeout en settings

## 🧪 Testing

```bash
# Instalar dependencias de desarrollo
pip install -e ".[dev]"

# Ejecutar pruebas
pytest

# Con cobertura
pytest --cov=src
```

## 📦 Compilar Ejecutable

```bash
# Instalar PyInstaller
pip install -e ".[build]"

# Compilar
pyinstaller bot360.spec

# El .exe estará en dist/
```

## 🔄 Versionado y Releases

Seguimos **Semantic Versioning**: MAJOR.MINOR.PATCH

### Crear Nueva Versión

1. Actualizar version en `pyproject.toml` y `setup.py`
2. Actualizar `CHANGELOG.md`
3. Commit y push
4. Crear tag: `git tag -a v1.0.0 -m "Release 1.0.0"`
5. Push tag: `git push origin v1.0.0`
6. Crear Release en GitHub con el .exe compilado

## 📝 Changelog

Ver [CHANGELOG.md](CHANGELOG.md) para historial completo de cambios.

## 🤝 Contribuciones

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para pautas de contribución.

## ⚠️ Seguridad

**IMPORTANTE**: Nunca compartir `.env` ni credenciales INPEC en repositories públicos.

- Usar variables de entorno para secretos
- Activar 2FA en cuentas INPEC
- Revisar logs regularmente
- Reportar vulnerabilidades a: security@bot360.local

## 📞 Soporte

- 📧 Email: support@bot360.local
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/bot360/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/tu-usuario/bot360/discussions)

## 📄 Licencia

Este proyecto está licenciado bajo MIT - Ver [LICENSE](LICENSE) para detalles.

## ✨ Agradecimientos

Desarrollado para automatizar procesos INPEC Salud 360.

---

**Última actualización**: 2024
**Versión**: 1.0.0
**Estado**: Beta

