from distutils.core import setup  
import py2exe  
  
py2exe_options = {
    "py2exe": {
        "includes":["sip",],
        "compressed":1,
        "optimize":2,
        "bundle_files":1,
    }  
}
  
setup(windows=["main.py"], options=py2exe_options, zipfile=None)  
