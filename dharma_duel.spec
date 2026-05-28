# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Dharma Duel
Use this to create standalone executables

USAGE:
  pyinstaller dharma_duel.spec

This will create:
  - dist/DharmaDuel.exe (Windows)
  - dist/DharmaDuel.app (Mac)
  - dist/DharmaDuel (Linux)
"""

import platform

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data', 'data'),
        ('assets', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DharmaDuel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging, False for release
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you create one: icon='assets/icon.ico'
)

# Mac-specific app bundle
if platform.system() == 'Darwin':
    app = BUNDLE(
        exe,
        name='DharmaDuel.app',
        icon=None,
        bundle_identifier='com.dharmaduel.game',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSHighResolutionCapable': 'True',
        },
    )
