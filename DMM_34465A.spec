# -*- mode: python ; coding: utf-8 -*-
# Keysight 34465A multiméter vezérlő – PyInstaller spec
# Build: python -m PyInstaller DMM_34465A.spec --noconfirm
# Eredmény: dist\DMM_34465A.exe

a = Analysis(
    ['dmm_34465a.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tkinter', 'tkinter.ttk', 'tkinter.messagebox'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'pandas', 'matplotlib', 'scipy', 'serial',
              'uvicorn', 'fastapi', 'pyvisa'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DMM_34465A',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
