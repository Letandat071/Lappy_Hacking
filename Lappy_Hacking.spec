# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
import sys
from PyInstaller.utils.hooks import collect_data_files

# Sử dụng đường dẫn tuyệt đối
base_path = os.path.abspath(os.getcwd())

a = Analysis(
    ['main.py'],
    pathex=[base_path],
    binaries=[],
    datas=[
        ('public/image/*.jpg', 'public/image'),
        ('public/image/*.png', 'public/image'),
    ],
    hiddenimports=['PIL', 'PIL._imagingtk', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=True,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Lappy_Ver2.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=False,
    icon='public/image/icon.jpg',
    manifest='manifest.xml'
) 