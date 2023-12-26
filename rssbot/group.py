# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E1101,W0718,W0612,E0611


"list of bots"


from .object import Object


def __dir__():
    return (
            'Group',
            'byorig'
           )


__all__ = __dir__()


class Group(Object):

    objs = []    

    @staticmethod
    def add(obj) -> None:
        Group.objs.append(obj)

    @staticmethod
    def byorig(orig) -> Object:
        for obj in Group.objs:
            if object.__repr__(obj) == orig:
                return obj
        return None

    @staticmethod
    def first():
        if Group.objs:
            return Group.objs[0]

    @staticmethod
    def remove(obj):
        if obj in Group.objs:
            Group.objs.remove(obj)


def byorig(orig):
    return Group.byorig(orig)
