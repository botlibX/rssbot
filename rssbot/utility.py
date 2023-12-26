# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"utilities"


import os
import pathlib
import time
import types
import _thread


def __dir__():
    return (
        'cdir',
        'fntime',
        'forever',
        'laps',
        'name',
        'spl',
        'strip'
    )


__all__ = __dir__()


def cdir(pth) -> None:
    pth = pathlib.Path(pth)
    os.makedirs(pth, exist_ok=True)


def fntime(daystr) -> float:
    daystr = daystr.replace('_', ':')
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    return timed


def forever():
    while 1:
        try:
            time.sleep(1.0)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def laps(seconds, short=True) -> str:
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def name(obj) -> str:
    typ = type(obj)
    if isinstance(typ, types.ModuleType):
        return obj.__name__
    if '__self__' in dir(obj):
        return f'{obj.__self__.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj) and '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj):
        return f"{obj.__class__.__module__}.{obj.__class__.__name__}"
    if '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    return None


def spl(txt) -> []:
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def strip(pth, nmr=3) -> str:
    return os.sep.join(pth.split(os.sep)[-nmr:])
