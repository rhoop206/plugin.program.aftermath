import xbmc
import xbmcaddon

import os
from datetime import date
from datetime import timedelta

import uservar

KODIV = float(xbmc.getInfoLabel("System.BuildVersion")[:4])

HOME = xbmc.translatePath('special://home/')

ADDON_ID = uservar.ADDON_ID
ADDONTITLE = uservar.ADDONTITLE
ADDON = xbmcaddon.Addon(ADDON_ID)
ADDONPATH = ADDON.getAddonInfo('path')
VERSION = ADDON.getAddonInfo('version')

ADDONS = os.path.join(HOME, 'addons')
USERDATA = os.path.join(HOME, 'userdata')
ADDONDATA = os.path.join(USERDATA, 'addon_data', ADDON_ID)
WIZLOG = os.path.join(ADDONDATA, 'wizard.log')
PLUGIN = os.path.join(ADDONS, ADDON_ID)
PACKAGES = os.path.join(ADDONS, 'packages')
ICON = os.path.join(PLUGIN, 'icon.png')
FANART = os.path.join(PLUGIN, 'fanart.jpg')
ART = os.path.join(PLUGIN, 'resources', 'art')
SKINFOLD = os.path.join(ADDONPATH,   'resources', 'skins', 'DefaultSkin', 'media')
ADVANCED = os.path.join(USERDATA,  'advancedsettings.xml')
GUISETTINGS = os.path.join(USERDATA,  'guisettings.xml')

UPDATECHECK = uservar.UPDATECHECK if str(uservar.UPDATECHECK).isdigit() else 1
NOTIFICATION = uservar.NOTIFICATION
ENABLE = uservar.ENABLE
HEADERTYPE = uservar.HEADERTYPE if uservar.HEADERTYPE == 'Image' else 'Text'
HEADERMESSAGE = uservar.HEADERMESSAGE
BACKGROUND = uservar.BACKGROUND
HEADERIMAGE = uservar.HEADERIMAGE
COLOR1 = uservar.COLOR1
COLOR2 = uservar.COLOR2
THEME1 = uservar.THEME1
THEME2 = uservar.THEME2
THEME3 = uservar.THEME3
THEME4 = uservar.THEME4
THEME5 = uservar.THEME5
CONTACTICON = uservar.CONTACTICON if not uservar.CONTACTICON == 'http://' else ICON
CONTACTFANART = uservar.CONTACTFANART if not uservar.CONTACTFANART == 'http://' else FANART

TODAY = date.today()
TOMORROW = TODAY + timedelta(days=1)
THREEDAYS = TODAY + timedelta(days=3)
NEXTCHECK = TODAY + timedelta(days=UPDATECHECK)
MAXWIZSIZE = [100, 200, 300, 400, 500, 1000]
MAXWIZLINES = [100, 200, 300, 400, 500]
MAXWIZDATES = [1, 2, 3, 7]

NEXTCLEANDATE = ADDON.getSetting('nextcleandate')
WIZDEBUGGING = ADDON.getSetting('addon_debug')
DEBUGLEVEL = ADDON.getSetting('debuglevel')
ENABLEWIZLOG = ADDON.getSetting('wizardlog')
CLEANWIZLOG = ADDON.getSetting('autocleanwiz')
CLEANWIZLOGBY = ADDON.getSetting('wizlogcleanby')
CLEANDAYS = ADDON.getSetting('wizlogcleandays')
CLEANSIZE = ADDON.getSetting('wizlogcleansize')
CLEANLINES = ADDON.getSetting('wizlogcleanlines')
KEEPFAVS = ADDON.getSetting('keepfavourites')
KEEPSOURCES = ADDON.getSetting('keepsources')
KEEPPROFILES = ADDON.getSetting('keepprofiles')
KEEPADVANCED = ADDON.getSetting('keepadvanced')
KEEPSUPER = ADDON.getSetting('keepsuper')
KEEPREPOS = ADDON.getSetting('keeprepos')
KEEPWHITELIST = ADDON.getSetting('keepwhitelist')
NOTIFY = ADDON.getSetting('notify')
NOTEID = ADDON.getSetting('noteid')
NOTEDISMISS = ADDON.getSetting('notedismiss')
BUILDNAME = ADDON.getSetting('buildname')
BUILDVERSION = ADDON.getSetting('buildversion')