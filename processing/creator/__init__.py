import copy

from processing.creator.excel import Excel


class Layout(Excel):
    def addStyleAttribute(self, objstyle, attributes):
        s = copy.deepcopy(getattr(self, objstyle))
        for attribut, valeur in attributes.items():
            setattr(s, attribut, valeur)
        return s