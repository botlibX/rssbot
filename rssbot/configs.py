# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0201


"configurations"


import os


from .default import Default


def __dir__():
    return (
        'Cfg',
        'Config'
    )


class Config(Default):

    pass


Cfg         = Config()
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wd      = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wd, f"{Cfg.name}.pid")
