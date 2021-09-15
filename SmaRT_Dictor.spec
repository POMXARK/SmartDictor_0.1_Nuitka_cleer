# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
excluded_modules = ['torch.distributions'] # add this

a = Analysis(['SmaRT_Dictor.py'],
             pathex=['C:\\Users\\User\\PycharmProjects\\Corsairs_2_kivy'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'], # add this
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=excluded_modules,# add this
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

for d in a.datas:
    if '_C.cp39-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break

exe = EXE(pyz,Tree('C:\\Users\\User\\PycharmProjects\\Corsairs_2_kivy_app\\RESOURCE'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SmaRT_Dictor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )


