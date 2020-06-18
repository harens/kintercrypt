# -*- mode: python -*-
import os

# Allows for a relative path
spec_root = os.path.abspath(SPECPATH)

block_cipher = None


a = Analysis(['kintercrypt/main_gui.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='kintercrypt',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='kintercrypt.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': 'True'
              })