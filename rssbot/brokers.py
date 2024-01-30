# This file is placed in the Public Domain.
#
# pylint: disable=C,R, E0402


"list of bots"


from .objects import Object, items, keys


def __dir__():
    return (
        "Broker",
    )


__all__ = __dir__()


rpr = object.__repr__


class Broker(Object):

    objs = Object()

    @staticmethod
    def add(obj):
        setattr(Broker.objs, rpr(obj), obj)

    @staticmethod
    def all():
        return items(Broker.objs)

    @staticmethod
    def first():
        for key in keys(Broker.objs):
            return getattr(Broker.objs, key)

    @staticmethod
    def remove(obj):
        delattr(Broker.objs, rpr(obj))

    @staticmethod
    def byorig(orig):
        return getattr(Broker.objs, orig, None)

