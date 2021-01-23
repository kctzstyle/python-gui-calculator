
from cx_Freeze import setup, Executable


build_options = {
    'packages': ['calculate', 'app', 'tkinter'],
}
exe = [Executable('main.py')]

setup(
    name='GUI-Calculator',
    version='1.0.0',
    author='kctzstyle',
    description='Python GUI Calculator',
    options={'build_exe': build_options},
    executables=exe
)
