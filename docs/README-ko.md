# AutoType（자동 입력）

PySide6(Qt)과 pynput으로 제작된 아름다운 크로스 플랫폼 자동 입력 도구입니다. 모든 애플리케이션에서 키보드 입력을 시뮬레이션하며, 문자별 실감 타이핑과 즉시 클립보드 붙여넣기 두 가지 모드를 제공합니다.

## 기능

- **듀얼 입력 모드** — 문자별 실감 타이핑(무작위 지연 변동 포함) 또는 즉시 클립보드 붙여넣기
- **특수 키 지원** — Enter, Tab, Esc, 방향키, F1~F12 등 특수 키 토큰 지원
- **프리셋 관리** — 저장, 불러오기, 가져오기/내보내기(YAML 형식), 최대 50개
- **글로벌 단축키** — F6 시작, F7 중지, F8 전환 (모든 창에서 작동)
- **시스템 트레이** — 트레이로 최소화하여 빠른 제어
- **10개 UI 언어** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **항상 위에 표시** — 창을 항상 최상단에 고정
- **카운트다운 시작** — 0~10초 시작 지연 설정 가능
- **속도 조절** — 1~200 CPS(초당 문자 수)
- **줄 번호** — 줄 번호 및 문자/단어/줄 수 표시 에디터

## 설치

### 소스에서 실행

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### 의존성

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Qt UI 프레임워크
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — 키보드 시뮬레이션 + 글로벌 단축키 감지
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — 즉시 모드
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — 프리셋 가져오기/내보내기

### EXE 빌드 (Windows)

```bash
build.bat
```

## 사용법

### 기본 조작

1. 왼쪽 텍스트 편집기에 자동 입력할 텍스트를 입력하거나 붙여넣기
2. 오른쪽에서 입력 속도, 지연 시간, 모드 조정
3. "시작" 클릭 또는 F6 키로 시작
4. 카운트다운(기본 3초) 동안 대상 입력 필드에 커서 위치
5. 언제든지 F7로 정지 가능

### 특수 키 토큰

텍스트에 `{KEY}` 형식으로 특수 키를 삽입:

| 토큰 | 키 |
|---|---|
| `{ENTER}` | 엔터 |
| `{TAB}` | 탭 |
| `{ESC}` | 이스케이프 |
| `{SPACE}` | 스페이스 |
| `{BACKSPACE}` | 백스페이스 |
| `{DELETE}` | 삭제 |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | 방향키 |
| `{HOME}` `{END}` | Home / End |
| `{PAGEUP}` `{PAGEDOWN}` | 페이지 업/다운 |
| `{F1}` … `{F12}` | 기능 키 |

예시:
```
사용자명{ENTER}비밀번호{TAB}{ENTER}안녕하세요, 자동 입력된 텍스트입니다.{ENTER}
```

### 입력 모드

- **리얼리스틱** — pynput을 통해 문자별로 키 입력을 전송하며 무작위 지연 변동을 추가하여 실제 타이핑과 유사하게 만듭니다.
- **인스턴트** — 클립보드 + Ctrl+V로 한 번에 붙여넣습니다. 가장 빠른 방식입니다.

### 글로벌 단축키

| 키 | 기능 |
|---|---|
| F6 | 입력 시작 |
| F7 | 입력 중지 |
| F8 | 전환 (시작/중지) |

## 프로젝트 구조

```
AutoType/
├── main.py                     # 진입점
├── build.bat                   # PyInstaller 빌드 스크립트
├── AutoType.ico                # 앱 아이콘
├── requirements.txt            # 의존성
├── README.md                   # 중국어 README
├── docs/                       # 다른 언어 README
└── src/
    ├── core/
    │   ├── autotyper.py        # 입력 엔진 (스레드)
    │   └── key_simulator.py    # 키보드 시뮬레이션
    ├── ui/
    │   ├── main_window.py      # 메인 윈도우
    │   ├── editor_panel.py     # 텍스트 편집기 패널
    │   ├── settings_panel.py   # 설정 패널
    │   ├── preset_manager.py   # 프리셋 관리
    │   ├── widgets.py          # 커스텀 위젯
    │   └── theme.py            # 테마 정의
    └── utils/
        ├── config.py           # 설정 저장 (JSON)
        └── i18n.py             # 국제화
```

## 기술 스택

- **GUI**: PySide6 (Qt for Python)
- **키보드 시뮬레이션**: pynput / pyautogui
- **설정 저장**: JSON / YAML
- **빌드**: PyInstaller (단일 파일 EXE)

## 라이선스

MIT License

## 저자

Deanyu148
