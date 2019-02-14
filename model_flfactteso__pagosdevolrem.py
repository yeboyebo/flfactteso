# @class_declaration interna_pagosdevolrem #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_pagosdevolrem(modelos.mtd_pagosdevolrem, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_pagosdevolrem #
class flfactteso_pagosdevolrem(interna_pagosdevolrem, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration pagosdevolrem #
class pagosdevolrem(flfactteso_pagosdevolrem, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.pagosdevolrem_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
