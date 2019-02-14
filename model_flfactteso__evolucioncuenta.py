# @class_declaration interna_evolucioncuenta #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_evolucioncuenta(modelos.mtd_evolucioncuenta, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_evolucioncuenta #
class flfactteso_evolucioncuenta(interna_evolucioncuenta, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration evolucioncuenta #
class evolucioncuenta(flfactteso_evolucioncuenta, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.evolucioncuenta_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
