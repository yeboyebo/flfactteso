# @class_declaration interna_factteso_general #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_factteso_general(modelos.mtd_factteso_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_factteso_general #
class flfactteso_factteso_general(interna_factteso_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration factteso_general #
class factteso_general(flfactteso_factteso_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.factteso_general_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
