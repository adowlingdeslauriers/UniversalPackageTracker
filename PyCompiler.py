import sys

FILEPATH = sys.argv[1].replace("\\", "/")
import PyInstaller.__main__
PyInstaller.__main__.run([FILEPATH,"--onefile"])