import types


class Prototype:
    class __metaclass__(type):
        def __new__(self, name, bases, dict):
            for member, value in dict.items():
                if type(value) == types.FunctionType:
                    dict[member] = classmethod(value)
            return type.__new__(self, name, bases, dict)

    __new__ = NotImplemented
