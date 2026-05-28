# AutoType（自动输入）

精美、跨平台的自动输入工具。在任意应用中模拟键盘输入，支持逐字符模拟和即时粘贴两种模式。

**其他语言 / Other Languages:**
[English](docs/README-en.md) |
[日本語](docs/README-ja.md) |
[한국어](docs/README-ko.md) |
[Español](docs/README-es.md) |
[Français](docs/README-fr.md) |
[Deutsch](docs/README-de.md) |
[Русский](docs/README-ru.md) |
[Português](docs/README-pt.md) |
[العربية](docs/README-ar.md)

## 功能特性

- **双模式输入** — 逐字符模拟真人打字（带随机延迟波动），或即时剪贴板粘贴
- **特殊键支持** — 支持 Enter、Tab、Esc、方向键、F1–F12 等特殊键令牌
- **预设管理** — 保存、加载、导入/导出预设（YAML 格式），最多 50 组
- **全局快捷键** — F6 开始、F7 停止、F8 切换，可在任意窗口触发
- **系统托盘** — 最小化到托盘，托盘菜单快速控制
- **10 语言界面** — 中文、English、日本語、한국어、Español、Français、Deutsch、Русский、Português、العربية
- **窗口置顶** — 始终保持在最前，方便操作
- **倒计时启动** — 可配置 0–10 秒启动延迟
- **可调速度** — 1–200 CPS（字符/秒）
- **行号显示** — 编辑器带行号、字符/单词/行数统计

## 界面预览

主窗口左侧为文本编辑器，右侧为设置面板和预设列表。底部状态栏显示当前状态。

## 安装

### 从源码运行

```bash
# 克隆仓库
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

### 依赖

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1（Qt 界面框架）
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6（键盘输入模拟 + 全局热键监听）
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50（即时模式）
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0（预设导入/导出）

### 构建 EXE（Windows）

```bash
# 执行构建脚本
build.bat

# 或手动构建
pyinstaller --onefile --windowed --name AutoType --icon AutoType.ico --add-data "AutoType.ico;." main.py
```

## 使用指南

### 基本操作

1. 在左侧文本编辑器中输入或粘贴要自动输入的文本
2. 在右侧调整输入速度、延迟和模式
3. 点击"开始"或按 F6 启动输入
4. 在 3 秒（可配置）倒计时内将光标定位到目标输入框
5. 按 F7 随时停止

### 特殊键令牌

在文本中使用 `{KEY}` 格式插入特殊键：

| 令牌 | 对应按键 |
|---|---|
| `{ENTER}` | 回车 |
| `{TAB}` | Tab |
| `{ESC}` | Escape |
| `{SPACE}` | 空格 |
| `{BACKSPACE}` | 退格 |
| `{DELETE}` | 删除 |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | 方向键 |
| `{HOME}` `{END}` | Home / End |
| `{PAGEUP}` `{PAGEDOWN}` | 翻页 |
| `{F1}` … `{F12}` | 功能键 |

示例：
```
用户名{ENTER}密码{TAB}{ENTER}你好世界，这是自动输入的文本。{ENTER}
```

### 输入模式

- **逐字符模拟（Realistic）** — 使用 pynput 逐字符发送按键，带随机延迟波动，最接近真人打字效果
- **即时粘贴（Instant）** — 使用剪贴板 + Ctrl+V 一次性粘贴，速度最快

### 全局快捷键

| 按键 | 功能 |
|---|---|
| F6 | 开始输入 |
| F7 | 停止输入 |
| F8 | 切换（开始/停止） |

### 预设管理

- 保存当前文本和设置参数为预设（最多 50 组）
- 加载预设自动恢复文本和参数
- 从 YAML 文件导入/导出预设，便于分享和备份
- 支持筛选搜索、批量删除

## 项目结构

```
AutoType/
├── main.py                     # 入口
├── build.bat                   # PyInstaller 构建脚本
├── AutoType.ico                # 应用图标
├── requirements.txt            # 依赖
├── README.md                   # 本文件
├── docs/                       # 其他语言 README
│   ├── README-en.md            # English
│   ├── README-ja.md            # 日本語
│   ├── README-ko.md            # 한국어
│   ├── README-es.md            # Español
│   ├── README-fr.md            # Français
│   ├── README-de.md            # Deutsch
│   ├── README-ru.md            # Русский
│   ├── README-pt.md            # Português
│   └── README-ar.md            # العربية
└── src/
    ├── core/
    │   ├── autotyper.py        # 自动输入引擎（线程）
    │   └── key_simulator.py    # 键盘模拟（pynput / pyautogui）
    ├── ui/
    │   ├── main_window.py      # 主窗口
    │   ├── editor_panel.py     # 文本编辑器面板
    │   ├── settings_panel.py   # 设置面板
    │   ├── preset_manager.py   # 预设管理
    │   ├── widgets.py          # 自定义控件
    │   └── theme.py            # 主题定义
    └── utils/
        ├── config.py           # 配置持久化（JSON）
        └── i18n.py             # 国际化翻译
```

## 技术栈

- **GUI**: PySide6 (Qt for Python)
- **键盘模拟**: pynput（逐字符模式）/ pyautogui（即时模式）
- **配置存储**: JSON（用户配置）/ YAML（预设文件）
- **构建**: PyInstaller（单文件 EXE）

## 许可

MIT License

## 作者

Deanyu148
