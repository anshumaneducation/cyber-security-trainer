# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cryptography-start.py'],
    pathex=[],
    binaries=[],
    datas=[('client.py', '.'), ('server.py', '.'), ('hacker.py', '.'), ('password_verifier.py', '.'), ('digital-signer.py', '.'), ('digital-verifier.py', '.'), ('DSAkeys.txt', '.'), ('key.txt', '.'), ('private_key.pem', '.'), ('public_key.pem', '.'), ('RC4.py', '.'), ('RSA.py', '.'), ('SaveKeys.py', '.'), ('sDES.py', '.'), ('signature.txt', '.'), ('TDES.py', '.'), ('verification.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='cryptography-start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
