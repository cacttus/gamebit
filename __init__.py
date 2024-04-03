from krita import DockWidgetFactory, DockWidgetFactoryBase
from .gamebit import Gamebit
print('INITIZLISING INIT .PY GAMEBIT ')
Krita.instance().addDockWidgetFactory(DockWidgetFactory('gamebit', DockWidgetFactoryBase.DockRight, Gamebit))

#rom .extension_template import ExtensionTemplate
#Krita.instance().addExtension(ExtensionTemplate(Krita.instance()))