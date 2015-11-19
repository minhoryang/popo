__author__ = "minhoryang@gmail.com"
from importlib import import_module


class POPO(object):
    class TYPE(object):
        parent = None
        docstring = None
    class TYPE_INT(TYPE):  pass
    class TYPE_STRING(TYPE):  pass
    class TYPE_CLASS(TYPE):
        childs = {}  # XXX : sort by name
    class TYPE_ENUM(TYPE):
        pass  # TODO

    def __init__(self, module_name):
        self._module_name = module_name
        self._module = import_module(self._module_name)
        self._classes = self._stage1_get_classes()
        self._stage2_()

    def _stage1_get_classes(self):  # TODO: recursively
        classes = {}
        for name, cls in self._module.__dict__.items():
            if not '__' in name and self._module_name in cls.__module__:
                    classes[name] = cls
        return classes

    def _stage2_(self):
        head = []
        for name, cls in self._classes.items():
            now = self.TYPE_CLASS()
            now.name = name
            now.docstring = cls.__doc__
            head.append(now)


if __name__ == "__main__":
    POPO("examples2.test")
