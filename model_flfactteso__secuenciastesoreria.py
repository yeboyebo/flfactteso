# @class_declaration interna_secuenciastesoreria #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_secuenciastesoreria(modelos.mtd_secuenciastesoreria, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_secuenciastesoreria #
class flfactteso_secuenciastesoreria(interna_secuenciastesoreria, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration secuenciastesoreria #
class secuenciastesoreria(flfactteso_secuenciastesoreria, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.secuenciastesoreria_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
