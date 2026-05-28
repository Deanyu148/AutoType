# AutoType

Una hermosa herramienta de auto-escritura multiplataforma. Simula la entrada del teclado en cualquier aplicación, con modos de escritura realista carácter por carácter y pegado instantáneo desde el portapapeles.

## Características

- **Modos de Entrada Duales** — Escritura realista carácter por carácter (con variación aleatoria de retardo) o pegado instantáneo
- **Soporte de Teclas Especiales** — Enter, Tab, Esc, teclas de dirección, F1–F12 mediante tokens especiales
- **Gestión de Presets** — Guardar, cargar, importar/exportar presets (formato YAML), hasta 50
- **Atajos Globales** — F6 iniciar, F7 detener, F8 alternar (funciona desde cualquier ventana)
- **Bandeja del Sistema** — Minimizar a la bandeja con menú de acceso rápido
- **10 Idiomas en la UI** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **Siempre Visible** — Mantener la ventana siempre al frente
- **Cuenta Regresiva** — Retardo de inicio configurable de 0–10 segundos
- **Velocidad Ajustable** — 1–200 CPS (caracteres por segundo)
- **Números de Línea** — Editor con números de línea y conteo de caracteres/palabras/líneas

## Instalación

### Ejecutar desde Código Fuente

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### Dependencias

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Framework Qt para UI
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — Simulación de teclado + detector de atajos globales
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — Modo instantáneo
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — Importación/exportación de presets

### Compilar EXE (Windows)

```bash
build.bat
```

## Uso

### Operación Básica

1. Escriba o pegue el texto en el panel editor izquierdo
2. Ajuste la velocidad, retardo y modo en el panel derecho
3. Haga clic en "Iniciar" o presione F6 para comenzar
4. Coloque el cursor en el campo de destino durante la cuenta regresiva (3 seg por defecto)
5. Presione F7 para detener en cualquier momento

### Tokens de Teclas Especiales

Use la notación `{KEY}` para insertar teclas especiales:

| Token | Tecla |
|---|---|
| `{ENTER}` | Enter |
| `{TAB}` | Tab |
| `{ESC}` | Escape |
| `{SPACE}` | Espacio |
| `{BACKSPACE}` | Retroceso |
| `{DELETE}` | Suprimir |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | Flechas |
| `{HOME}` `{END}` | Inicio / Fin |
| `{PAGEUP}` `{PAGEDOWN}` | Re Pág / Av Pág |
| `{F1}` … `{F12}` | Teclas de función |

Ejemplo:
```
usuario{ENTER}contraseña{TAB}{ENTER}Hola Mundo, este es texto auto-escrito.{ENTER}
```

### Modos de Entrada

- **Realista** — Envía pulsaciones una por una via pynput con variación aleatoria de retardo. Imita la escritura humana.
- **Instantáneo** — Usa portapapeles + Ctrl+V para pegar todo de una vez. La opción más rápida.

### Atajos Globales

| Tecla | Acción |
|---|---|
| F6 | Iniciar escritura |
| F7 | Detener escritura |
| F8 | Alternar (iniciar/detener) |

## Estructura del Proyecto

```
AutoType/
├── main.py                     # Punto de entrada
├── build.bat                   # Script de compilación PyInstaller
├── AutoType.ico                # Icono de la aplicación
├── requirements.txt            # Dependencias
├── README.md                   # README en chino
├── docs/                       # READMEs en otros idiomas
└── src/
    ├── core/
    │   ├── autotyper.py        # Motor de escritura (hilo)
    │   └── key_simulator.py    # Simulación de teclado
    ├── ui/
    │   ├── main_window.py      # Ventana principal
    │   ├── editor_panel.py     # Panel editor de texto
    │   ├── settings_panel.py   # Panel de configuración
    │   ├── preset_manager.py   # Gestión de presets
    │   ├── widgets.py          # Widgets personalizados
    │   └── theme.py            # Definiciones de tema
    └── utils/
        ├── config.py           # Persistencia de configuración (JSON)
        └── i18n.py             # Internacionalización
```

## Stack Tecnológico

- **GUI**: PySide6 (Qt para Python)
- **Simulación de Teclado**: pynput / pyautogui
- **Almacenamiento de Config**: JSON / YAML
- **Compilación**: PyInstaller (EXE de archivo único)

## Licencia

MIT License

## Autor

Deanyu148
