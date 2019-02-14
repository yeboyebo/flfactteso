# @class_declaration interna_mandatoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactteso import models as modelos


class interna_mandatoscli(modelos.mtd_mandatoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfactteso_mandatoscli #
class flfactteso_mandatoscli(interna_mandatoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration mandatoscli #
class mandatoscli(flfactteso_mandatoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactteso.mandatoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
