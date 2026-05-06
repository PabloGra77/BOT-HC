# ANÁLISIS EXHAUSTIVO DEL PROYECTO BOT360 V9.2

**Generado**: Mayo 6, 2026  
**Versión del Proyecto**: BOT360 V9.2  
**Estado**: ✅ Exploración Completa

---

## TABLA DE CONTENIDOS

1. [Estructura del Proyecto](#1-estructura-del-proyecto)
2. [Lista Completa de Archivos](#2-lista-completa-de-archivos-python-y-su-propósito)
3. [Archivos de Configuración](#3-archivos-de-configuración-y-datos)
4. [Carpetas Duplicadas o Innecesarias](#4-carpetas-duplicadas-o-innecesarias)
5. [Requisitos](#5-dependencias-principalesrequirementst)
6. [Punto de Entrada Principal](#6-punto-de-entrada-principal)
7. [APIs y Conexiones Web](#7-referencias-a-conexiones-webapis)
8. [Módulos y Dependencias](#8-módulos-principales-y-dependencias)
9. [Problemas Identificados](#9-problemas-y-recomendaciones)

---

## 1. ESTRUCTURA DEL PROYECTO

```
BOT360 V9.2/                                    [Carpeta contenedor]
└── BOT360 V9.2/                                [Carpeta contenedor nivel 2]
    ├── .venv/                                  [⚠️ INNECESARIA - Entorno virtual ~500MB]
    │   └── Lib/site-packages/                  [Dependencias instaladas]
    │
    ├── BOT360/                                 [🎯 CARPETA PRINCIPAL]
    │
    ├── agenda_app/                             [📦 MÓDULO 1 - API y gestión de agendas]
    │   ├── api/                                [Rutas API REST]
    │   │   ├── __init__.py
    │   │   ├── agenda_routes.py                [Endpoints principales]
    │   │   └── security.py                     [Autenticación API key + Rate limit]
    │   │
    │   ├── application/                        [Lógica de negocio]
    │   │   ├── __init__.py
    │   │   ├── job_service.py                  [Orquestación de jobs asíncronos]
    │   │   └── hc_excel.py                     [Parsing de HC desde uploads]
    │   │
    │   ├── bot/                                [Lógica del bot]
    │   │   ├── runner.py                       [PUNTO DE ENTRADA DEL BOT]
    │   │   └── excel_lookup.py                 [Búsqueda de profesionales]
    │   │
    │   ├── domain/                             [Modelos de datos]
    │   │   ├── __init__.py
    │   │   └── requests.py                     [AgendaRequest, HCRequest dataclasses]
    │   │
    │   ├── routes/                             [Rutas de UI]
    │   │   └── ui.py                           [Página HTML + servicios web]
    │   │
    │   ├── __init__.py                         [create_app() - Factory pattern]
    │   ├── config.py                           [Configuración Flask]
    │   └── __pycache__/                        [⚠️ Archivos compilados - pueden eliminarse]
    │
    ├── bot360_app/                             [📦 MÓDULO 2 - Automatización y web]
    │   ├── automation/                         [Bot de automatización Selenium]
    │   │   ├── __init__.py
    │   │   ├── loader.py                       [Cargador que exporta Bot]
    │   │   └── inpec_bot.py                    [⭐ CORE BOT - Lógica Selenium]
    │   │
    │   ├── common/                             [Configuración compartida]
    │   │   ├── __init__.py
    │   │   ├── settings.py                     [Definición de rutas (BASE_DIR, CONFIG_DIR, etc.)]
    │   │   └── job_config.py                   [Config runtime de jobs]
    │   │
    │   ├── admin/                              [Administración]
    │   │   ├── __init__.py
    │   │   └── gui.py                          [GUI de admin (si existe)]
    │   │
    │   ├── web/                                [Servidor web]
    │   │   ├── __init__.py
    │   │   ├── server.py                       [🎯 PUNTO DE ENTRADA PRINCIPAL]
    │   │   └── wsgi.py                         [Configuración WSGI para producción]
    │   │
    │   ├── __init__.py
    │   └── __pycache__/                        [⚠️ Archivos compilados]
    │
    ├── build/                                  [⚠️ COMPILACIÓN PORTÁTIL - ~200MB]
    │   └── BotInpec360_Portable/
    │       └── localpycs/
    │
    ├── config/                                 [Configuración del proyecto]
    │   ├── config.json                         [🔐 CRÍTICO - Credenciales y config]
    │   ├── requirements.txt                    [Dependencias pinned con versiones]
    │   └── requirements_compatible.txt         [Dependencias compatibles]
    │
    ├── docs/                                   [Documentación]
    │   ├── ARQUITECTURA_AGENDA.md              [Especificación completa]
    │   └── debug/                              [⚠️ ARCHIVOS DUPLICADOS]
    │       ├── agenda_api_snip.txt
    │       ├── debug_visor.txt                 [DUPLICADO - ver logs/runtime/]
    │       ├── resumen_ejecucion.txt           [DUPLICADO - ver logs/runtime/]
    │       └── structure_scan.txt              [DUPLICADO - ver logs/runtime/]
    │
    ├── downloads/                              [Archivos generados runtime]
    │   ├── browser/                            [Descargas temporales del navegador]
    │   └── runtime/
    │       ├── hc/                             [Historias clínicas descargadas]
    │       └── job_configs/                    [Configuraciones temporales por job]
    │
    ├── logs/                                   [Logs de ejecución]
    │   ├── agenda_app.log                      [Log principal de la aplicación]
    │   └── runtime/                            [⚠️ ARCHIVOS DUPLICADOS]
    │       ├── debug_visor.txt                 [DUPLICADO - consolidar en docs/debug/]
    │       ├── resumen_ejecucion.txt           [DUPLICADO - consolidar en docs/debug/]
    │       └── structure_scan.txt              [DUPLICADO - consolidar en docs/debug/]
    │
    ├── scripts/                                [Scripts de utilidad]
    │   └── debug_excel.py                      [Depuración de Excel]
    │
    ├── tests/                                  [Pruebas unitarias]
    │   ├── test_agenda_api.py                  [Pruebas de API]
    │   └── test_agenda_service.py              [Pruebas de servicios]
    │
    ├── usuario/                                [Datos de usuarios]
    │   └── PLANTILLA_ACTUALIZADA.csv           [Base de datos de profesionales]
    │
    ├── iniciar_bot.bat                         [🎯 PUNTO DE ENTRADA - Para usuarios]
    ├── INSTALAR_EN_PC_NUEVO.bat                [🎯 INSTALADOR ASISTENTE]
    └── [Carpeta principal del repositorio]
```

---

## 2. LISTA COMPLETA DE ARCHIVOS PYTHON Y SU PROPÓSITO

### ESTRUCTURA MODULAR (28 archivos de código)

#### AGENDA_APP (11 archivos) - Gestión de agendas
| Archivo | Líneas | Propósito | Estado |
|---------|--------|----------|--------|
| `agenda_app/__init__.py` | 40 | Inicializador, factory pattern `create_app()` | ✅ Core |
| `agenda_app/config.py` | 25 | Configuración Flask, rutas, keys | ✅ Core |
| `agenda_app/api/__init__.py` | 5 | Inicializador blueprint API | ✅ Core |
| `agenda_app/api/agenda_routes.py` | 80+ | **Rutas API**: POST/GET/DELETE agendas | ✅ Core |
| `agenda_app/api/security.py` | 50+ | Autenticación X-API-Key, rate limiting | ✅ Core |
| `agenda_app/application/__init__.py` | 5 | Inicializador | ✅ Core |
| `agenda_app/application/job_service.py` | 200+ | **Orquestación jobs asíncronos** | ✅ Core |
| `agenda_app/application/hc_excel.py` | 100+ | Extracción datos HC de requests | ✅ Core |
| `agenda_app/bot/runner.py` | 300+ | **Ejecutor del bot** - Genera agendas y HC | ✅ Core |
| `agenda_app/bot/excel_lookup.py` | 50+ | Búsqueda de profesionales en Excel | ✅ Core |
| `agenda_app/domain/requests.py` | 100+ | Dataclasses: AgendaRequest, HCRequest | ✅ Core |

#### BOT360_APP (13 archivos) - Automatización y web
| Archivo | Líneas | Propósito | Estado |
|---------|--------|----------|--------|
| `bot360_app/__init__.py` | 5 | Inicializador | ✅ Core |
| `bot360_app/common/__init__.py` | 5 | Inicializador | ✅ Core |
| `bot360_app/common/settings.py` | 60+ | **Definición de rutas dinamicas** BASE_DIR, CONFIG_DIR, LOGS_DIR, etc. | ✅ Core |
| `bot360_app/common/job_config.py` | 50+ | Configuración runtime de jobs | ✅ Core |
| `bot360_app/admin/__init__.py` | 5 | Inicializador | ✅ Opcional |
| `bot360_app/admin/gui.py` | ? | GUI de administración | ❓ Desconocido |
| `bot360_app/automation/__init__.py` | 5 | Inicializador | ✅ Core |
| `bot360_app/automation/loader.py` | 2 | Cargador que exporta `Bot` | ✅ Core |
| `bot360_app/automation/inpec_bot.py` | 800+ | **⭐ CORE DEL BOT** - Lógica Selenium | ✅ Core |
| `bot360_app/web/__init__.py` | 5 | Inicializador | ✅ Core |
| `bot360_app/web/server.py` | 30+ | Servidor Flask + `main()` | ✅ Core |
| `bot360_app/web/wsgi.py` | 10+ | Configuración WSGI | ✅ Core |

#### TESTS (2 archivos)
| Archivo | Propósito |
|---------|----------|
| `tests/test_agenda_api.py` | Pruebas unitarias de endpoints API |
| `tests/test_agenda_service.py` | Pruebas del servicio de agendas |

#### SCRIPTS (1 archivo)
| Archivo | Propósito |
|---------|----------|
| `scripts/debug_excel.py` | Depuración de lectura de Excel |

---

## 3. ARCHIVOS DE CONFIGURACIÓN Y DATOS

### Configuración (3 archivos en `config/`)

#### 3.1 config.json
**Ubicación**: `config/config.json`  
**Criticidad**: 🔴 CRÍTICA (Credenciales sensibles)  
**Contenido**:
```json
{
  "maintenance_mode": false,
  "admin_ids": [],
  "security": {
    "api_key": "CHANGE_ME_API_KEY",          // ⚠️ Debe ser único
    "secret_key": "CHANGE_ME_SECRET_KEY",    // ⚠️ Debe ser único
    "reset_token": "CHANGE_ME_RESET_TOKEN"   // ⚠️ Debe ser único
  },
  "credenciales": {                          // Usuario principal INPEC
    "usuario": "PGRANADOS",
    "contrasena": "Pablo56+",                // ⚠️ CREDENCIAL EXPUESTA
    "numero_verificacion": "Inpec",
    "url": "https://sisipec.salud360.app/Inpec360/servlet/ingreso"
  },
  "credenciales_hc": [                       // Múltiples usuarios para HC
    { "usuario": "ESTADISTICA", "contrasena": "Pablo56+", ... },
    { "usuario": "ESTADISTICA1", "contrasena": "Pablo56+", ... },
    { "usuario": "ESTADISTICA5", "contrasena": "Pablo56+", ... }
  ],
  "profesional": {
    "primer_apellido": "RUIZ",
    "primer_nombre": "CARMEN",
    "documento": "12345678",
    "sede": "RM MANIZALES",
    "servicios": ["Psicología", "Trabajo Social"]
  },
  "configuracion_agenda": {
    "dias_atencion": ["Martes"],
    "horarios": [
      { "inicio": "17:00", "fin": "22:50", "duracion": 14 }
    ],
    "servicios": ["PSIQUIATRÍA", "TM PSIQUIATRIA"]
  },
  "generacion_agenda": {
    "fecha_inicio": "24/02/2026",
    "fecha_fin": "24/02/2026"
  },
  "sedes": [                                  // 31+ sedes penitenciarias
    "COMPLEJO CARCELARIO Y PENITENCIARIO BOGOTA",
    "CPAMS EL BARNE",
    "EPMSC NEIVA",
    ...
  ]
}
```

#### 3.2 requirements.txt
```
flask==3.0.0
selenium==4.15.2
webdriver-manager==4.0.1
pandas==2.1.4
openpyxl==3.1.2
requests==2.31.0
pymupdf==1.23.8
urllib3==2.1.0
```

#### 3.3 requirements_compatible.txt
```
flask
selenium
webdriver-manager
pandas
openpyxl
requests
pymupdf
urllib3
```

**Nota**: requirements_compatible.txt es versión simplificada (sin versiones pinned).

### Datos de Usuario
- **usuario/PLANTILLA_ACTUALIZADA.csv** - Base de datos de profesionales para búsqueda

### Archivos Batch (Puntos de Entrada)

#### iniciar_bot.bat
```batch
@echo off
cd /d "%~dp0"
echo Iniciando BOT...
echo Acceda a http://127.0.0.1:5000 en su navegador.
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: No se encontró el entorno virtual.
    pause
    exit /b 1
)
REM Ejecutar desde la carpeta BOT360 para que los imports funcionen
pushd "%~dp0"
".venv\Scripts\python.exe" -m bot360_app.web.server
popd
pause
```

**Flujo**:
1. Activa .venv
2. Ejecuta `bot360_app.web.server` (módulo main)
3. Lanza servidor Flask en `http://127.0.0.1:5000`

#### INSTALAR_EN_PC_NUEVO.bat
- Instalador asistente
- Detecta Python
- Crea virtualenv
- Instala dependencias

---

## 4. CARPETAS DUPLICADAS O INNECESARIAS

### ⚠️ CRÍTICAS - ELIMINAR INMEDIATAMENTE

#### 1. .venv/ (~500-800 MB)
- **Ubicación**: `BOT360 V9.2/ (nivel 2) /.venv/`
- **Contenido**: Entorno virtual completo de Python
- **Razón**: Archivos compilados, pueden regenerarse
- **Acción**: 
  ```powershell
  # Eliminar
  Remove-Item ".venv" -Recurse -Force
  
  # Regenerar
  python -m venv .venv
  .venv\Scripts\pip.exe install -r config\requirements.txt
  ```

#### 2. build/BotInpec360_Portable/ (~200-400 MB)
- **Ubicación**: `BOT360/build/BotInpec360_Portable/`
- **Contenido**: Compilación portátil anterior (PyInstaller)
- **Razón**: Archivo compilado antiguo, no actualizado
- **Acción**: **ELIMINAR si no está en uso activo**
  ```powershell
  Remove-Item "build\BotInpec360_Portable" -Recurse -Force
  ```

#### 3. __pycache__/ (50-100 MB distribuido)
- **Ubicaciones**: `agenda_app/__pycache__`, `bot360_app/__pycache__`, etc.
- **Contenido**: Archivos `.pyc` compilados de Python
- **Razón**: Auto-regenerados, no necesarios en versionado
- **Acción**: Agregar a `.gitignore` (si usa git)
  ```
  **/__pycache__/
  *.pyc
  ```
  Limpiar manualmente:
  ```powershell
  Get-ChildItem -Recurse -Filter __pycache__ | Remove-Item -Recurse
  ```

### ⚠️ ARCHIVOS DUPLICADOS - CONSOLIDAR

#### 4. Archivos de Debug Duplicados

**PROBLEMA**: Los mismos archivos existen en dos ubicaciones

| Archivo | Ubicación 1 | Ubicación 2 | Tamaño | Acción |
|---------|-------------|------------|--------|--------|
| debug_visor.txt | `logs/runtime/` | `docs/debug/` | ? | Mantener en docs/debug/, eliminar de logs/ |
| resumen_ejecucion.txt | `logs/runtime/` | `docs/debug/` | ? | Mantener en docs/debug/, eliminar de logs/ |
| structure_scan.txt | `logs/runtime/` | `docs/debug/` | ? | Mantener en docs/debug/, eliminar de logs/ |
| agenda_api_snip.txt | - | `docs/debug/` | ? | ✅ Único |

**Recomendación**:
```powershell
# Revisar contenido
gc logs/runtime/debug_visor.txt
gc docs/debug/debug_visor.txt

# Si son idénticos, eliminar
Remove-Item logs/runtime/debug_visor.txt
Remove-Item logs/runtime/resumen_ejecucion.txt
Remove-Item logs/runtime/structure_scan.txt
```

---

## 5. DEPENDENCIAS PRINCIPALES (requirements.txt)

### 8 Dependencias Directas

| Paquete | Versión | Propósito | Categoría |
|---------|---------|----------|----------|
| **flask** | 3.0.0 | Framework web REST API | Core |
| **selenium** | 4.15.2 | Automatización de navegador | Core |
| **webdriver-manager** | 4.0.1 | Gestión de drivers Selenium | Core |
| **pandas** | 2.1.4 | Procesamiento de Excel/CSV | Core |
| **openpyxl** | 3.1.2 | Lectura/escritura de archivos .xlsx | Core |
| **requests** | 2.31.0 | Cliente HTTP para API calls | Core |
| **pymupdf** | 1.23.8 | Procesamiento de PDFs (PyMuPDF) | Core |
| **urllib3** | 2.1.0 | Base de requests, conexiones HTTP | Core |

### Dependencias Instaladas Indirectas (17+ paquetes)

```
Cuando ejecuta: pip install -r config/requirements.txt

Se instalan automáticamente:
- blinker               # Señales en Flask
- charset_normalizer    # Normalización de charset
- cffi                  # Foreign Function Interface para C
- click                 # CLI framework (usado por Flask)
- colorama              # Colores en terminal (Windows)
- python-dateutil       # Manipulación de fechas
- python-dotenv         # Variables .env
- et-xmlfile            # Escritura de XML (openpyxl)
- fitz (PyMuPDF)        # Procesamiento PDF
- itsdangerous          # Serialización segura (Flask)
- PySocks               # Proxy SOCKS (requests)
- wsproto               # Protocolo WebSocket
- werkzeug              # Utilidades WSGI (Flask)
- certifi               # Certificados SSL
- attrs / attr          # Clases con decoradores
- outcome               # Gestión de resultados
- ...y más
```

### Versión Compatible vs Pinned

- **requirements.txt**: ✅ Versiones específicas (reproducibilidad)
- **requirements_compatible.txt**: ✅ Solo nombres (flexibilidad)

**Recomendación**: Mantener ambas
- Usar `requirements.txt` en CI/CD y producción
- Usar `requirements_compatible.txt` para desarrollo

---

## 6. PUNTO DE ENTRADA PRINCIPAL

### Opción 1: Script Batch (Para usuarios finales) ✅ RECOMENDADO
```batch
iniciar_bot.bat
```
**Flujo**:
1. Valida entorno virtual
2. Ejecuta: `.venv\Scripts\python.exe -m bot360_app.web.server`
3. Lanza Flask en `0.0.0.0:5000`
4. Usuario accede a `http://localhost:5000`

### Opción 2: Ejecución Directa (Desarrollo)
```powershell
python -m bot360_app.web.server
```

### Opción 3: Servidor WSGI (Producción)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 bot360_app.web.wsgi:app
# o
waitress-serve --port=5000 bot360_app.web.wsgi:app
```

### Flujo de Ejecución Detallado

```
┌─────────────────────────────────────────────────────────────────┐
│ usuario ejecuta: iniciar_bot.bat                                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
        .venv\Scripts\python.exe -m bot360_app.web.server
                             │
                             ▼
         bot360_app/web/server.py → main()
                             │
                             ▼
              app = Flask(__name__)  [inicialización básica]
                             │
                             ▼
         agenda_app/__init__.py → create_app()
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
        Config  API BP    UI BP      Logging
        Flask  Register  Register   Config
                 │           │           │
                 └───────────┼───────────┘
                             │
                             ▼
          app.run(host='0.0.0.0', port=5000, debug=False)
                             │
                             ▼
              🌐 Servidor escuchando en http://127.0.0.1:5000
                             │
                             ▼
         Usuario accede con navegador
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
    GET /          POST /api/agenda      GET /api/agenda/{id}
   [HTML UI]      [Crear job]         [Estado job]
        │              │                     │
        │              ▼                     ▼
        │    job_service.crear_job_agenda()  get_job_snapshot()
        │              │                     │
        │              ▼                     ▼
        │    ThreadPoolExecutor              Cache en memoria
        │              │
        │              ▼
        │    Bot.iniciar_navegador()
        │    Bot.login()
        │    Bot.configurar_agenda()
        │    Bot.generar_agenda()
        │              │
        │              ▼
        │    ✅ Agenda generada en INPEC
```

---

## 7. REFERENCIAS A CONEXIONES WEB/APIs

### APIs Internas (Endpoints)

#### POST /api/agenda
- **Autenticación**: X-API-Key header
- **Body**:
  ```json
  {
    "sede": "CPMS BOGOTA - MODELO",
    "cc": "12345678",
    "fecha": "25/02/2026",
    "hora_inicio": "17:00",
    "duracion_min": 14,
    "cantidad": 5
  }
  ```
- **Respuesta**: `202 { "job_id": "uuid" }`

#### GET /api/agenda/{job_id}
- **Autenticación**: X-API-Key header
- **Respuesta**: `200 { "status": "en_ejecución", "detail": "...", "created_at": "..." }`

#### POST /api/agenda/{job_id}/stop
- **Autenticación**: X-API-Key header
- **Respuesta**: `200 { "ok": true, "message": "Job detenido" }`

#### POST /api/agenda/{job_id}/continue
- **Autenticación**: X-API-Key header
- **Respuesta**: `200 { "ok": true, "job_id": "nuevo_uuid" }`

#### GET /api/ping
- **Autenticación**: X-API-Key header
- **Respuesta**: `200 { "ok": true }`

#### POST /api/reset
- **Autenticación**: X-API-Key + X-Reset-Token
- **Respuesta**: `200 { "reset": true }`

### API Externa

#### INPEC Salud 360
- **URL**: `https://sisipec.salud360.app/Inpec360/servlet/ingreso`
- **Tipo**: Web application (Selenium automation)
- **Operaciones**:
  1. **Login**: Usuario + contraseña + número verificación
  2. **Configurar Agenda**: Establecer horarios y servicios
  3. **Generar Agenda**: Crear citas según parámetros
  4. **Descargar HC**: Historias clínicas en PDF

### Rate Limiting

```python
# security.py
_MAX_FAILED_ATTEMPTS = 10
_WINDOW_SECONDS = 60
```

**Límite**: 10 intentos fallidos por IP en 60 segundos.

### Librerías HTTP

| Librería | Uso |
|----------|-----|
| **requests** | Llamadas HTTP REST |
| **urllib3** | Base para requests, conexiones HTTP |
| **selenium** | Automatización de navegador (Chrome/Edge/IE) |
| **webdriver-manager** | Descarga automática de drivers |

---

## 8. MÓDULOS PRINCIPALES Y DEPENDENCIAS

### Mapa de Dependencias

```
┌─────────────────────────────────────────────────────────────────┐
│                    PUNTO DE ENTRADA                             │
│              iniciar_bot.bat → server.py                        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │  agenda_app/__init__.py       │
            │  create_app()                 │
            └──────────────────────────────┘
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
        ┌────────────┐ ┌─────────┐ ┌──────────┐
        │  config.py │ │  api/   │ │ routes/  │
        │  Config    │ │         │ │   ui.py  │
        └────────────┘ │ api_bp  │ └──────────┘
                       │ register│
                       └────┬────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
    ┌─────────────┐ ┌──────────────┐ ┌──────────────┐
    │   agenda_   │ │   security.  │ │   routes.py  │
    │   routes.py │ │     py       │ │              │
    │             │ │ (auth +      │ │ @api_bp      │
    │ POST /      │ │  rate limit) │ │              │
    │ agenda      │ └──────────────┘ └──────────────┘
    └────┬────────┘
         │
         ▼
    ┌──────────────────────┐
    │ job_service.py       │
    │ crear_job_agenda()   │
    │ get_job_snapshot()   │
    └────┬─────────────────┘
         │
         ▼
    ┌──────────────────────┐
    │ ThreadPoolExecutor   │
    │ _ejecutar_job_agenda │
    └────┬─────────────────┘
         │
         ▼ (en thread separado)
    ┌──────────────────────┐
    │ runner.py            │
    │ ejecutar_bot_job()   │
    └────┬─────────────────┘
         │
    ┌────┴────────────────┐
    ▼                     ▼
┌──────────┐         ┌────────────┐
│bot/      │         │excel_      │
│__init__  │         │lookup.py   │
│          │         │buscar_     │
│runner.py │         │profesional │
│_cargar_  │         │_por_cc()   │
│credenciales      │
│_crear_  │         └────────────┘
│bot_con_ │
│sesion() │
└────┬────┘
     │
     ▼
┌──────────────────────────┐
│ bot360_app/              │
│ automation/              │
│ inpec_bot.py             │
│ Bot class ⭐             │
│                          │
│ iniciar_navegador()      │
│ login()                  │
│ configurar_agenda()      │
│ generar_agenda()         │
│ descargar_hc()           │
│ cerrar()                 │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Selenium WebDriver       │
│ Chrome/Edge/IE           │
│ webdriver-manager        │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ INPEC Salud 360          │
│ https://sisipec.         │
│ salud360.app/...         │
└──────────────────────────┘
```

### Módulo: agenda_app

```
agenda_app/
├── __init__.py
│   ├── from flask import Flask
│   ├── from .config import Config
│   ├── _configure_logging()
│   └── create_app()  ← FACTORY PATTERN
│
├── config.py
│   ├── class Config
│   ├── SECRET_KEY
│   ├── API_KEY
│   ├── LOG_PATH
│   ├── USERS_EXCEL_PATH
│   └── DEBUG
│
├── api/
│   ├── __init__.py
│   │   └── from .agenda_routes import api_bp
│   │
│   ├── agenda_routes.py  ← ENDPOINTS
│   │   ├── POST /agenda
│   │   ├── GET /agenda/{job_id}
│   │   ├── POST /agenda/{job_id}/stop
│   │   ├── POST /agenda/{job_id}/continue
│   │   ├── GET /ping
│   │   └── POST /reset
│   │
│   └── security.py
│       ├── require_api_key()  ← Decorador
│       ├── require_reset_token()  ← Decorador
│       ├── Rate limiting por IP
│       └── HMAC comparación segura
│
├── application/
│   ├── __init__.py
│   │
│   ├── job_service.py  ← ORQUESTACIÓN
│   │   ├── crear_job_agenda()
│   │   ├── crear_job_hc()
│   │   ├── get_job_snapshot()
│   │   ├── detener_job()
│   │   ├── continuar_job_hc()
│   │   ├── clear_all_jobs()
│   │   └── ThreadPoolExecutor
│   │
│   └── hc_excel.py
│       └── extract_hc_request_data()
│
├── bot/
│   ├── runner.py  ← EJECUTOR DEL BOT
│   │   ├── _crear_bot_con_sesion()
│   │   ├── _recuperar_o_reiniciar_bot()
│   │   ├── ejecutar_bot_job()
│   │   ├── ejecutar_bot_job_hc()
│   │   └── MAX_RECOVERY_ATTEMPTS
│   │
│   └── excel_lookup.py
│       ├── buscar_profesional_por_cc()
│       ├── CargarProfesionales()
│       └── Búsqueda en usuario/PLANTILLA_ACTUALIZADA.csv
│
├── domain/
│   ├── __init__.py
│   │
│   └── requests.py
│       ├── class AgendaRequest
│       │   ├── sede: str
│       │   ├── cc: str
│       │   ├── fecha: str (DD/MM/YYYY o "hoy")
│       │   ├── hora_inicio: str (HH:MM)
│       │   ├── duracion_min: int
│       │   ├── cantidad: int
│       │   └── from_dict() → validación
│       │
│       └── class HCRequest
│           ├── cedula: str
│           ├── fecha_inicio: str
│           ├── fecha_fin: str
│           ├── servicio: str
│           ├── estrategia: str
│           ├── ruta_descarga: str
│           ├── pacientes_excel: list
│           └── from_dict() → validación
│
└── routes/
    └── ui.py
        ├── GET / → HTML form
        └── Servicios web frontend
```

### Módulo: bot360_app

```
bot360_app/
├── __init__.py
│
├── common/
│   ├── __init__.py
│   │
│   ├── settings.py  ← RUTAS DINÁMICAS
│   │   ├── BASE_DIR = Path(__file__).resolve().parents[2]
│   │   ├── CONFIG_DIR
│   │   ├── LOGS_DIR
│   │   ├── RUNTIME_LOG_DIR
│   │   ├── DOWNLOADS_DIR
│   │   ├── HC_OUTPUT_DIR
│   │   ├── CHROME_DOWNLOAD_DIR
│   │   ├── CONFIG_PATH
│   │   ├── JOB_CONFIG_DIR
│   │   └── funciones: load_main_config(), save_main_config(),
│   │             get_api_key(), get_secret_key(), etc.
│   │
│   └── job_config.py
│       ├── build_agenda_runtime_config()
│       ├── cleanup_runtime_config()
│       └── Gestión de config temporal por job
│
├── admin/
│   ├── __init__.py
│   └── gui.py  ← Posible interfaz gráfica
│
├── automation/
│   ├── __init__.py
│   │   └── from .inpec_bot import Bot
│   │
│   ├── loader.py
│   │   └── __all__ = ["Bot"]  ← Solo exporta Bot
│   │
│   └── inpec_bot.py  ⭐ CORE BOT (800+ líneas)
│       ├── SELECTORES = { ... }  ← XPath y By selectors
│       │
│       ├── normalize_text()  ← Normalización de strings
│       │
│       ├── class Bot
│       │   ├── __init__(config_path, browser_name, credential_override)
│       │   │
│       │   ├── iniciar_navegador(download_dir)
│       │   │   └── Chrome/Edge/IE via webdriver-manager
│       │   │
│       │   ├── login()
│       │   │   ├── Ingresa usuario + contraseña
│       │   │   ├── Realiza verificación
│       │   │   └── Valida sesión
│       │   │
│       │   ├── configurar_agenda()
│       │   │   ├── Selecciona sede
│       │   │   ├── Busca profesional
│       │   │   ├── Configura horarios y servicios
│       │   │   └── Guarda configuración
│       │   │
│       │   ├── generar_agenda()
│       │   │   ├── Establece fechas
│       │   │   ├── Genera agendas
│       │   │   └── Valida resultado
│       │   │
│       │   ├── descargar_hc()
│       │   │   ├── Selecciona pacientes
│       │   │   ├── Descarga PDFs
│       │   │   └── Guarda en descargas/hc/
│       │   │
│       │   ├── recuperar_pagina_y_sesion()
│       │   │   └── Recuperación suave en caso de timeout
│       │   │
│       │   └── cerrar()
│       │       └── Cierra navegador y limpia
│       │
│       └── Error handling y reintentos
│
└── web/
    ├── __init__.py
    │
    ├── server.py  ← PUNTO DE ENTRADA
    │   ├── from agenda_app import create_app
    │   │
    │   ├── _startup_error = None
    │   │
    │   ├── def main()
    │   │   ├── Crea app con create_app()
    │   │   ├── Maneja errores de startup
    │   │   ├── Imprime mensajes
    │   │   └── app.run(host='0.0.0.0', port=5000, debug=False)
    │   │
    │   └── if __name__ == "__main__": main()
    │
    └── wsgi.py
        ├── from agenda_app import create_app
        └── app = create_app()  ← Para producción
```

### Dependencias de Importación Cruzadas

```
inpec_bot.py IMPORTA DE:
├── json, time, sys, datetime, os, shutil, glob
├── requests
├── fitz (PyMuPDF)
├── selenium (webdriver, By, Keys, WebDriverWait, etc.)
├── webdriver_manager (ChromeDriverManager, EdgeChromiumDriverManager)
├── bot360_app.common.settings (rutas)
└── unicodedata

runner.py IMPORTA DE:
├── logging, os, threading, time
├── concurrent.futures.ThreadPoolExecutor
├── datetime
├── glob, json
├── pandas
├── agenda_app.config (Config)
├── agenda_app.domain.requests (AgendaRequest, HCRequest)
├── agenda_app.bot.excel_lookup (buscar_profesional_por_cc)
├── bot360_app.automation.loader (Bot)
├── bot360_app.common.job_config
├── bot360_app.common.settings
└── opciones de threading y recuperación de errores

job_service.py IMPORTA DE:
├── logging, os, threading, time
├── concurrent.futures
├── datetime
├── glob, json
├── pandas
├── agenda_app.config
├── agenda_app.domain.requests
├── agenda_app.application.hc_excel
├── agenda_app.application.job_service
├── bot360_app.automation.loader (Bot)
├── bot360_app.common.settings
└── subprocess para reset

agenda_routes.py IMPORTA DE:
├── logging
├── flask (Blueprint, jsonify, request)
├── agenda_app.application.hc_excel
├── agenda_app.application.job_service (todas las funciones)
├── agenda_app.domain.requests
├── agenda_app.api.security
└── Flask blueprints

security.py IMPORTA DE:
├── hmac
├── threading
├── time
├── functools.wraps
└── flask (current_app, jsonify, request)
```

---

## 9. PROBLEMAS Y RECOMENDACIONES

### 🔴 CRÍTICOS

#### 1. Credenciales Expuestas en config.json

**Problema**:
```json
{
  "credenciales": {
    "usuario": "PGRANADOS",
    "contrasena": "Pablo56+",  // ⚠️ VISIBLE EN CÓDIGO
  }
}
```

**Riesgos**:
- Credenciales visibles en repositorio
- Acceso no autorizado a INPEC
- Auditoría de seguridad fallará

**Soluciones**:
1. **Variables de entorno** (recomendado)
   ```python
   import os
   usuario = os.getenv("INPEC_USERNAME", "")
   password = os.getenv("INPEC_PASSWORD", "")
   ```

2. **Archivo .env** (desarrollo local)
   ```
   INPEC_USERNAME=PGRANADOS
   INPEC_PASSWORD=***
   AGENDA_API_KEY=***
   ```

3. **Gestor de secretos** (producción)
   - AWS Secrets Manager
   - Azure Key Vault
   - HashiCorp Vault

#### 2. API Keys Débiles

**config.json**:
```json
{
  "security": {
    "api_key": "CHANGE_ME_API_KEY",
    "secret_key": "CHANGE_ME_SECRET_KEY",
    "reset_token": "CHANGE_ME_RESET_TOKEN"
  }
}
```

**Problema**: Claves de ejemplo aún configuradas

**Solución**:
```python
# Validación en create_app()
if app.config.get("API_KEY") == "dev-api-key":
    raise RuntimeError("API_KEY insegura detectada")
```

#### 3. Rate Limiting Débil

**security.py**:
```python
_MAX_FAILED_ATTEMPTS = 10
_WINDOW_SECONDS = 60
```

**Problema**: Solo bloquea por IP, no por usuario

**Solución**:
```python
# Usar Redis para rate limiting distribuido
# o implementar bloqueo por (IP, usuario)
```

### 🟠 ALTOS

#### 4. Archivos Duplicados

**Problema**: Mismos archivos en `logs/runtime/` y `docs/debug/`

**Solución**:
```powershell
# Consolidar en docs/debug/
Remove-Item logs/runtime/debug_visor.txt
Remove-Item logs/runtime/resumen_ejecucion.txt
Remove-Item logs/runtime/structure_scan.txt
```

#### 5. Falta de Virtualenv en el Controlador de Fuentes

**.gitignore recomendado**:
```
.venv/
*.pyc
__pycache__/
build/
dist/
*.egg-info/
.pytest_cache/
logs/*.log
downloads/
*.csv.bak
```

#### 6. Recuperación de Errores Limitada

**inpec_bot.py**:
```python
MAX_RECOVERY_ATTEMPTS = 3
```

**Problema**: No reinicia bot si falla múltiples veces

**Solución**:
```python
# Implementar Circuit Breaker pattern
# o alertas a administrador después de X fallos
```

### 🟡 MEDIOS

#### 7. Logging No Configurable

**settings.py**:
```python
LOG_PATH = os.environ.get(
    "AGENDA_LOG_PATH",
    os.path.join(BASE_DIR, "logs", "agenda_app.log")
)
```

**Solución**: Agregar nivelación de log
```python
LOG_LEVEL = os.environ.get("AGENDA_LOG_LEVEL", "INFO")
logging.getLogger().setLevel(LOG_LEVEL)
```

#### 8. Falta de Tests

Solo 2 archivos de test:
- `tests/test_agenda_api.py`
- `tests/test_agenda_service.py`

**Recomendación**: Agregar pruebas para:
- Bot automation (mocks de Selenium)
- Excel lookup
- HC download
- Validación de requests

---

## 10. ESTADÍSTICAS DEL PROYECTO

| Métrica | Valor |
|---------|-------|
| **Archivos Python** | 28 (excl. .venv) |
| **Líneas de Código Est.** | 2,500+ |
| **Módulos Principales** | 2 (agenda_app, bot360_app) |
| **Dependencias Directas** | 8 |
| **Dependencias Indirectas** | 17+ |
| **Archivos de Configuración** | 3 (config.json, requirements.txt, requirements_compatible.txt) |
| **Carpetas de Datos** | 5 (config, downloads, logs, usuario, docs) |
| **Tamaño Estimado sin .venv** | 50-100 MB |
| **Tamaño Estimado con .venv** | 500-800 MB |
| **APIs Internas** | 6 endpoints |
| **APIs Externas** | 1 (INPEC) |

---

## CONCLUSIÓN

BOT360 V9.2 es una aplicación Flask + Selenium robusta para automatización de agendas y descarga de historias clínicas del sistema INPEC. 

**Puntos Fuertes**:
- ✅ Arquitectura modular bien estructurada
- ✅ API REST segura con autenticación
- ✅ Automatización con Selenium (multiple browsers)
- ✅ Documentación en ARQUITECTURA_AGENDA.md
- ✅ Rate limiting y seguridad

**Áreas de Mejora**:
- 🔴 Credenciales expuestas (usar variables de entorno)
- 🔴 .venv y build/ innecesarios en repositorio
- 🟠 Archivos duplicados de debug
- 🟠 Cobertura de tests limitada
- 🟡 Recuperación de errores mejorable

---

**Documento generado**: Mayo 6, 2026
**Versión**: 1.0
