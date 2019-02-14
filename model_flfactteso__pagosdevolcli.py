# @class_declaration interna_pagosdevolcli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_pagosdevolcli(modelos.mtd_pagosdevolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_pagosdevolcli #
class flfactteso_pagosdevolcli(interna_pagosdevolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration pagosdevolcli #
class pagosdevolcli(flfactteso_pagosdevolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.pagosdevolcli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
