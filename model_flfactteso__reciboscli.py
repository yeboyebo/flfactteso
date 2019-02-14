# @class_declaration interna_reciboscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_reciboscli(modelos.mtd_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_reciboscli #
class flfactteso_reciboscli(interna_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration reciboscli #
class reciboscli(flfactteso_reciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.reciboscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
