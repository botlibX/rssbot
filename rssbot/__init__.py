# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,E0402



"""original programmer (op)


op <cmd> [key=val] [key==val] [mod=n1,n2]
op [-a] [-c] [-d] [-h] [-v] [-w]

commands:

cfg - irc configuration
cmd - commands
mod - show available modules
now - show genocide stats
req - reconsider
wsd - show wisdom

options:

-a     load all modules
-c     start console
-d     start daemon
-h     display help
-v     use verbose
-w     wait for services"""


from .defines import *
from .defines import __dir__
