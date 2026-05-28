# AutoType

Uma bela ferramenta de digitação automática multiplataforma. Simula a entrada do teclado em qualquer aplicativo, com modos de digitação realista caractere por caractere e colagem instantânea da área de transferência.

## Funcionalidades

- **Modos de Entrada Duplos** — Digitação realista caractere por caractere (com variação aleatória de atraso) ou colagem instantânea
- **Suporte a Teclas Especiais** — Enter, Tab, Esc, setas direcionais, F1–F12 via tokens especiais
- **Gerenciamento de Predefinições** — Salvar, carregar, importar/exportar predefinições (formato YAML), até 50
- **Atalhos Globais** — F6 iniciar, F7 parar, F8 alternar (funciona de qualquer janela)
- **Bandeja do Sistema** — Minimizar para a bandeja com menu de acesso rápido
- **10 Idiomas na Interface** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **Sempre no Topo** — Manter a janela acima das outras
- **Contagem Regressiva** — Atraso de início configurável de 0–10 segundos
- **Velocidade Ajustável** — 1–200 CPS (caracteres por segundo)
- **Números de Linha** — Editor com números de linha e contagem de caracteres/palavras/linhas

## Instalação

### Executar do Código Fonte

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### Dependências

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Framework Qt para UI
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — Simulação de teclado + detector de atalhos globais
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — Modo instantâneo
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — Importação/exportação de predefinições

### Compilar EXE (Windows)

```bash
build.bat
```

## Uso

### Operação Básica

1. Digite ou cole o texto no painel editor esquerdo
2. Ajuste a velocidade, atraso e modo no painel direito
3. Clique em "Iniciar" ou pressione F6
4. Posicione o cursor no campo de destino durante a contagem regressiva (3 seg por padrão)
5. Pressione F7 para parar a qualquer momento

### Tokens de Teclas Especiais

Use a notação `{KEY}` para inserir teclas especiais:

| Token | Tecla |
|---|---|
| `{ENTER}` | Enter |
| `{TAB}` | Tab |
| `{ESC}` | Esc |
| `{SPACE}` | Espaço |
| `{BACKSPACE}` | Backspace |
| `{DELETE}` | Delete |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | Setas direcionais |
| `{HOME}` `{END}` | Home / End |
| `{PAGEUP}` `{PAGEDOWN}` | Page Up / Down |
| `{F1}` … `{F12}` | Teclas de função |

Exemplo:
```
usuario{ENTER}senha{TAB}{ENTER}Olá Mundo, este é um texto auto-digitado.{ENTER}
```

### Modos de Entrada

- **Realista** — Envia pressionamentos de tecla um por um via pynput com variação aleatória de atraso. Imita a digitação humana.
- **Instantâneo** — Usa área de transferência + Ctrl+V para colar tudo de uma vez. Opção mais rápida.

### Atalhos Globais

| Tecla | Ação |
|---|---|
| F6 | Iniciar digitação |
| F7 | Parar digitação |
| F8 | Alternar (iniciar/parar) |

## Estrutura do Projeto

```
AutoType/
├── main.py                     # Ponto de entrada
├── build.bat                   # Script de build PyInstaller
├── AutoType.ico                # Ícone do aplicativo
├── requirements.txt            # Dependências
├── README.md                   # README em chinês
├── docs/                       # READMEs em outros idiomas
└── src/
    ├── core/
    │   ├── autotyper.py        # Motor de digitação (thread)
    │   └── key_simulator.py    # Simulação de teclado
    ├── ui/
    │   ├── main_window.py      # Janela principal
    │   ├── editor_panel.py     # Painel editor de texto
    │   ├── settings_panel.py   # Painel de configurações
    │   ├── preset_manager.py   # Gerenciamento de predefinições
    │   ├── widgets.py          # Widgets personalizados
    │   └── theme.py            # Definições de tema
    └── utils/
        ├── config.py           # Persistência de configuração (JSON)
        └── i18n.py             # Internacionalização
```

## Stack Tecnológico

- **GUI**: PySide6 (Qt para Python)
- **Simulação de Teclado**: pynput / pyautogui
- **Armazenamento de Config**: JSON / YAML
- **Build**: PyInstaller (EXE de arquivo único)

## Licença

MIT License

## Autor

Deanyu148
