# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0401,E0402


"""feed fetcher


rssbot <cmd> [key=val] [key==val] [mod=n1,n2]
rssbot [-c] [-d] [-h] [-v]

commands:

cfg - irc configuration
cmd - commands
dpl - items of feed to display
mod - show available modules
mre - show cached output
pwd - create sasl password
rem - remove feed
rss - add feed

options:

-c     start console
-d     start daemon
-h     display help
-v     use verbose"""


from .defines import *
from .defines import __dir__
