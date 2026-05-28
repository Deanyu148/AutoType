# AutoType

Un bel outil de saisie automatique multiplateforme. Simule la frappe au clavier dans n'importe quelle application, avec un mode réaliste caractère par caractère et un mode collage instantané depuis le presse-papiers.

## Fonctionnalités

- **Deux Modes de Saisie** — Saisie réaliste caractère par caractère (avec variation aléatoire du délai) ou collage instantané
- **Touches Spéciales** — Prend en charge Enter, Tab, Esc, touches fléchées, F1–F12 via des jetons spéciaux
- **Gestion de Préréglages** — Sauvegarder, charger, importer/exporter des préréglages (format YAML), jusqu'à 50
- **Raccourcis Globaux** — F6 pour démarrer, F7 pour arrêter, F8 pour basculer (fonctionne depuis n'importe quelle fenêtre)
- **Barre des Tâches** — Réduire dans la zone de notification avec menu d'accès rapide
- **10 Langues d'Interface** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **Toujours au Premier Plan** — Garder la fenêtre au-dessus des autres
- **Compte à Rebours** — Délai de démarrage configurable de 0–10 secondes
- **Vitesse Réglable** — 1–200 CPS (caractères par seconde)
- **Numéros de Ligne** — Éditeur avec numéros de ligne et compteurs caractères/mots/lignes

## Installation

### Exécuter depuis les Sources

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### Dépendances

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Framework Qt pour l'interface
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — Simulation de clavier + écouteur de raccourcis globaux
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — Mode instantané
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — Import/export de préréglages

### Compiler en EXE (Windows)

```bash
build.bat
```

## Utilisation

### Opération de Base

1. Saisissez ou collez le texte dans le panneau d'édition à gauche
2. Ajustez la vitesse, le délai et le mode à droite
3. Cliquez sur "Démarrer" ou appuyez sur F6
4. Placez le curseur dans le champ cible pendant le compte à rebours (3 sec par défaut)
5. Appuyez sur F7 pour arrêter à tout moment

### Jetons de Touches Spéciales

Utilisez la notation `{KEY}` pour insérer des touches spéciales :

| Jeton | Touche |
|---|---|
| `{ENTER}` | Entrée |
| `{TAB}` | Tab |
| `{ESC}` | Échap |
| `{SPACE}` | Espace |
| `{BACKSPACE}` | Retour arrière |
| `{DELETE}` | Supprimer |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | Flèches |
| `{HOME}` `{END}` | Début / Fin |
| `{PAGEUP}` `{PAGEDOWN}` | Page haut / bas |
| `{F1}` … `{F12}` | Touches de fonction |

Exemple :
```
utilisateur{ENTER}motdepasse{TAB}{ENTER}Bonjour le Monde, ceci est du texte auto-saisi.{ENTER}
```

### Modes de Saisie

- **Réaliste** — Envoie les frappes une par une via pynput avec variation aléatoire du délai. Imite la frappe humaine.
- **Instantané** — Utilise le presse-papiers + Ctrl+V pour tout coller en une fois. Le plus rapide.

### Raccourcis Globaux

| Touche | Action |
|---|---|
| F6 | Démarrer la saisie |
| F7 | Arrêter la saisie |
| F8 | Basculer (démarrer/arrêter) |

## Structure du Projet

```
AutoType/
├── main.py                     # Point d'entrée
├── build.bat                   # Script de build PyInstaller
├── AutoType.ico                # Icône de l'application
├── requirements.txt            # Dépendances
├── README.md                   # README en chinois
├── docs/                       # READMEs dans d'autres langues
└── src/
    ├── core/
    │   ├── autotyper.py        # Moteur de saisie (thread)
    │   └── key_simulator.py    # Simulation de clavier
    ├── ui/
    │   ├── main_window.py      # Fenêtre principale
    │   ├── editor_panel.py     # Panneau d'édition de texte
    │   ├── settings_panel.py   # Panneau de paramètres
    │   ├── preset_manager.py   # Gestion des préréglages
    │   ├── widgets.py          # Widgets personnalisés
    │   └── theme.py            # Définitions du thème
    └── utils/
        ├── config.py           # Persistance de la configuration (JSON)
        └── i18n.py             # Internationalisation
```

## Stack Technique

- **GUI** : PySide6 (Qt pour Python)
- **Simulation de Clavier** : pynput / pyautogui
- **Stockage de Configuration** : JSON / YAML
- **Build** : PyInstaller (EXE fichier unique)

## Licence

MIT License

## Auteur

Deanyu148
