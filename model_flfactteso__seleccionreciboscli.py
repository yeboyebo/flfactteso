# @class_declaration interna_seleccionreciboscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_seleccionreciboscli(modelos.mtd_seleccionreciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_seleccionreciboscli #
class flfactteso_seleccionreciboscli(interna_seleccionreciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration seleccionreciboscli #
class seleccionreciboscli(flfactteso_seleccionreciboscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.seleccionreciboscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
