import xbmc
import xbmcgui

import os
from datetime import datetime, timedelta

from resources.libs import vars


def log_notify(title, message, times=2000, icon=vars.ICON, sound=False):
    xbmcgui.Dialog().notification(title, message, icon, int(times), sound)


def log(msg, level=xbmc.LOGDEBUG):
    if not os.path.exists(vars.ADDONDATA):
        os.makedirs(vars.ADDONDATA)
    if not os.path.exists(vars.WIZLOG):
        f = open(vars.WIZLOG, 'w')
        f.close()
    if vars.WIZDEBUGGING == 'false':
        return False
    if vars.DEBUGLEVEL == '0':
        return False
    if vars.DEBUGLEVEL == '1' and level not in [xbmc.LOGNOTICE, xbmc.LOGERROR, xbmc.LOGSEVERE, xbmc.LOGFATAL]:
        return False
    if vars.DEBUGLEVEL == '2':
        level = xbmc.LOGNOTICE
    try:
        xbmc.log('{0}: {1}'.format(vars.ADDONTITLE, msg), level)
    except Exception as e:
        try:
            xbmc.log('Logging Failure: {0}'.format(e), level)
        except:
            pass
    if vars.ENABLEWIZLOG == 'true':
        lastcheck = vars.NEXTCLEANDATE if not vars.NEXTCLEANDATE == '' else str(vars.TODAY)
        if vars.CLEANWIZLOG == 'true' and lastcheck <= str(vars.TODAY):

            check_log()
        with open(vars.WIZLOG, 'a') as f:
            line = "[{0} {1}] {2}".format(datetime.now().date(), str(datetime.now().time())[:8], msg)
            f.write(line.rstrip('\r\n')+'\n')


def check_log():
    if vars.CLEANWIZLOGBY == '0':
        keep = vars.TODAY - timedelta(days=vars.MAXWIZDATES[int(float(vars.CLEANDAYS))])
        x = 0

        f = open(vars.WIZLOG)
        a = f.read()
        f.close()
        lines = a.split('\n')

        for line in lines:
            if str(line[1:11]) >= str(keep):
                break
            x += 1

        newfile = lines[x:]
        writing = '\n'.join(newfile)
        f = open(vars.WIZLOG, 'w')
        f.write(writing)
        f.close()
    elif vars.CLEANWIZLOGBY == '1':
        maxsize = vars.MAXWIZSIZE[int(float(vars.CLEANSIZE))]*1024

        f = open(vars.WIZLOG)
        a = f.read()
        f.close()
        lines = a.split('\n')

        if os.path.getsize(vars.WIZLOG) >= maxsize:
            start = len(lines)/2
            newfile = lines[start:]
            writing = '\n'.join(newfile)
            f = open(vars.WIZLOG, 'w')
            f.write(writing)
            f.close()
    elif vars.CLEANWIZLOGBY == '2':
        f = open(vars.WIZLOG)
        a = f.read()
        f.close()
        lines = a.split('\n')

        maxlines = vars.MAXWIZLINES[int(float(vars.CLEANLINES))]
        if len(lines) > maxlines:
            start = len(lines) - int(maxlines/2)
            newfile = lines[start:]
            writing = '\n'.join(newfile)
            f = open(vars.WIZLOG, 'w')
            f.write(writing)
            f.close()
    vars.ADDON.setSetting('nextcleandate', str(next))


def convert_size(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G']:
        if abs(num) < 1024.0:
            return "%3.02f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.02f %s%s" % (num, 'G', suffix)


def percentage(part, whole):
    return 100 * float(part)/float(whole)
