# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['DatabaseOrganization_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Commercial_Tool',
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
	icon='icon.ico'
)
