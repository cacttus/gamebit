
import sys
import os
import subprocess
import platform

#https://krita-artists.org/t/cannot-reload-python-plugin-script-i-am-developing-without-restarting-krita/36420
#https://krita-artists.org/t/python-plugins-reload/5448/2

_MODULE_NAME='gamebit'
_REPOSITORY='~/git/'
_PLUGINDIR='' #leave blank for default

def reload_krita_scripter(module_name, repo, plugin_dir):
  if plugin_dir == "":
    platss = platform.system()
    print(f"platform.system()={platss}")
    if platss == 'Windows':
      plugin_dir = '%APPDATA%\krita\pykrita'
    elif platss == 'Linux':
      plugin_dir = '~/.local/share/krita/pykrita'
    elif platss == 'MacOS':
      plugin_dir = '~/Library/Application Support/Krita/pykrita'
    else:
      raise Exception(f"Unrecognized Platform {platss}")
      
  def import_package():    
    #from gamebit import Gamebit
    __import__(module_name)        
  
  #copy files
  try:
    cmd = f"cp -R {repo}{module_name}/{module_name} {plugin_dir} && cp {repo}{module_name}/{module_name}.desktop {plugin_dir}/{module_name}.desktop"
    pr = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
    pr.wait()
    print("copied files")
  except Exception as e:
    print(f"Failed to copy files: {e}")
    raise e
  
  #print(f"Loaded extendsions:{Krita.extensions()}")
  #all_items = dd.findItems('', QtCore.Qt.MatchRegExp)
  #print(f"Loaded esdf:{dd} count = {dd.count(dd)}")
  #ddd = dd.index( a.objectName())
  
  #Works
  #dd=Krita.dockers()
  #ddd=[i for i, e in enumerate(dd) if e.objectName()=='gamebit']
  #dd[ddd[0]].close() #this will also remove it

  #print(f"ddd={ddd}")
  #for d in dd:
  #  print(f"Docker: {d.objectName()}")

  # for d in Application.activeWindow().dockers():
  #   print(f"Docker: {d.getWindowTitle()}")
  # for d in Krita.instance().dockers():
  #   print(f"Docker: {d.getWindowTitle()}")
  # for w in Krita.instance().windows():
  #   print(f"W: {w.getWindowTitle()}")

  try:
    QtCore.qDebug("RELOADING EXTENSION FROM KRITA_MENU")
    import_package()
    PLUGIN_EXEC_FROM = 'KRITA_MENU'
  except:

    modpath=f"{plugin_dir}/{module_name}"
  
    if not modpath in sys.path.copy():
      print(f"Adding system path: {modpath}")
      sys.path.append(modpath)
    #print(f"path={sys.path.copy()}")

    if module_name in sys.modules:
      from importlib import reload
      print("Reload pyKritaLib")
      reload(sys.modules[module_name])
    else:
      print(f"Import {module_name}")
      __import__(module_name)

    from gamebit import Gamebit
    PLUGIN_EXEC_FROM = 'SCRIPTER_PLUGIN'    
    
    Krita.instance().addExtension(Gamebit(Krita.instance()))
  print('done.')

reload_krita_scripter(module_name=_MODULE_NAME, repo=_REPOSITORY, plugin_dir=_PLUGINDIR)