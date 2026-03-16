# ProjetT5200 – Arts numériques rétro

**Projet artistique et technique explorant l’adaptation de contenus modernes sur un PC vintage Toshiba T5200.**

---

## 🎨 Objectif du projet

Le ProjetT5200 vise à **recréer une expérience numérique rétro** en adaptant des médias modernes pour du matériel ancien :

1. **Images**  
   - Conversion d’images modernes en **16 niveaux ambre** pour l’écran monochrome du T5200.  
   - Scripts Python permettant d’appliquer des filtres, ajuster le contraste et quantifier les couleurs.

2. **Musique / MIDI**  
   - Adaptation de fichiers MIDI modernes pour la **Sound Blaster 16 OPL3**.  
   - Scripts Python qui limitent la polyphonie, remappent les instruments modernes vers des équivalents OPL3 et respectent la contrainte des 16 canaux.

---

## 📂 Structure du projet
```text
ProjetT5200/
├── .venv/                      # Environnement virtuel Python
├── images/                     # Tout ce qui concerne les images
│   ├── Economiseur d'écran/    # Exemples de screensavers rétro
│   ├── Exemples/               # Images de test
│   └── traitement.py           # Script de traitement images
├── midi_project/               # Tout ce qui concerne la musique / MIDI
│   ├── exemples/               # Fichiers MIDI originaux et convertis
│   ├── midi_to_OPL3.py         # Script principal MIDI
│   └── utils.py                # Mapping instruments et fonctions auxiliaires
├── README.md                   # Présentation globale du projet
└── LICENSE                     # Licence (optionnel)