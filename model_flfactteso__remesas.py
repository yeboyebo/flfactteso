# @class_declaration interna_remesas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_remesas(modelos.mtd_remesas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_remesas #
class flfactteso_remesas(interna_remesas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration remesas #
class remesas(flfactteso_remesas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.remesas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
