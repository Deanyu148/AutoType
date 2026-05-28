"""Internationalization — multi-language support."""
from __future__ import annotations

LANGUAGES = {
    "zh": "中文",
    "en": "English",
    "ja": "日本語",
    "ko": "한국어",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ru": "Русский",
    "pt": "Português",
    "ar": "العربية",
}

# ── All translatable texts ─────────────────────────────────────────
# Each key maps to a dict of language_code → translation.
# Keys: zh, en, ja, ko, es, fr, de, ru, pt, ar

TEXTS = {
    # ── Window & Menus ────────────────────────────
    "app.title": {
        "zh": "自动输入", "en": "AutoType",
        "ja": "自動入力", "ko": "자동 입력", "es": "AutoType", "fr": "AutoType",
        "de": "AutoType", "ru": "Авто ввод", "pt": "AutoType", "ar": "أوتو تايب",
    },
    "menu.file": {
        "zh": "文件(&F)", "en": "&File",
        "ja": "ファイル(&F)", "ko": "파일(&F)", "es": "&Archivo", "fr": "&Fichier",
        "de": "&Datei", "ru": "&Файл", "pt": "&Arquivo", "ar": "&ملف",
    },
    "menu.window": {
        "zh": "窗口(&W)", "en": "&Window",
        "ja": "ウィンドウ(&W)", "ko": "창(&W)", "es": "&Ventana", "fr": "&Fenêtre",
        "de": "&Fenster", "ru": "&Окно", "pt": "&Janela", "ar": "&نافذة",
    },
    "menu.help": {
        "zh": "帮助(&H)", "en": "&Help",
        "ja": "ヘルプ(&H)", "ko": "도움말(&H)", "es": "A&yuda", "fr": "&Aide",
        "de": "&Hilfe", "ru": "&Справка", "pt": "A&juda", "ar": "&مساعدة",
    },
    "menu.new_preset": {
        "zh": "新建预设...", "en": "New Preset...",
        "ja": "新規プリセット...", "ko": "새 프리셋...", "es": "Nuevo preset...",
        "fr": "Nouveau préréglage...", "de": "Neue Voreinstellung...",
        "ru": "Новый пресет...", "pt": "Nova predefinição...", "ar": "إعداد مسبق جديد...",
    },
    "menu.import": {
        "zh": "导入文本文件...", "en": "Import Text File...",
        "ja": "テキストファイルをインポート...", "ko": "텍스트 파일 가져오기...",
        "es": "Importar archivo de texto...", "fr": "Importer un fichier texte...",
        "de": "Textdatei importieren...", "ru": "Импорт текстового файла...",
        "pt": "Importar arquivo de texto...", "ar": "استيراد ملف نصي...",
    },
    "menu.export": {
        "zh": "导出到文件...", "en": "Export to File...",
        "ja": "ファイルにエクスポート...", "ko": "파일로 내보내기...",
        "es": "Exportar a archivo...", "fr": "Exporter vers un fichier...",
        "de": "In Datei exportieren...", "ru": "Экспорт в файл...",
        "pt": "Exportar para arquivo...", "ar": "تصدير إلى ملف...",
    },
    "menu.exit": {
        "zh": "退出", "en": "Exit",
        "ja": "終了", "ko": "종료", "es": "Salir", "fr": "Quitter",
        "de": "Beenden", "ru": "Выход", "pt": "Sair", "ar": "خروج",
    },
    "menu.always_on_top": {
        "zh": "窗口置顶 (Alt+T)", "en": "Always on Top (Alt+T)",
        "ja": "最前面に表示 (Alt+T)", "ko": "항상 위에 표시 (Alt+T)",
        "es": "Siempre visible (Alt+T)", "fr": "Toujours au premier plan (Alt+T)",
        "de": "Immer im Vordergrund (Alt+T)", "ru": "Поверх всех окон (Alt+T)",
        "pt": "Sempre no topo (Alt+T)", "ar": "دائما في المقدمة (Alt+T)",
    },
    "menu.hotkey_ref": {
        "zh": "快捷键参考...", "en": "Hotkey Reference...",
        "ja": "ホットキーリファレンス...", "ko": "단축키 참조...",
        "es": "Referencia de atajos...", "fr": "Référence des raccourcis...",
        "de": "Tastenkürzel-Referenz...", "ru": "Справка по горячим клавишам...",
        "pt": "Referência de atalhos...", "ar": "مرجع مفاتيح الاختصار...",
    },
    "menu.language": {
        "zh": "语言(&L)", "en": "&Language",
        "ja": "言語(&L)", "ko": "언어(&L)", "es": "&Idioma", "fr": "&Langue",
        "de": "&Sprache", "ru": "&Язык", "pt": "&Idioma", "ar": "&اللغة",
    },
    "menu.about": {
        "zh": "关于自动输入", "en": "About AutoType",
        "ja": "自動入力について", "ko": "AutoType 정보",
        "es": "Acerca de AutoType", "fr": "À propos d'AutoType",
        "de": "Über AutoType", "ru": "О программе AutoType",
        "pt": "Sobre o AutoType", "ar": "حول أوتو تايب",
    },

    # ── Buttons ────────────────────────────────────
    "btn.start": {
        "zh": "开始", "en": "Start",
        "ja": "開始", "ko": "시작", "es": "Iniciar", "fr": "Démarrer",
        "de": "Start", "ru": "Старт", "pt": "Iniciar", "ar": "بدء",
    },
    "btn.pause": {
        "zh": "暂停", "en": "Pause",
        "ja": "一時停止", "ko": "일시 정지", "es": "Pausa", "fr": "Pause",
        "de": "Pause", "ru": "Пауза", "pt": "Pausar", "ar": "إيقاف مؤقت",
    },
    "btn.resume": {
        "zh": "继续", "en": "Resume",
        "ja": "再開", "ko": "재개", "es": "Reanudar", "fr": "Reprendre",
        "de": "Fortsetzen", "ru": "Продолжить", "pt": "Retomar", "ar": "استئناف",
    },
    "btn.stop": {
        "zh": "停止", "en": "Stop",
        "ja": "停止", "ko": "정지", "es": "Detener", "fr": "Arrêter",
        "de": "Stopp", "ru": "Стоп", "pt": "Parar", "ar": "إيقاف",
    },
    "btn.load": {
        "zh": "加载", "en": "Load",
        "ja": "読み込み", "ko": "불러오기", "es": "Cargar", "fr": "Charger",
        "de": "Laden", "ru": "Загрузить", "pt": "Carregar", "ar": "تحميل",
    },
    "btn.save": {
        "zh": "保存", "en": "Save",
        "ja": "保存", "ko": "저장", "es": "Guardar", "fr": "Enregistrer",
        "de": "Speichern", "ru": "Сохранить", "pt": "Salvar", "ar": "حفظ",
    },
    "btn.delete": {
        "zh": "删除", "en": "Delete",
        "ja": "削除", "ko": "삭제", "es": "Eliminar", "fr": "Supprimer",
        "de": "Löschen", "ru": "Удалить", "pt": "Excluir", "ar": "حذف",
    },
    "btn.rename": {
        "zh": "重命名", "en": "Rename",
        "ja": "名前変更", "ko": "이름 변경", "es": "Renombrar", "fr": "Renommer",
        "de": "Umbenennen", "ru": "Переименовать", "pt": "Renomear", "ar": "إعادة تسمية",
    },
    "btn.export": {
        "zh": "导出...", "en": "Export...",
        "ja": "エクスポート...", "ko": "내보내기...", "es": "Exportar...",
        "fr": "Exporter...", "de": "Exportieren...", "ru": "Экспорт...",
        "pt": "Exportar...", "ar": "تصدير...",
    },
    "btn.close": {
        "zh": "关闭", "en": "Close",
        "ja": "閉じる", "ko": "닫기", "es": "Cerrar", "fr": "Fermer",
        "de": "Schließen", "ru": "Закрыть", "pt": "Fechar", "ar": "إغلاق",
    },
    "btn.save_preset": {
        "zh": "保存预设", "en": "Save Preset",
        "ja": "プリセットを保存", "ko": "프리셋 저장", "es": "Guardar preset",
        "fr": "Enregistrer le préréglage", "de": "Voreinstellung speichern",
        "ru": "Сохранить пресет", "pt": "Salvar predefinição", "ar": "حفظ الإعداد المسبق",
    },
    "btn.cancel": {
        "zh": "取消", "en": "Cancel",
        "ja": "キャンセル", "ko": "취소", "es": "Cancelar", "fr": "Annuler",
        "de": "Abbrechen", "ru": "Отмена", "pt": "Cancelar", "ar": "إلغاء",
    },
    "btn.manage_presets": {
        "zh": "管理预设...", "en": "Manage Presets...",
        "ja": "プリセット管理...", "ko": "프리셋 관리...", "es": "Gestionar presets...",
        "fr": "Gérer les préréglages...", "de": "Voreinstellungen verwalten...",
        "ru": "Управление пресетами...", "pt": "Gerenciar predefinições...",
        "ar": "إدارة الإعدادات المسبقة...",
    },
    "btn.delete_all": {
        "zh": "删除全部", "en": "Delete All",
        "ja": "すべて削除", "ko": "모두 삭제", "es": "Eliminar todo",
        "fr": "Tout supprimer", "de": "Alle löschen", "ru": "Удалить всё",
        "pt": "Excluir todos", "ar": "حذف الكل",
    },
    "btn.clear": {
        "zh": "清空", "en": "Clear",
        "ja": "クリア", "ko": "지우기", "es": "Limpiar", "fr": "Effacer",
        "de": "Leeren", "ru": "Очистить", "pt": "Limpar", "ar": "مسح",
    },
    "btn.export_all": {
        "zh": "导出全部...", "en": "Export All...",
        "ja": "すべてエクスポート...", "ko": "모두 내보내기...", "es": "Exportar todo...",
        "fr": "Tout exporter...", "de": "Alle exportieren...",
        "ru": "Экспортировать всё...", "pt": "Exportar todos...", "ar": "تصدير الكل...",
    },
    "btn.import_presets": {
        "zh": "导入...", "en": "Import...",
        "ja": "インポート...", "ko": "가져오기...",
        "es": "Importar...", "fr": "Importer...",
        "de": "Importieren...", "ru": "Импорт...",
        "pt": "Importar...", "ar": "استيراد...",
    },
    "btn.select_all": {
        "zh": "全选", "en": "Select All",
        "ja": "すべて選択", "ko": "모두 선택", "es": "Seleccionar todo",
        "fr": "Tout sélectionner", "de": "Alle auswählen",
        "ru": "Выбрать всё", "pt": "Selecionar todos", "ar": "تحديد الكل",
    },
    "btn.deselect_all": {
        "zh": "取消全选", "en": "Deselect All",
        "ja": "選択解除", "ko": "모두 선택 해제", "es": "Deseleccionar todo",
        "fr": "Tout désélectionner", "de": "Auswahl aufheben",
        "ru": "Снять выбор", "pt": "Desmarcar todos", "ar": "إلغاء تحديد الكل",
    },
    "btn.import_selected": {
        "zh": "导入选中", "en": "Import Selected",
        "ja": "選択をインポート", "ko": "선택 가져오기", "es": "Importar selección",
        "fr": "Importer la sélection", "de": "Auswahl importieren",
        "ru": "Импорт выбранных", "pt": "Importar selecionados", "ar": "استيراد المحدد",
    },

    # ── Typing states ─────────────────────────────
    "state.running": {
        "zh": "运行中...", "en": "Running...",
        "ja": "実行中...", "ko": "실행 중...", "es": "Ejecutando...",
        "fr": "En cours...", "de": "Läuft...", "ru": "Выполняется...",
        "pt": "Executando...", "ar": "جارٍ التشغيل...",
    },
    "state.paused": {
        "zh": "已暂停", "en": "Paused",
        "ja": "一時停止中", "ko": "일시 정지됨", "es": "Pausado",
        "fr": "En pause", "de": "Pausiert", "ru": "Приостановлено",
        "pt": "Pausado", "ar": "متوقف مؤقتاً",
    },
    "state.ready": {
        "zh": "就绪", "en": "Ready",
        "ja": "準備完了", "ko": "준비", "es": "Listo", "fr": "Prêt",
        "de": "Bereit", "ru": "Готов", "pt": "Pronto", "ar": "جاهز",
    },
    "state.countdown": {
        "zh": "倒计时", "en": "Countdown",
        "ja": "カウントダウン", "ko": "카운트다운", "es": "Cuenta regresiva",
        "fr": "Compte à rebours", "de": "Countdown", "ru": "Обратный отсчёт",
        "pt": "Contagem regressiva", "ar": "عد تنازلي",
    },
    "state.typing": {
        "zh": "输入中", "en": "Typing",
        "ja": "入力中", "ko": "입력 중", "es": "Escribiendo",
        "fr": "Saisie en cours", "de": "Tippt", "ru": "Ввод...",
        "pt": "Digitando", "ar": "جارٍ الكتابة",
    },
    "state.error": {
        "zh": "错误", "en": "Error",
        "ja": "エラー", "ko": "오류", "es": "Error", "fr": "Erreur",
        "de": "Fehler", "ru": "Ошибка", "pt": "Erro", "ar": "خطأ",
    },
    "state.complete": {
        "zh": "完成", "en": "Complete",
        "ja": "完了", "ko": "완료", "es": "Completado", "fr": "Terminé",
        "de": "Abgeschlossen", "ru": "Завершено", "pt": "Concluído", "ar": "مكتمل",
    },

    # ── Section titles ────────────────────────────
    "section.text_input": {
        "zh": "文本输入", "en": "Text Input",
        "ja": "テキスト入力", "ko": "텍스트 입력", "es": "Entrada de texto",
        "fr": "Saisie de texte", "de": "Texteingabe", "ru": "Ввод текста",
        "pt": "Entrada de texto", "ar": "إدخال النص",
    },
    "section.settings": {
        "zh": "输入设置", "en": "Typing Settings",
        "ja": "入力設定", "ko": "입력 설정", "es": "Configuración de escritura",
        "fr": "Paramètres de saisie", "de": "Eingabeeinstellungen",
        "ru": "Настройки ввода", "pt": "Configurações de digitação", "ar": "إعدادات الكتابة",
    },
    "section.presets": {
        "zh": "预设", "en": "Presets",
        "ja": "プリセット", "ko": "프리셋", "es": "Presets", "fr": "Préréglages",
        "de": "Voreinstellungen", "ru": "Пресеты", "pt": "Predefinições", "ar": "الإعدادات المسبقة",
    },
    "section.control": {
        "zh": "控制", "en": "Control",
        "ja": "コントロール", "ko": "제어", "es": "Control", "fr": "Contrôle",
        "de": "Steuerung", "ru": "Управление", "pt": "Controle", "ar": "التحكم",
    },
    "section.status": {
        "zh": "状态", "en": "Status",
        "ja": "ステータス", "ko": "상태", "es": "Estado", "fr": "Statut",
        "de": "Status", "ru": "Статус", "pt": "Status", "ar": "الحالة",
    },
    "section.manage_presets": {
        "zh": "管理预设", "en": "Manage Presets",
        "ja": "プリセット管理", "ko": "프리셋 관리", "es": "Gestionar presets",
        "fr": "Gérer les préréglages", "de": "Voreinstellungen verwalten",
        "ru": "Управление пресетами", "pt": "Gerenciar predefinições",
        "ar": "إدارة الإعدادات المسبقة",
    },

    # ── Settings labels ───────────────────────────
    "settings.speed": {
        "zh": "输入速度", "en": "Typing Speed",
        "ja": "入力速度", "ko": "입력 속도", "es": "Velocidad de escritura",
        "fr": "Vitesse de frappe", "de": "Eingabegeschwindigkeit",
        "ru": "Скорость ввода", "pt": "Velocidade de digitação", "ar": "سرعة الكتابة",
    },
    "settings.speed_tip": {
        "zh": "每秒输入字符数，50 CPS 约等于平均打字速度。",
        "en": "Characters per second. 50 CPS is about average typing speed.",
        "ja": "1秒あたりの文字数。50 CPSは平均的なタイピング速度です。",
        "ko": "초당 문자 수. 50 CPS는 평균 타이핑 속도입니다.",
        "es": "Caracteres por segundo. 50 CPS equivale a la velocidad promedio.",
        "fr": "Caractères par seconde. 50 CPS correspond à la vitesse moyenne.",
        "de": "Zeichen pro Sekunde. 50 CPS entspricht der Durchschnittsgeschwindigkeit.",
        "ru": "Символов в секунду. 50 CPS — средняя скорость печати.",
        "pt": "Caracteres por segundo. 50 CPS é a velocidade média de digitação.",
        "ar": "حرف في الثانية. 50 حرف/ثانية هو متوسط سرعة الكتابة.",
    },
    "settings.delay": {
        "zh": "启动延迟", "en": "Start Delay",
        "ja": "開始遅延", "ko": "시작 지연", "es": "Retardo inicial",
        "fr": "Délai de démarrage", "de": "Startverzögerung",
        "ru": "Задержка старта", "pt": "Atraso inicial", "ar": "تأخير البدء",
    },
    "settings.mode_group": {
        "zh": "输入模式", "en": "Typing Mode",
        "ja": "入力モード", "ko": "입력 모드", "es": "Modo de escritura",
        "fr": "Mode de saisie", "de": "Eingabemodus",
        "ru": "Режим ввода", "pt": "Modo de digitação", "ar": "وضع الكتابة",
    },
    "settings.mode_real": {
        "zh": "逐字符模拟 (模拟真人打字)", "en": "Realistic (char by char)",
        "ja": "リアル (1文字ずつ)", "ko": "리얼리스틱 (문자별)",
        "es": "Realista (carácter por carácter)", "fr": "Réaliste (caractère par caractère)",
        "de": "Realistisch (Zeichen für Zeichen)", "ru": "Реалистичный (посимвольно)",
        "pt": "Realista (caractere por caractere)", "ar": "واقعي (حرف حرف)",
    },
    "settings.mode_instant": {
        "zh": "即时粘贴 (剪贴板)", "en": "Instant (clipboard paste)",
        "ja": "インスタント (クリップボード)", "ko": "즉시 (클립보드 붙여넣기)",
        "es": "Instantáneo (pegar del portapapeles)", "fr": "Instantané (coller du presse-papiers)",
        "de": "Sofort (Zwischenablage)", "ru": "Мгновенный (вставка из буфера)",
        "pt": "Instantâneo (colar da área de transferência)", "ar": "فوري (لصق من الحافظة)",
    },
    "settings.variance": {
        "zh": "随机延迟波动", "en": "Random Variance",
        "ja": "ランダム変動", "ko": "무작위 변동", "es": "Variación aleatoria",
        "fr": "Variation aléatoire", "de": "Zufällige Abweichung",
        "ru": "Случайная вариация", "pt": "Variação aleatória", "ar": "تباين عشوائي",
    },
    "settings.variance_tip": {
        "zh": "模拟真人打字的随机延迟变化。",
        "en": "Random delay variation to simulate human-like typing.",
        "ja": "人間らしいタイピングをシミュレートするためのランダムな遅延変動。",
        "ko": "사람과 같은 타이핑을 시뮬레이션하는 무작위 지연 변동.",
        "es": "Variación aleatoria para simular escritura humana.",
        "fr": "Variation aléatoire pour simuler une frappe humaine.",
        "de": "Zufällige Verzögerung zur Simulation menschlicher Eingaben.",
        "ru": "Случайная вариация задержки для имитации живого ввода.",
        "pt": "Variação aleatória para simular digitação humana.",
        "ar": "تباين عشوائي في التأخير لمحاكاة الكتابة البشرية.",
    },
    "settings.always_on_top": {
        "zh": "窗口置顶 (Alt+T)", "en": "Always on Top (Alt+T)",
        "ja": "最前面に表示 (Alt+T)", "ko": "항상 위에 표시 (Alt+T)",
        "es": "Siempre visible (Alt+T)", "fr": "Toujours au premier plan (Alt+T)",
        "de": "Immer im Vordergrund (Alt+T)", "ru": "Поверх всех окон (Alt+T)",
        "pt": "Sempre no topo (Alt+T)", "ar": "دائما في المقدمة (Alt+T)",
    },

    # ── Speed unit ─────────────────────────────────
    "unit.cps": {
        "zh": "CPS", "en": "CPS",
        "ja": "CPS", "ko": "CPS", "es": "CPS", "fr": "CPS",
        "de": "CPS", "ru": "CPS", "pt": "CPS", "ar": "حرف/ث",
    },
    "unit.sec": {
        "zh": "秒", "en": "sec",
        "ja": "秒", "ko": "초", "es": "seg", "fr": "sec",
        "de": "Sek", "ru": "сек", "pt": "seg", "ar": "ثانية",
    },
    "unit.pct": {
        "zh": "%", "en": "%",
        "ja": "%", "ko": "%", "es": "%", "fr": "%",
        "de": "%", "ru": "%", "pt": "%", "ar": "٪",
    },

    # ── Editor ────────────────────────────────────
    "editor.placeholder": {
        "zh": "在此输入或粘贴文本...\n\n特殊键: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "en": "Type or paste your text here...\n\nSpecial keys: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "ja": "テキストを入力または貼り付け...\n\n特殊キー: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "ko": "텍스트를 입력하거나 붙여넣으세요...\n\n특수 키: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "es": "Escriba o pegue su texto aquí...\n\nTeclas especiales: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "fr": "Saisissez ou collez votre texte ici...\n\nTouches spéciales: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "de": "Text hier eingeben oder einfügen...\n\nSondertasten: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "ru": "Введите или вставьте текст...\n\nСпецклавиши: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "pt": "Digite ou cole seu texto aqui...\n\nTeclas especiais: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
        "ar": "اكتب أو الصق النص هنا...\n\nمفاتيح خاصة: {ENTER} {TAB} {ESC} {BACKSPACE}\n{UP} {DOWN} {LEFT} {RIGHT} {SPACE}",
    },
    "editor.chars": {
        "zh": "字符", "en": "Chars",
        "ja": "文字", "ko": "문자", "es": "Caracteres", "fr": "Caractères",
        "de": "Zeichen", "ru": "Симв.", "pt": "Caracteres", "ar": "حروف",
    },
    "editor.words": {
        "zh": "单词", "en": "Words",
        "ja": "単語", "ko": "단어", "es": "Palabras", "fr": "Mots",
        "de": "Wörter", "ru": "Слов", "pt": "Palavras", "ar": "كلمات",
    },
    "editor.lines": {
        "zh": "行数", "en": "Lines",
        "ja": "行", "ko": "줄", "es": "Líneas", "fr": "Lignes",
        "de": "Zeilen", "ru": "Строк", "pt": "Linhas", "ar": "أسطر",
    },

    # ── Presets ───────────────────────────────────
    "presets.no_presets": {
        "zh": "(无预设)", "en": "(no presets)",
        "ja": "(プリセットなし)", "ko": "(프리셋 없음)", "es": "(sin presets)",
        "fr": "(aucun préréglage)", "de": "(keine Voreinstellungen)",
        "ru": "(нет пресетов)", "pt": "(sem predefinições)", "ar": "(لا توجد إعدادات مسبقة)",
    },
    "presets.filter": {
        "zh": "筛选预设...", "en": "Filter presets...",
        "ja": "プリセットをフィルター...", "ko": "프리셋 필터...", "es": "Filtrar presets...",
        "fr": "Filtrer les préréglages...", "de": "Voreinstellungen filtern...",
        "ru": "Фильтр пресетов...", "pt": "Filtrar predefinições...", "ar": "تصفية الإعدادات المسبقة...",
    },
    "presets.preview": {
        "zh": "预览:", "en": "Preview:",
        "ja": "プレビュー:", "ko": "미리보기:", "es": "Vista previa:",
        "fr": "Aperçu:", "de": "Vorschau:", "ru": "Просмотр:",
        "pt": "Pré-visualização:", "ar": "معاينة:",
    },
    "presets.new_title": {
        "zh": "新建预设", "en": "New Preset",
        "ja": "新規プリセット", "ko": "새 프리셋", "es": "Nuevo preset",
        "fr": "Nouveau préréglage", "de": "Neue Voreinstellung",
        "ru": "Новый пресет", "pt": "Nova predefinição", "ar": "إعداد مسبق جديد",
    },
    "presets.name": {
        "zh": "预设名称:", "en": "Preset name:",
        "ja": "プリセット名:", "ko": "프리셋 이름:", "es": "Nombre del preset:",
        "fr": "Nom du préréglage:", "de": "Name der Voreinstellung:",
        "ru": "Имя пресета:", "pt": "Nome da predefinição:", "ar": "اسم الإعداد المسبق:",
    },
    "presets.name_holder": {
        "zh": "输入预设名称...", "en": "Enter preset name...",
        "ja": "プリセット名を入力...", "ko": "프리셋 이름 입력...", "es": "Ingrese nombre del preset...",
        "fr": "Entrez le nom du préréglage...", "de": "Name der Voreinstellung eingeben...",
        "ru": "Введите имя пресета...", "pt": "Digite o nome da predefinição...",
        "ar": "أدخل اسم الإعداد المسبق...",
    },
    "presets.text_label": {
        "zh": "输入文本:", "en": "Text:",
        "ja": "テキスト:", "ko": "텍스트:", "es": "Texto:",
        "fr": "Texte:", "de": "Text:", "ru": "Текст:",
        "pt": "Texto:", "ar": "النص:",
    },
    "presets.placeholder": {
        "zh": "在此输入或粘贴文本...", "en": "Type or paste text here...",
        "ja": "テキストを入力または貼り付け...", "ko": "텍스트를 입력하거나 붙여넣으세요...",
        "es": "Escriba o pegue texto aquí...", "fr": "Saisissez ou collez du texte ici...",
        "de": "Text hier eingeben oder einfügen...", "ru": "Введите или вставьте текст...",
        "pt": "Digite ou cole texto aqui...", "ar": "اكتب أو الصق النص هنا...",
    },
    "presets.params": {
        "zh": "输入参数", "en": "Typing Parameters",
        "ja": "入力パラメータ", "ko": "입력 매개변수", "es": "Parámetros de escritura",
        "fr": "Paramètres de saisie", "de": "Eingabeparameter",
        "ru": "Параметры ввода", "pt": "Parâmetros de digitação", "ar": "معلمات الكتابة",
    },
    "presets.speed_label": {
        "zh": "速度(CPS)", "en": "Speed (CPS)",
        "ja": "速度(CPS)", "ko": "속도(CPS)", "es": "Velocidad (CPS)",
        "fr": "Vitesse (CPS)", "de": "Geschwindigkeit (CPS)",
        "ru": "Скорость (CPS)", "pt": "Velocidade (CPS)", "ar": "السرعة (حرف/ث)",
    },
    "presets.delay_label": {
        "zh": "延迟(秒)", "en": "Delay (sec)",
        "ja": "遅延(秒)", "ko": "지연(초)", "es": "Retardo (seg)",
        "fr": "Délai (sec)", "de": "Verzögerung (Sek)",
        "ru": "Задержка (сек)", "pt": "Atraso (seg)", "ar": "التأخير (ثانية)",
    },
    "presets.mode_label": {
        "zh": "模式", "en": "Mode",
        "ja": "モード", "ko": "모드", "es": "Modo", "fr": "Mode",
        "de": "Modus", "ru": "Режим", "pt": "Modo", "ar": "الوضع",
    },
    "presets.mode_char": {
        "zh": "逐字符", "en": "Char",
        "ja": "文字単位", "ko": "문자별", "es": "Carácter", "fr": "Caractère",
        "de": "Zeichen", "ru": "Посимв.", "pt": "Caractere", "ar": "حرف",
    },
    "presets.mode_instant": {
        "zh": "即时", "en": "Instant",
        "ja": "インスタント", "ko": "즉시", "es": "Instantáneo", "fr": "Instantané",
        "de": "Sofort", "ru": "Мгнов.", "pt": "Instantâneo", "ar": "فوري",
    },
    "presets.variance_label": {
        "zh": "波动(%)", "en": "Variance (%)",
        "ja": "変動(%)", "ko": "변동(%)", "es": "Variación (%)",
        "fr": "Variation (%)", "de": "Abweichung (%)",
        "ru": "Вариация (%)", "pt": "Variação (%)", "ar": "التباين (٪)",
    },
    "presets.no_params": {
        "zh": "（未设置参数）", "en": "(no parameters set)",
        "ja": "（パラメータ未設定）", "ko": "(매개변수 미설정)", "es": "(sin parámetros)",
        "fr": "(aucun paramètre défini)", "de": "(keine Parameter gesetzt)",
        "ru": "(параметры не заданы)", "pt": "(sem parâmetros)", "ar": "(لم يتم تعيين معلمات)",
    },
    "presets.count": {
        "zh": "{} / {}", "en": "{} / {}",
        "ja": "{} / {}", "ko": "{} / {}", "es": "{} / {}", "fr": "{} / {}",
        "de": "{} / {}", "ru": "{} / {}", "pt": "{} / {}", "ar": "{} / {}",
    },

    # ── Dialogs ───────────────────────────────────
    "dlg.no_text": {
        "zh": "无文本", "en": "No Text",
        "ja": "テキストなし", "ko": "텍스트 없음", "es": "Sin texto",
        "fr": "Pas de texte", "de": "Kein Text", "ru": "Нет текста",
        "pt": "Sem texto", "ar": "لا يوجد نص",
    },
    "dlg.enter_text": {
        "zh": "请输入要自动输入的文本。", "en": "Please enter some text to type.",
        "ja": "自動入力するテキストを入力してください。", "ko": "입력할 텍스트를 입력하세요.",
        "es": "Ingrese el texto a escribir.", "fr": "Veuillez saisir du texte à taper.",
        "de": "Bitte geben Sie Text zum Tippen ein.", "ru": "Введите текст для автоматического ввода.",
        "pt": "Digite o texto a ser inserido.", "ar": "يرجى إدخال نص للكتابة.",
    },
    "dlg.config_error": {
        "zh": "配置错误", "en": "Config Error",
        "ja": "設定エラー", "ko": "설정 오류", "es": "Error de configuración",
        "fr": "Erreur de configuration", "de": "Konfigurationsfehler",
        "ru": "Ошибка конфигурации", "pt": "Erro de configuração", "ar": "خطأ في الإعدادات",
    },
    "dlg.config_failed": {
        "zh": "加载配置失败", "en": "Failed to load config",
        "ja": "設定の読み込みに失敗しました", "ko": "설정 로드 실패",
        "es": "Error al cargar configuración", "fr": "Échec du chargement de la configuration",
        "de": "Konfiguration konnte nicht geladen werden", "ru": "Не удалось загрузить конфигурацию",
        "pt": "Falha ao carregar configuração", "ar": "فشل تحميل الإعدادات",
    },
    "dlg.empty_name": {
        "zh": "名称为空", "en": "Empty Name",
        "ja": "名前が空です", "ko": "이름이 비어 있습니다", "es": "Nombre vacío",
        "fr": "Nom vide", "de": "Leerer Name", "ru": "Пустое имя",
        "pt": "Nome vazio", "ar": "اسم فارغ",
    },
    "dlg.enter_name": {
        "zh": "请输入预设名称。", "en": "Please enter a preset name.",
        "ja": "プリセット名を入力してください。", "ko": "프리셋 이름을 입력하세요.",
        "es": "Ingrese un nombre para el preset.", "fr": "Veuillez entrer un nom de préréglage.",
        "de": "Bitte geben Sie einen Namen ein.", "ru": "Введите имя пресета.",
        "pt": "Digite um nome para a predefinição.", "ar": "يرجى إدخال اسم الإعداد المسبق.",
    },
    "dlg.empty_text": {
        "zh": "文本为空", "en": "Empty Text",
        "ja": "テキストが空です", "ko": "텍스트가 비어 있습니다", "es": "Texto vacío",
        "fr": "Texte vide", "de": "Leerer Text", "ru": "Пустой текст",
        "pt": "Texto vazio", "ar": "نص فارغ",
    },
    "dlg.cannot_save_empty": {
        "zh": "不能保存空预设。", "en": "Cannot save an empty preset.",
        "ja": "空のプリセットは保存できません。", "ko": "빈 프리셋은 저장할 수 없습니다.",
        "es": "No se puede guardar un preset vacío.", "fr": "Impossible d'enregistrer un préréglage vide.",
        "de": "Leere Voreinstellung kann nicht gespeichert werden.", "ru": "Нельзя сохранить пустой пресет.",
        "pt": "Não é possível salvar predefinição vazia.", "ar": "لا يمكن حفظ إعداد مسبق فارغ.",
    },
    "dlg.limit_reached": {
        "zh": "达到上限", "en": "Limit Reached",
        "ja": "上限に達しました", "ko": "한도 도달", "es": "Límite alcanzado",
        "fr": "Limite atteinte", "de": "Limit erreicht", "ru": "Достигнут лимит",
        "pt": "Limite atingido", "ar": "تم الوصول إلى الحد الأقصى",
    },
    "dlg.limit_msg": {
        "zh": "预设数量已达上限 ({} 个)，请先删除旧预设。",
        "en": "Maximum presets ({}) reached. Please delete old presets first.",
        "ja": "プリセット数が上限 ({}) に達しました。古いプリセットを削除してください。",
        "ko": "최대 프리셋 수({})에 도달했습니다. 이전 프리셋을 삭제하세요.",
        "es": "Máximo de presets ({}) alcanzado. Elimine presets antiguos primero.",
        "fr": "Maximum de préréglages ({}) atteint. Supprimez d'anciens préréglages.",
        "de": "Maximale Anzahl ({}) erreicht. Bitte löschen Sie alte Voreinstellungen.",
        "ru": "Достигнут максимум пресетов ({}). Сначала удалите старые.",
        "pt": "Máximo de predefinições ({}) atingido. Exclua as antigas primeiro.",
        "ar": "تم الوصول للحد الأقصى ({}). يرجى حذف القديمة أولا.",
    },
    "dlg.delete_confirm": {
        "zh": "确定要删除 \"{}\" 吗？", "en": "Delete \"{}\"?",
        "ja": "\"{}\" を削除しますか？", "ko": "\"{}\"을(를) 삭제하시겠습니까?",
        "es": "¿Eliminar \"{}\"?", "fr": "Supprimer \"{}\" ?",
        "de": "\"{}\" löschen?", "ru": "Удалить \"{}\"?",
        "pt": "Excluir \"{}\"?", "ar": "حذف \"{}\"؟",
    },
    "dlg.save_preset": {
        "zh": "保存预设", "en": "Save Preset",
        "ja": "プリセットを保存", "ko": "프리셋 저장", "es": "Guardar preset",
        "fr": "Enregistrer le préréglage", "de": "Voreinstellung speichern",
        "ru": "Сохранить пресет", "pt": "Salvar predefinição", "ar": "حفظ الإعداد المسبق",
    },
    "dlg.preset_name": {
        "zh": "预设名称:", "en": "Preset name:",
        "ja": "プリセット名:", "ko": "프리셋 이름:", "es": "Nombre del preset:",
        "fr": "Nom du préréglage:", "de": "Name:", "ru": "Имя пресета:",
        "pt": "Nome:", "ar": "اسم الإعداد المسبق:",
    },
    "dlg.rename_preset": {
        "zh": "重命名预设", "en": "Rename Preset",
        "ja": "プリセット名を変更", "ko": "프리셋 이름 변경", "es": "Renombrar preset",
        "fr": "Renommer le préréglage", "de": "Voreinstellung umbenennen",
        "ru": "Переименовать пресет", "pt": "Renomear predefinição", "ar": "إعادة تسمية الإعداد المسبق",
    },
    "dlg.new_name": {
        "zh": "新名称:", "en": "New name:",
        "ja": "新しい名前:", "ko": "새 이름:", "es": "Nuevo nombre:",
        "fr": "Nouveau nom:", "de": "Neuer Name:", "ru": "Новое имя:",
        "pt": "Novo nome:", "ar": "الاسم الجديد:",
    },
    "dlg.delete_preset": {
        "zh": "删除预设", "en": "Delete Preset",
        "ja": "プリセットを削除", "ko": "프리셋 삭제", "es": "Eliminar preset",
        "fr": "Supprimer le préréglage", "de": "Voreinstellung löschen",
        "ru": "Удалить пресет", "pt": "Excluir predefinição", "ar": "حذف الإعداد المسبق",
    },
    "dlg.export_preset": {
        "zh": "导出预设", "en": "Export Preset",
        "ja": "プリセットをエクスポート", "ko": "프리셋 내보내기", "es": "Exportar preset",
        "fr": "Exporter le préréglage", "de": "Voreinstellung exportieren",
        "ru": "Экспорт пресета", "pt": "Exportar predefinição", "ar": "تصدير الإعداد المسبق",
    },
    "dlg.typing_error": {
        "zh": "输入错误", "en": "Typing Error",
        "ja": "入力エラー", "ko": "입력 오류", "es": "Error de escritura",
        "fr": "Erreur de saisie", "de": "Eingabefehler", "ru": "Ошибка ввода",
        "pt": "Erro de digitação", "ar": "خطأ في الكتابة",
    },
    "dlg.typing_in_progress": {
        "zh": "正在输入中", "en": "Typing in Progress",
        "ja": "入力中", "ko": "입력 진행 중", "es": "Escritura en progreso",
        "fr": "Saisie en cours", "de": "Eingabe läuft", "ru": "Идёт ввод",
        "pt": "Digitação em andamento", "ar": "الكتابة قيد التقدم",
    },
    "dlg.stop_and_exit": {
        "zh": "输入正在进行，确定停止并退出？",
        "en": "Typing is in progress. Stop and exit?",
        "ja": "入力が進行中です。停止して終了しますか？",
        "ko": "입력이 진행 중입니다. 중지하고 종료하시겠습니까?",
        "es": "Escritura en progreso. ¿Detener y salir?",
        "fr": "Saisie en cours. Arrêter et quitter ?",
        "de": "Eingabe läuft. Stoppen und beenden?",
        "ru": "Идёт ввод. Остановить и выйти?",
        "pt": "Digitação em andamento. Parar e sair?",
        "ar": "الكتابة قيد التقدم. إيقاف وخروج؟",
    },
    "dlg.import_error": {
        "zh": "导入错误", "en": "Import Error",
        "ja": "インポートエラー", "ko": "가져오기 오류", "es": "Error de importación",
        "fr": "Erreur d'importation", "de": "Importfehler", "ru": "Ошибка импорта",
        "pt": "Erro de importação", "ar": "خطأ في الاستيراد",
    },
    "dlg.read_failed": {
        "zh": "读取文件失败", "en": "Failed to read file",
        "ja": "ファイルの読み取りに失敗しました", "ko": "파일 읽기 실패",
        "es": "Error al leer archivo", "fr": "Échec de lecture du fichier",
        "de": "Datei konnte nicht gelesen werden", "ru": "Не удалось прочитать файл",
        "pt": "Falha ao ler arquivo", "ar": "فشل قراءة الملف",
    },
    "dlg.export_error": {
        "zh": "导出错误", "en": "Export Error",
        "ja": "エクスポートエラー", "ko": "내보내기 오류", "es": "Error de exportación",
        "fr": "Erreur d'exportation", "de": "Exportfehler", "ru": "Ошибка экспорта",
        "pt": "Erro de exportação", "ar": "خطأ في التصدير",
    },
    "dlg.write_failed": {
        "zh": "写入文件失败", "en": "Failed to write file",
        "ja": "ファイルの書き込みに失敗しました", "ko": "파일 쓰기 실패",
        "es": "Error al escribir archivo", "fr": "Échec d'écriture du fichier",
        "de": "Datei konnte nicht geschrieben werden", "ru": "Не удалось записать файл",
        "pt": "Falha ao escrever arquivo", "ar": "فشل كتابة الملف",
    },
    "dlg.sim_error": {
        "zh": "创建输入模拟器失败", "en": "Failed to create simulator",
        "ja": "シミュレーターの作成に失敗しました", "ko": "시뮬레이터 생성 실패",
        "es": "Error al crear simulador", "fr": "Échec de création du simulateur",
        "de": "Simulator konnte nicht erstellt werden", "ru": "Не удалось создать симулятор",
        "pt": "Falha ao criar simulador", "ar": "فشل إنشاء المحاكي",
    },
    "dlg.type_error": {
        "zh": "输入出错", "en": "Typing error",
        "ja": "入力エラー", "ko": "입력 오류", "es": "Error de escritura",
        "fr": "Erreur de saisie", "de": "Eingabefehler", "ru": "Ошибка ввода",
        "pt": "Erro de digitação", "ar": "خطأ كتابة",
    },
    "dlg.confirm": {
        "zh": "确认", "en": "Confirm",
        "ja": "確認", "ko": "확인", "es": "Confirmar", "fr": "Confirmer",
        "de": "Bestätigen", "ru": "Подтверждение", "pt": "Confirmar", "ar": "تأكيد",
    },
    "dlg.delete_all_prompt": {
        "zh": "若要删除所有预设，请输入：我要删除所有预设",
        "en": "To delete all presets, please enter: I want to delete all presets",
        "ja": "すべてのプリセットを削除するには、次のように入力：すべてのプリセットを削除します",
        "ko": "모든 프리셋을 삭제하려면 다음을 입력하세요: 모든 프리셋 삭제",
        "es": "Para eliminar todos los presets, escriba: Quiero eliminar todos los presets",
        "fr": "Pour supprimer tous les préréglages, saisissez: Je veux supprimer tous les préréglages",
        "de": "Zum Löschen aller Voreinstellungen geben Sie ein: Ich möchte alle löschen",
        "ru": "Для удаления всех пресетов введите: Я хочу удалить все пресеты",
        "pt": "Para excluir todas as predefinições, digite: Quero excluir todas",
        "ar": "لحذف جميع الإعدادات المسبقة، أدخل: أريد حذف جميع الإعدادات المسبقة",
    },
    "dlg.delete_all_phrase": {
        "zh": "我要删除所有预设",
        "en": "I want to delete all presets",
        "ja": "すべてのプリセットを削除します",
        "ko": "모든 프리셋 삭제",
        "es": "Quiero eliminar todos los presets",
        "fr": "Je veux supprimer tous les préréglages",
        "de": "Ich möchte alle löschen",
        "ru": "Я хочу удалить все пресеты",
        "pt": "Quero excluir todas",
        "ar": "أريد حذف جميع الإعدادات المسبقة",
    },
    "dlg.delete_all_wrong": {
        "zh": "输入不正确，操作已取消。", "en": "Incorrect input. Operation cancelled.",
        "ja": "入力が正しくありません。操作はキャンセルされました。", "ko": "입력이 올바르지 않습니다. 작업이 취소되었습니다.",
        "es": "Entrada incorrecta. Operación cancelada.", "fr": "Saisie incorrecte. Opération annulée.",
        "de": "Falsche Eingabe. Vorgang abgebrochen.", "ru": "Неверный ввод. Операция отменена.",
        "pt": "Entrada incorreta. Operação cancelada.", "ar": "إدخال غير صحيح. تم إلغاء العملية.",
    },
    "dlg.import_title": {
        "zh": "导入预设", "en": "Import Presets",
        "ja": "プリセットのインポート", "ko": "프리셋 가져오기", "es": "Importar presets",
        "fr": "Importer des préréglages", "de": "Voreinstellungen importieren",
        "ru": "Импорт пресетов", "pt": "Importar predefinições", "ar": "استيراد الإعدادات المسبقة",
    },
    "dlg.import_invalid": {
        "zh": "无效的预设文件格式。", "en": "Invalid preset file format.",
        "ja": "無効なプリセットファイル形式です。", "ko": "잘못된 프리셋 파일 형식입니다.",
        "es": "Formato de archivo de preset no válido.", "fr": "Format de fichier de préréglage invalide.",
        "de": "Ungültiges Dateiformat.", "ru": "Неверный формат файла пресетов.",
        "pt": "Formato de arquivo de predefinição inválido.", "ar": "تنسيق ملف الإعدادات المسبقة غير صالح.",
    },
    "dlg.import_empty": {
        "zh": "文件中没有可导入的预设。", "en": "No presets found in file.",
        "ja": "ファイルにインポート可能なプリセットがありません。", "ko": "파일에 가져올 프리셋이 없습니다.",
        "es": "No se encontraron presets en el archivo.", "fr": "Aucun préréglage trouvé dans le fichier.",
        "de": "Keine Voreinstellungen in der Datei gefunden.", "ru": "Пресеты в файле не найдены.",
        "pt": "Nenhuma predefinição encontrada no arquivo.", "ar": "لم يتم العثور على إعدادات مسبقة في الملف.",
    },
    "dlg.import_count": {
        "zh": "已导入 {} 个预设。", "en": "Imported {} preset(s).",
        "ja": "{} 個のプリセットをインポートしました。", "ko": "{}개의 프리셋을 가져왔습니다.",
        "es": "{} preset(s) importado(s).", "fr": "{} préréglage(s) importé(s).",
        "de": "{} Voreinstellung(en) importiert.", "ru": "Импортировано пресетов: {}.",
        "pt": "{} predefinição(ões) importada(s).", "ar": "تم استيراد {} إعداد مسبق.",
    },
    "dlg.export_all_title": {
        "zh": "导出所有预设", "en": "Export All Presets",
        "ja": "すべてのプリセットをエクスポート", "ko": "모든 프리셋 내보내기",
        "es": "Exportar todos los presets", "fr": "Exporter tous les préréglages",
        "de": "Alle Voreinstellungen exportieren", "ru": "Экспорт всех пресетов",
        "pt": "Exportar todas as predefinições", "ar": "تصدير جميع الإعدادات المسبقة",
    },
    "dlg.export_title": {
        "zh": "导出预设", "en": "Export Presets",
        "ja": "プリセットのエクスポート", "ko": "프리셋 내보내기", "es": "Exportar presets",
        "fr": "Exporter les préréglages", "de": "Voreinstellungen exportieren",
        "ru": "Экспорт пресетов", "pt": "Exportar predefinições", "ar": "تصدير الإعدادات المسبقة",
    },
    "dlg.export_count": {
        "zh": "已导出 {} 个预设。", "en": "Exported {} preset(s).",
        "ja": "{} 個のプリセットをエクスポートしました。", "ko": "{}개의 프리셋을 내보냈습니다.",
        "es": "{} preset(s) exportado(s).", "fr": "{} préréglage(s) exporté(s).",
        "de": "{} Voreinstellung(en) exportiert.", "ru": "Экспортировано пресетов: {}.",
        "pt": "{} predefinição(ões) exportada(s).", "ar": "تم تصدير {} إعداد مسبق.",
    },
    "dlg.export_none": {
        "zh": "未选中任何预设。", "en": "No presets selected.",
        "ja": "プリセットが選択されていません。", "ko": "선택된 프리셋이 없습니다.",
        "es": "No se seleccionaron presets.", "fr": "Aucun préréglage sélectionné.",
        "de": "Keine Voreinstellungen ausgewählt.", "ru": "Пресеты не выбраны.",
        "pt": "Nenhuma predefinição selecionada.", "ar": "لم يتم تحديد إعدادات مسبقة.",
    },

    # ── File filters ──────────────────────────────
    "filter.import": {
        "zh": "文本文件 (*.txt *.md *.py *.json *.html *.css *.js);;所有文件 (*)",
        "en": "Text Files (*.txt *.md *.py *.json *.html *.css *.js);;All Files (*)",
        "ja": "テキストファイル (*.txt *.md *.py *.json *.html *.css *.js);;すべてのファイル (*)",
        "ko": "텍스트 파일 (*.txt *.md *.py *.json *.html *.css *.js);;모든 파일 (*)",
        "es": "Archivos de texto (*.txt *.md *.py *.json *.html *.css *.js);;Todos (*)",
        "fr": "Fichiers texte (*.txt *.md *.py *.json *.html *.css *.js);;Tous (*)",
        "de": "Textdateien (*.txt *.md *.py *.json *.html *.css *.js);;Alle Dateien (*)",
        "ru": "Текстовые файлы (*.txt *.md *.py *.json *.html *.css *.js);;Все файлы (*)",
        "pt": "Arquivos de texto (*.txt *.md *.py *.json *.html *.css *.js);;Todos (*)",
        "ar": "ملفات نصية (*.txt *.md *.py *.json *.html *.css *.js);;جميع الملفات (*)",
    },
    "filter.export_text": {
        "zh": "文本文件 (*.txt);;所有文件 (*)",
        "en": "Text Files (*.txt);;All Files (*)",
        "ja": "テキストファイル (*.txt);;すべてのファイル (*)",
        "ko": "텍스트 파일 (*.txt);;모든 파일 (*)",
        "es": "Archivos de texto (*.txt);;Todos (*)",
        "fr": "Fichiers texte (*.txt);;Tous (*)",
        "de": "Textdateien (*.txt);;Alle Dateien (*)",
        "ru": "Текстовые файлы (*.txt);;Все файлы (*)",
        "pt": "Arquivos de texto (*.txt);;Todos (*)",
        "ar": "ملفات نصية (*.txt);;جميع الملفات (*)",
    },
    "filter.preset_yaml": {
        "zh": "预设文件 (*.yaml *.yml);;所有文件 (*)",
        "en": "Preset Files (*.yaml *.yml);;All Files (*)",
        "ja": "プリセットファイル (*.yaml *.yml);;すべてのファイル (*)",
        "ko": "프리셋 파일 (*.yaml *.yml);;모든 파일 (*)",
        "es": "Archivos de preset (*.yaml *.yml);;Todos (*)",
        "fr": "Fichiers de préréglage (*.yaml *.yml);;Tous (*)",
        "de": "Voreinstellungsdateien (*.yaml *.yml);;Alle Dateien (*)",
        "ru": "Файлы пресетов (*.yaml *.yml);;Все файлы (*)",
        "pt": "Arquivos de predefinição (*.yaml *.yml);;Todos (*)",
        "ar": "ملفات الإعدادات المسبقة (*.yaml *.yml);;جميع الملفات (*)",
    },

    # ── Hotkey reference ──────────────────────────
    "hotkey.title": {
        "zh": "快捷键参考", "en": "Hotkey Reference",
        "ja": "ホットキーリファレンス", "ko": "단축키 참조", "es": "Referencia de atajos",
        "fr": "Référence des raccourcis", "de": "Tastenkürzel-Referenz",
        "ru": "Справка по горячим клавишам", "pt": "Referência de atalhos",
        "ar": "مرجع مفاتيح الاختصار",
    },
    "hotkey.text": {
        "zh": ("快捷键参考\n\n  F6  —  开始输入\n  F7  —  停止输入\n  F8  —  切换 (开始/停止)\n\n"
               "特殊令牌 (在文本中使用):\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
        "en": ("Hotkey Reference\n\n  F6  —  Start typing\n  F7  —  Stop typing\n  F8  —  Toggle (start/stop)\n\n"
               "Special Tokens (use in text):\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
        "ja": ("ホットキーリファレンス\n\n  F6  —  入力を開始\n  F7  —  入力を停止\n  F8  —  切り替え (開始/停止)\n\n"
               "特殊トークン (テキスト内で使用):\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
        "ko": ("단축키 참조\n\n  F6  —  입력 시작\n  F7  —  입력 중지\n  F8  —  전환 (시작/중지)\n\n"
               "특수 토큰 (텍스트에서 사용):\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
        "es": ("Referencia de Atajos\n\n  F6  —  Iniciar escritura\n  F7  —  Detener escritura\n"
               "  F8  —  Alternar (iniciar/detener)\n\nTokens Especiales:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n"
               "  {BACKSPACE}  {DELETE}\n  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n"
               "  {F1} .. {F12}\n"),
        "fr": ("Référence des Raccourcis\n\n  F6  —  Démarrer la saisie\n  F7  —  Arrêter la saisie\n"
               "  F8  —  Basculer (démarrer/arrêter)\n\nJetons Spéciaux:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n"
               "  {BACKSPACE}  {DELETE}\n  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n"
               "  {F1} .. {F12}\n"),
        "de": ("Tastenkürzel-Referenz\n\n  F6  —  Eingabe starten\n  F7  —  Eingabe stoppen\n"
               "  F8  —  Umschalten (starten/stoppen)\n\nSonderzeichen:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n"
               "  {BACKSPACE}  {DELETE}\n  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n"
               "  {F1} .. {F12}\n"),
        "ru": ("Горячие клавиши\n\n  F6  —  Начать ввод\n  F7  —  Остановить ввод\n  F8  —  Переключить\n\n"
               "Специальные токены:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
        "pt": ("Referência de Atalhos\n\n  F6  —  Iniciar digitação\n  F7  —  Parar digitação\n"
               "  F8  —  Alternar (iniciar/parar)\n\nTokens Especiais:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n"
               "  {BACKSPACE}  {DELETE}\n  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n"
               "  {F1} .. {F12}\n"),
        "ar": ("مرجع مفاتيح الاختصار\n\n  F6  —  بدء الكتابة\n  F7  —  إيقاف الكتابة\n  F8  —  تبديل\n\n"
               "رموز خاصة:\n  {ENTER}  {TAB}  {ESC}  {SPACE}\n  {BACKSPACE}  {DELETE}\n"
               "  {UP}  {DOWN}  {LEFT}  {RIGHT}\n  {HOME}  {END}  {PAGEUP}  {PAGEDOWN}\n  {F1} .. {F12}\n"),
    },

    # ── About ─────────────────────────────────────
    "about.title": {
        "zh": "关于自动输入", "en": "About AutoType",
        "ja": "自動入力について", "ko": "AutoType 정보", "es": "Acerca de AutoType",
        "fr": "À propos d'AutoType", "de": "Über AutoType",
        "ru": "О программе AutoType", "pt": "Sobre o AutoType", "ar": "حول أوتو تايب",
    },
    "about.text": {
        "zh": "自动输入 v1.0\n\n一款精美的自动输入工具。\n基于 PySide6 (Qt) 和 pynput 构建。\n\nF6 开始，F7 停止。",
        "en": "AutoType v1.0\n\nA beautiful auto-typing tool.\nBuilt with PySide6 (Qt) and pynput.\n\nF6 to start, F7 to stop.",
        "ja": "自動入力 v1.0\n\n美しい自動入力ツール。\nPySide6 (Qt) と pynput で構築。\n\nF6 で開始、F7 で停止。",
        "ko": "AutoType v1.0\n\n아름다운 자동 입력 도구.\nPySide6 (Qt) 및 pynput 기반.\n\nF6 시작, F7 중지.",
        "es": "AutoType v1.0\n\nUna hermosa herramienta de auto-escritura.\nConstruido con PySide6 (Qt) y pynput.\n\nF6 iniciar, F7 detener.",
        "fr": "AutoType v1.0\n\nUn bel outil de saisie automatique.\nConstruit avec PySide6 (Qt) et pynput.\n\nF6 démarrer, F7 arrêter.",
        "de": "AutoType v1.0\n\nEin schönes Auto-Tipp-Tool.\nErstellt mit PySide6 (Qt) und pynput.\n\nF6 starten, F7 stoppen.",
        "ru": "AutoType v1.0\n\nКрасивый инструмент автоввода.\nСоздан на PySide6 (Qt) и pynput.\n\nF6 старт, F7 стоп.",
        "pt": "AutoType v1.0\n\nUma bela ferramenta de digitação automática.\nConstruído com PySide6 (Qt) e pynput.\n\nF6 iniciar, F7 parar.",
        "ar": "أوتو تايب v1.0\n\nأداة كتابة تلقائية جميلة.\nمبنية باستخدام PySide6 (Qt) و pynput.\n\nF6 بدء، F7 إيقاف.",
    },

    # ── Tray ──────────────────────────────────────
    "tray.show_hide": {
        "zh": "显示 / 隐藏", "en": "Show / Hide",
        "ja": "表示 / 非表示", "ko": "표시 / 숨기기", "es": "Mostrar / Ocultar",
        "fr": "Afficher / Masquer", "de": "Anzeigen / Ausblenden",
        "ru": "Показать / Скрыть", "pt": "Mostrar / Ocultar", "ar": "إظهار / إخفاء",
    },
    "tray.start": {
        "zh": "开始输入", "en": "Start Typing",
        "ja": "入力を開始", "ko": "입력 시작", "es": "Iniciar escritura",
        "fr": "Démarrer la saisie", "de": "Eingabe starten",
        "ru": "Начать ввод", "pt": "Iniciar digitação", "ar": "بدء الكتابة",
    },
    "tray.stop": {
        "zh": "停止输入", "en": "Stop Typing",
        "ja": "入力を停止", "ko": "입력 중지", "es": "Detener escritura",
        "fr": "Arrêter la saisie", "de": "Eingabe stoppen",
        "ru": "Остановить ввод", "pt": "Parar digitação", "ar": "إيقاف الكتابة",
    },
    "tray.quit": {
        "zh": "退出", "en": "Quit",
        "ja": "終了", "ko": "종료", "es": "Salir", "fr": "Quitter",
        "de": "Beenden", "ru": "Выход", "pt": "Sair", "ar": "خروج",
    },
    "tray.tooltip": {
        "zh": "自动输入", "en": "AutoType",
        "ja": "自動入力", "ko": "AutoType", "es": "AutoType",
        "fr": "AutoType", "de": "AutoType", "ru": "AutoType",
        "pt": "AutoType", "ar": "أوتو تايب",
    },

    # ── Status bar ────────────────────────────────
    "status.preset": {
        "zh": "预设", "en": "Preset",
        "ja": "プリセット", "ko": "프리셋", "es": "Preset", "fr": "Préréglage",
        "de": "Voreinstellung", "ru": "Пресет", "pt": "Predefinição", "ar": "الإعداد المسبق",
    },

    # ── Hotkey hint labels ────────────────────────
    "hint.start": {
        "zh": "开始", "en": "Start",
        "ja": "開始", "ko": "시작", "es": "Iniciar", "fr": "Démarrer",
        "de": "Start", "ru": "Старт", "pt": "Iniciar", "ar": "بدء",
    },
    "hint.stop": {
        "zh": "停止", "en": "Stop",
        "ja": "停止", "ko": "중지", "es": "Detener", "fr": "Arrêter",
        "de": "Stopp", "ru": "Стоп", "pt": "Parar", "ar": "إيقاف",
    },
    "hint.toggle": {
        "zh": "切换", "en": "Toggle",
        "ja": "切替", "ko": "전환", "es": "Alternar", "fr": "Basculer",
        "de": "Umschalten", "ru": "Перекл.", "pt": "Alternar", "ar": "تبديل",
    },
}

_current_lang = "zh"


def set_language(lang: str) -> None:
    global _current_lang
    if lang in LANGUAGES:
        _current_lang = lang


def get_language() -> str:
    return _current_lang


def tr(key: str, **fmt) -> str:
    entry = TEXTS.get(key, {})
    text = entry.get(_current_lang) or entry.get("en") or key
    if fmt:
        text = text.format(**fmt)
    return text
