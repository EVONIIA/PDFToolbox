# -*- mode: python ; coding: utf-8 -*-
r"""Spécification PyInstaller pour PDF Toolbox by EVONIIA.

Deux constructions, depuis la racine du projet :

    $env:PDFTOOLBOX_BUILD = "onedir"
    .\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean pdf_toolbox.spec

    $env:PDFTOOLBOX_BUILD = "onefile"
    .\.venv\Scripts\python.exe -m PyInstaller --noconfirm pdf_toolbox.spec

onedir produit dist/PDFToolbox/PDFToolbox.exe.
onefile produit dist/PDFToolbox.exe.

pdfium.dll et version.json restent dans pypdfium2_raw : pypdfium2 les
charge à côté de son paquet, pas à la racine de l'exécutable.
"""

import os
import sys
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

project_root = Path(SPECPATH)
mode = os.environ.get("PDFTOOLBOX_BUILD", "onedir").strip().lower()
if mode not in {"onedir", "onefile"}:
    raise SystemExit("PDFTOOLBOX_BUILD doit valoir onedir ou onefile.")

icon = project_root / "assets" / "brand" / "app.ico"
version_file = project_root / "packaging" / "windows_version_info.txt"
if not version_file.is_file():
    raise SystemExit(f"Métadonnées Windows introuvables : {version_file}")

datas = [(str(project_root / "assets"), "assets")]
binaries = []
hiddenimports = [
    "pypdf",
    "pypdf.generic",
    "pypdfium2",
    "pypdfium2_raw",
    "PIL",
    "PIL.Image",
    "PIL.ImageOps",
    "PIL._tkinter_finder",
    "tkinterdnd2",
]

datas += collect_data_files("customtkinter")
datas += collect_data_files("pypdfium2")
datas += collect_data_files("pypdfium2_raw")
binaries += collect_dynamic_libs("pypdfium2_raw")

import pypdfium2_raw

raw_dir = Path(pypdfium2_raw.__file__).resolve().parent
pdfium = list(raw_dir.glob("pdfium.*"))
if not pdfium:
    raise SystemExit(f"pdfium introuvable dans {raw_dir}")
if not (raw_dir / "version.json").is_file():
    raise SystemExit(f"version.json introuvable dans {raw_dir}")
for library in pdfium:
    binaries.append((str(library), "pypdfium2_raw"))

import tkinterdnd2

tkdnd = Path(tkinterdnd2.__file__).resolve().parent / "tkdnd"
if not tkdnd.is_dir():
    raise SystemExit(f"Bibliothèque tkdnd introuvable : {tkdnd}")
datas.append((str(tkdnd), "tkinterdnd2/tkdnd"))

a = Analysis(
    [str(project_root / "main.py")],
    pathex=[str(project_root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe_options = {
    "name": "PDFToolbox",
    "debug": False,
    "bootloader_ignore_signals": False,
    "strip": False,
    "upx": False,
    "console": False,
    "disable_windowed_traceback": True,
    "argv_emulation": False,
    "version": str(version_file),
}
if icon.is_file():
    exe_options["icon"] = str(icon)
else:
    print("Aucune icône assets/brand/app.ico : l'icône Windows par défaut est conservée.", file=sys.stderr)

if mode == "onefile":
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        exclude_binaries=False,
        **exe_options,
    )
else:
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        **exe_options,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=False,
        upx_exclude=[],
        name="PDFToolbox",
    )
