# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0212


"runtime"


import inspect


from .command import Command
from .event   import Event
from .object  import Object, spl
from .storage import Storage
from .thread  import launch


def __dir__():
    return (
        'cmnd',
        'scan'
    )


__all__ = __dir__()


def cmnd(txt):
    evn = Event()
    evn.txt = txt
    Command.handle(evn)
    evn.wait()
    return evn


def scan(pkg, modstr, initer=False) -> []:
    mods = []
    for modname in spl(modstr):
        module = getattr(pkg, modname, None)
        if not module:
            continue
        for key, cmd in inspect.getmembers(module, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Command.add(cmd)
        for key, clz in inspect.getmembers(module, inspect.isclass):
            if key.startswith("cb"):
                continue
            if not issubclass(clz, Object):
                continue
            Storage.add(clz)
        if initer and "init" in dir(module):
            module._thr = launch(module.init, name=f"init {modname}")
        mods.append(module)
    return mods
