# AutoType（自動入力）

PySide6（Qt）と pynput で構築された、美しいクロスプラットフォームの自動入力ツールです。任意のアプリケーションでキーボード入力をシミュレートし、1文字ずつのリアルタイピングとクリップボード貼り付けの2つのモードを提供します。

## 機能

- **デュアル入力モード** — 1文字ずつのリアルタイピング（ランダム遅延付き）または即時クリップボード貼り付け
- **特殊キー対応** — Enter、Tab、Esc、矢印キー、F1〜F12 などの特殊キートークン
- **プリセット管理** — 保存、読み込み、インポート/エクスポート（YAML形式）、最大50件
- **グローバルホットキー** — F6 で開始、F7 で停止、F8 で切り替え（どのウィンドウからでも操作可能）
- **システムトレイ** — タスクトレイに最小化してクイック操作
- **10言語UI** — 中文、English、日本語、한국어、Español、Français、Deutsch、Русский、Português、العربية
- **常に最前面** — ウィンドウを最前面に固定
- **カウントダウン開始** — 0〜10秒の開始遅延を設定可能
- **速度調整** — 1〜200 CPS（文字/秒）
- **行番号表示** — 行番号と文字/単語/行数のカウント付きエディタ

## インストール

### ソースから実行

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### 依存関係

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Qt UI フレームワーク
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — キーボードシミュレーション + グローバルホットキー監視
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — 即時モード
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — プリセットのインポート/エクスポート

### EXE のビルド（Windows）

```bash
build.bat
```

## 使用方法

### 基本操作

1. 左側のテキストエディタに自動入力するテキストを入力または貼り付け
2. 右側で入力速度、遅延、モードを調整
3. 「開始」をクリックまたは F6 を押して開始
4. カウントダウン（デフォルト3秒）の間に対象の入力フィールドにカーソルを配置
5. いつでも F7 で停止可能

### 特殊キートークン

テキスト内で `{KEY}` 形式のトークンを使用：

| トークン | 対応キー |
|---|---|
| `{ENTER}` | Enter |
| `{TAB}` | Tab |
| `{ESC}` | Escape |
| `{SPACE}` | スペース |
| `{BACKSPACE}` | バックスペース |
| `{DELETE}` | Delete |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | 矢印キー |
| `{HOME}` `{END}` | Home / End |
| `{PAGEUP}` `{PAGEDOWN}` | Page Up / Down |
| `{F1}` … `{F12}` | ファンクションキー |

例：
```
ユーザー名{ENTER}パスワード{TAB}{ENTER}これは自動入力されたテキストです。{ENTER}
```

### 入力モード

- **リアル** — pynput を使って1文字ずつキーストロークを送信。ランダムな遅延変動付きで最も人間らしい入力
- **インスタント** — クリップボード + Ctrl+V で一括貼り付け。最速の入力方式

### グローバルホットキー

| キー | 機能 |
|---|---|
| F6 | 入力を開始 |
| F7 | 入力を停止 |
| F8 | 切り替え（開始/停止） |

## プロジェクト構成

```
AutoType/
├── main.py                     # エントリポイント
├── build.bat                   # PyInstaller ビルドスクリプト
├── AutoType.ico                # アプリアイコン
├── requirements.txt            # 依存関係
├── README.md                   # 中国語 README
├── docs/                       # 他言語 README
└── src/
    ├── core/
    │   ├── autotyper.py        # 入力エンジン（スレッド）
    │   └── key_simulator.py    # キーボードシミュレーション
    ├── ui/
    │   ├── main_window.py      # メインウィンドウ
    │   ├── editor_panel.py     # テキストエディタパネル
    │   ├── settings_panel.py   # 設定パネル
    │   ├── preset_manager.py   # プリセット管理
    │   ├── widgets.py          # カスタムウィジェット
    │   └── theme.py            # テーマ定義
    └── utils/
        ├── config.py           # 設定の永続化（JSON）
        └── i18n.py             # 国際化対応
```

## 技術スタック

- **GUI**: PySide6 (Qt for Python)
- **キーボードシミュレーション**: pynput / pyautogui
- **設定保存**: JSON / YAML
- **ビルド**: PyInstaller（単一ファイル EXE）

## ライセンス

MIT License

## 作者

Deanyu148
