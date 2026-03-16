# ProjetT5200 – Arts numériques rétro

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Projet artistique et technique explorant l’adaptation de contenus modernes sur un PC vintage Toshiba T5200.**

---

## 📖 Sommaire

- [🎨 Objectif du projet](#-objectif-du-projet)  
- [📂 Structure du projet](#-structure-du-projet)  
- [⚙️ Installation et dépendances](#-installation-et-dépendances)  
- [🖼️ Utilisation – Images](#-utilisation--images)  
- [🎵 Utilisation – MIDI](#-utilisation--midi)  
- [💡 Notes artistiques](#-notes-artistiques)  
- [📜 Licence](#-licence)

---

## 🎨 Objectif du projet

Le ProjetT5200 vise à **recréer une expérience numérique rétro** en adaptant des médias modernes pour du matériel ancien.  

<details>
<summary>Images</summary>

- Conversion d’images modernes en **16 niveaux ambre** pour l’écran monochrome du T5200.  
- Scripts Python permettant d’appliquer des filtres, ajuster le contraste et quantifier les couleurs.

</details>

<details>
<summary>Musique / MIDI</summary>

- Adaptation de fichiers MIDI modernes pour la **Sound Blaster 16 OPL3**.  
- Scripts Python qui limitent la polyphonie, remappent les instruments modernes vers des équivalents OPL3 et respectent la contrainte des 16 canaux.

</details>

---

## 📂 Structure du projet

```text
ProjetT5200/
├── .venv/                     # Environnement virtuel Python
├── images/                     # Tout ce qui concerne les images
│   ├── Economiseur d'écran/    # Screensavers rétro
│   ├── Exemples/               # Images de test
│   └── traitement.py           # Script de traitement images
├── midi_project/               # Tout ce qui concerne la musique / MIDI
│   ├── exemples/               # Fichiers MIDI originaux et convertis
│   ├── midi_to_OPL3.py         # Script principal MIDI
│   └── utils.py                # Mapping instruments et fonctions auxiliaires
├── .gitignore                  # Fichiers à ignorer
├── README.md                   # Ce fichier
└── LICENSE                     # Licence (optionnel)