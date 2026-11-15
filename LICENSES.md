# Licences des composants tiers

PDF Toolbox by EVONIIA est un logiciel propriétaire d'EVONIIA. Ses conditions figurent dans le fichier `LICENSE`. La publication éventuelle du dépôt en accès public ne transfère pas ces composants à EVONIIA et ne change pas leur licence.

Ce fichier ne décrit que les bibliothèques tierces livrées ou utilisées avec l'application. Ces composants n'appartiennent pas à EVONIIA. Chacun reste soumis à la licence de son titulaire. Aucune de ces licences n'est présentée comme une cession de droits à EVONIIA.

PyMuPDF n'est pas utilisé. Les miniatures passent par pypdfium2.

Les versions ci-dessous sont celles installées pour la candidate 1.0.0. Elles correspondent aux bornes de `requirements.txt`.

| Composant | Version | Licence | Rôle |
|---|---|---|---|
| Python | 3.11 ou plus récent | PSF License | Interpréteur. PyInstaller en embarque une copie dans l’exécutable. |
| customtkinter | 6.0.0 | CC0-1.0 | Interface. |
| pypdf | 7.0.1 | BSD-3-Clause | Lecture, fusion, découpe, extraction et réorganisation des PDF. |
| pypdfium2 | 5.15.2 | BSD-3-Clause et Apache-2.0 | Miniatures, via PDFium. Les licences de construction de PDFium sont livrées avec le paquet. |
| Pillow | 13.0.0 | MIT-CMU | Images JPG et PNG, et préparation des logos. |
| tkinterdnd2 | 0.7.0 | MIT | Glisser-déposer. La bibliothèque tkdnd est incluse dans le paquet. |
| PyInstaller | 6.22.3 | GPL-2.0-or-later, avec exception | Outil de compilation uniquement. L’exception autorise à distribuer un programme propriétaire empaqueté sans placer PDF Toolbox sous GPL. |
| darkdetect | 0.8.0 | BSD-3-Clause | Dépendance de customtkinter, pour détecter le thème de Windows. Non utilisé directement par le code d'EVONIIA. |

Tkinter fait partie de la bibliothèque standard de Python et reste soumis à la licence PSF.

Les licences de construction de PDFium, livrées dans le paquet pypdfium2, concernent PDFium et ses composants. Elles ne transfèrent pas ces composants à EVONIIA.

PyInstaller n’est pas nécessaire pour utiliser l’application déjà compilée. Il sert seulement à produire `dist\PDFToolbox` et `dist\PDFToolbox.exe`.

Les préférences de l’utilisateur restent dans `%APPDATA%\EVONIIA\PDF Toolbox\settings.json`. Elles ne sont pas placées dans le dossier temporaire d’extraction de PyInstaller.
