from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['E:\\1projects\\Python\\time_'],
    binaries=[],
    datas=[],
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

exe = EXE(pyz,
    Tree('E:\\1projects\\Python\\time_\\'),
  a.scripts,
  a.binaries,
  a.zipfiles,
  a.datas,
  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins )],
  name='TimeMachine',
  debug=False,
  strip=False,
  upx=True,
  console=False,
  icon='TimeMachine.ico')


coll = COLLECT(exe,
           Tree('E:\\1projects\\Python\\time_\\'),
           a.binaries,
           a.zipfiles,
           a.datas,
           *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
           strip=False,
           upx=True,
           name='TimeMachine')


