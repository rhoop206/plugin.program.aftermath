################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import xbmc
import xbmcgui

import os
import re

import time
from datetime import date, timedelta

import uservar
from resources.libs import wizard

ADDON_ID       = uservar.ADDON_ID
ADDONTITLE     = uservar.ADDONTITLE
ADDON          = wizard.addonId(ADDON_ID)
DIALOG         = xbmcgui.Dialog()
HOME           = xbmc.translatePath('special://home/')
ADDONS         = os.path.join(HOME,      'addons')
USERDATA       = os.path.join(HOME,      'userdata')
PLUGIN         = os.path.join(ADDONS,    ADDON_ID)
PACKAGES       = os.path.join(ADDONS,    'packages')
ADDONDATA      = os.path.join(USERDATA,  'addon_data', ADDON_ID)
ADDOND         = os.path.join(USERDATA,  'addon_data')
TRAKTFOLD      = os.path.join(ADDONDATA, 'trakt')
ICON           = os.path.join(PLUGIN,    'icon.png')
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
THREEDAYS      = TODAY + timedelta(days=3)
KEEPTRAKT      = wizard.getS('keeptrakt')
TRAKTSAVE      = wizard.getS('traktlastsave')
COLOR1         = uservar.COLOR1
COLOR2         = uservar.COLOR2
ORDER          = ['exodusredux', 'gaia', 'openmeta', 'overeasy', 'placenta', 'premiumizer', 'realizer', 'scrubs', 'seren', 'trakt', 'yoda']

TRAKTID = {
    'placenta': {
        'name'     : 'Placenta',
        'plugin'   : 'plugin.video.placenta',
        'saved'    : 'placenta',
        'path'     : os.path.join(ADDONS, 'plugin.video.placenta'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.placenta', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.placenta', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'placenta_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.placenta', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.user', 'trakt.refresh', 'trakt.token'],
        'activate' : 'RunPlugin(plugin://plugin.video.placenta/?action=authTrakt)'},
    'gaia': {
        'name'     : 'Gaia',
        'plugin'   : 'plugin.video.gaia',
        'saved'    : 'gaia',
        'path'     : os.path.join(ADDONS, 'plugin.video.gaia'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.gaia', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.gaia', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'gaia_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.gaia', 'settings.xml'),
        'default'  : 'accounts.informants.trakt.user',
        'data'     : ['accounts.informants.trakt.user', 'accounts.informants.trakt.refresh', 'accounts.informants.trakt.token'],
        'activate' : 'RunPlugin(plugin://plugin.video.gaia/?action=traktAuthorize)'},
    'overeasy': {
        'name'     : 'Overeasy',
        'plugin'   : 'plugin.video.overeasy',
        'saved'    : 'overeasy',
        'path'     : os.path.join(ADDONS, 'plugin.video.overeasy'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.overeasy', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.overeasy', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'overeasy_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.overeasy', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.refresh', 'trakt.token', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.overeasy/?action=authTrakt)'},
    'seren': {
        'name'     : 'Seren',
        'plugin'   : 'plugin.video.seren',
        'saved'    : 'seren',
        'path'     : os.path.join(ADDONS, 'plugin.video.seren'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.seren', 'temp-icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.seren', 'temp-fanart.png'),
        'file'     : os.path.join(TRAKTFOLD, 'seren_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.seren', 'settings.xml'),
        'default'  : 'trakt.username',
        'data'     : ['trakt.auth', 'trakt.refresh', 'trakt.username'],
        'activate' : 'RunPlugin(plugin://plugin.video.seren/?action=authTrakt)'},
    'trakt': {
        'name'     : 'Trakt',
        'plugin'   : 'script.trakt',
        'saved'    : 'trakt',
        'path'     : os.path.join(ADDONS, 'script.trakt'),
        'icon'     : os.path.join(ADDONS, 'script.trakt', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'script.trakt', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'trakt_trakt'),
        'settings' : os.path.join(ADDOND, 'script.trakt', 'settings.xml'),
        'default'  : 'user',
        'data'     : ['authorization', 'user'],
        'activate' : 'RunScript(script.trakt, action=auth_info)'},
    'exodusredux': {
        'name'     : 'Exodus Redux',
        'plugin'   : 'plugin.video.exodusredux',
        'saved'    : 'exodusredux',
        'path'     : os.path.join(ADDONS, 'plugin.video.exodusredux'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.exodusredux', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.exodusredux', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'exodusredux_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.exodusredux', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.user', 'trakt.refresh', 'trakt.token'],
        'activate' : 'RunPlugin(plugin://plugin.video.exodusredux/?action=authTrakt)'},
    'openmeta': {
        'name'     : 'OpenMeta',
        'plugin'   : 'plugin.video.openmeta',
        'saved'    : 'openmeta',
        'path'     : os.path.join(ADDONS, 'plugin.video.openmeta'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.openmeta', 'resources/icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.openmeta', 'resources/fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'openmeta_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.openmeta', 'settings.xml'),
        'default'  : 'trakt_access_token',
        'data'     : ['trakt_access_token', 'trakt_refresh_token', 'trakt_expires_at    '],
        'activate' : 'RunPlugin(plugin://plugin.video.openmeta/authenticate_trakt)'},
    'yoda': {
        'name'     : 'Yoda',
        'plugin'   : 'plugin.video.yoda',
        'saved'    : 'yoda',
        'path'     : os.path.join(ADDONS, 'plugin.video.yoda'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.yoda', 'icon.jpg'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.yoda', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'yoda_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.yoda', 'settings.xml'),
        'default'  : 'trakt.auth',
        'data'     : ['trakt.token', 'trakt.refresh', 'trakt.auth'],
        'activate' : 'RunPlugin(plugin://plugin.video.yoda/?action=authTrakt)'},
    'scrubs': {
        'name'     : 'Scrubs v2',
        'plugin'   : 'plugin.video.scrubsv2',
        'saved'    : 'scrubs',
        'path'     : os.path.join(ADDONS, 'plugin.video.scrubsv2'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.scrubsv2', 'icon.jpg'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.scrubsv2', 'fanart.png'),
        'file'     : os.path.join(TRAKTFOLD, 'scrubs_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.scrubs', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.user', 'trakt.user2', 'trakt.token', 'trakt.refresh', 'trakt.auth'],
        'activate' : 'RunPlugin(plugin://plugin.video.scrubsv2/?action=authTrakt)'},
    'premiumizer': {
        'name'     : 'Premiumizer',
        'plugin'   : 'plugin.video.premiumizer',
        'saved'    : 'premiumizer',
        'path'     : os.path.join(ADDONS, 'plugin.video.premiumizer'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.premiumizer', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.premiumizer', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'premiumizer_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.premiumizer', 'settings.xml'),
        'default'  : 'trakt.auth',
        'data'     : ['trakt.token', 'trakt.refresh', 'trakt.auth'],
        'activate' : 'RunPlugin(plugin://plugin.video.premiumizer/?action=authTrakt)'},
    'realizer': {
        'name'     : 'Realizer',
        'plugin'   : 'plugin.video.realizer',
        'saved'    : 'premiumizer',
        'path'     : os.path.join(ADDONS, 'plugin.video.realizer'),
        'icon'     : os.path.join(ADDONS, 'plugin.video.realizer', 'icon.png'),
        'fanart'   : os.path.join(ADDONS, 'plugin.video.realizer', 'fanart.jpg'),
        'file'     : os.path.join(TRAKTFOLD, 'realizer_trakt'),
        'settings' : os.path.join(ADDOND, 'plugin.video.realizer', 'settings.xml'),
        'default'  : 'trakt.auth',
        'data'     : ['trakt.token', 'trakt.refresh', 'trakt.auth'],
        'activate' : 'RunPlugin(plugin://plugin.video.realizer/?action=authTrakt)'}
}

def traktUser(who):
	user=None
	if TRAKTID[who]:
		if os.path.exists(TRAKTID[who]['path']):
			try:
				add = wizard.addonId(TRAKTID[who]['plugin'])
				user = add.getSetting(TRAKTID[who]['default'])
			except:
				return None
	return user

def traktIt(do, who):
	if not os.path.exists(ADDONDATA): os.makedirs(ADDONDATA)
	if not os.path.exists(TRAKTFOLD): os.makedirs(TRAKTFOLD)
	if who == 'all':
		for log in ORDER:
			if os.path.exists(TRAKTID[log]['path']):
				try:
					addonid   = wizard.addonId(TRAKTID[log]['plugin'])
					default   = TRAKTID[log]['default']
					user      = addonid.getSetting(default)
					if user == '' and do == 'update': continue
					updateTrakt(do, log)
				except: pass
			else: wizard.log('[Trakt Data] %s(%s) is not installed' % (TRAKTID[log]['name'],TRAKTID[log]['plugin']), xbmc.LOGERROR)
		wizard.setS('traktlastsave', str(THREEDAYS))
	else:
		if TRAKTID[who]:
			if os.path.exists(TRAKTID[who]['path']):
				updateTrakt(do, who)
		else: wizard.log('[Trakt Data] Invalid Entry: %s' % who, xbmc.LOGERROR)

def clearSaved(who, over=False):
	if who == 'all':
		for trakt in TRAKTID:
			clearSaved(trakt,  True)
	elif TRAKTID[who]:
		file = TRAKTID[who]['file']
		if os.path.exists(file):
			os.remove(file)
			wizard.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TRAKTID[who]['name']),'[COLOR %s]Trakt Data: Removed![/COLOR]' % COLOR2, 2000, TRAKTID[who]['icon'])
		wizard.setS(TRAKTID[who]['saved'], '')
	if not over: wizard.refresh()

def updateTrakt(do, who):
	file      = TRAKTID[who]['file']
	settings  = TRAKTID[who]['settings']
	data      = TRAKTID[who]['data']
	addonid   = wizard.addonId(TRAKTID[who]['plugin'])
	saved     = TRAKTID[who]['saved']
	default   = TRAKTID[who]['default']
	user      = addonid.getSetting(default)
	suser     = wizard.getS(saved)
	name      = TRAKTID[who]['name']
	icon      = TRAKTID[who]['icon']

	if do == 'update':
		if not user == '':
			try:
				with open(file, 'w') as f:
					for trakt in data:
						f.write('<trakt>\n\t<id>%s</id>\n\t<value>%s</value>\n</trakt>\n' % (trakt, addonid.getSetting(trakt)))
					f.close()
				user = addonid.getSetting(default)
				wizard.setS(saved, user)
				wizard.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Trakt Data: Saved![/COLOR]' % COLOR2, 2000, icon)
			except Exception as e:
				wizard.log("[Trakt Data] Unable to Update %s (%s)" % (who, str(e)), xbmc.LOGERROR)
		else: wizard.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Trakt Data: Not Registered![/COLOR]' % COLOR2, 2000, icon)
	elif do == 'restore':
		if os.path.exists(file):
			f = open(file,mode='r'); g = f.read().replace('\n','').replace('\r','').replace('\t',''); f.close();
			match = re.compile('<trakt><id>(.+?)</id><value>(.+?)</value></trakt>').findall(g)
			try:
				if len(match) > 0:
					for trakt, value in match:
						addonid.setSetting(trakt, value)
				user = addonid.getSetting(default)
				wizard.setS(saved, user)
				wizard.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Trakt: Restored![/COLOR]' % COLOR2, 2000, icon)
			except Exception as e:
				wizard.log("[Trakt Data] Unable to Restore %s (%s)" % (who, str(e)), xbmc.LOGERROR)
		#else: wizard.LogNotify(name,'Trakt Data: [COLOR red]Not Found![/COLOR]', 2000, icon)
	elif do == 'clearaddon':
		wizard.log('%s SETTINGS: %s' % (name, settings), xbmc.LOGDEBUG)
		if os.path.exists(settings):
			try:
				f = open(settings, "r"); lines = f.readlines(); f.close()
				f = open(settings, "w")
				for line in lines:
					match = wizard.parseDOM(line, 'setting', ret='id')
					if len(match) == 0: f.write(line)
					else:
						if match[0] not in data: f.write(line)
						else: wizard.log('Removing Line: %s' % line, xbmc.LOGNOTICE)
				f.close()
				wizard.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name),'[COLOR %s]Addon Data: Cleared![/COLOR]' % COLOR2, 2000, icon)
			except Exception as e:
				wizard.log("[Trakt Data] Unable to Clear Addon %s (%s)" % (who, str(e)), xbmc.LOGERROR)
	wizard.refresh()

def autoUpdate(who):
	if who == 'all':
		for log in TRAKTID:
			if os.path.exists(TRAKTID[log]['path']):
				autoUpdate(log)
	elif TRAKTID[who]:
		if os.path.exists(TRAKTID[who]['path']):
			u = traktUser(who)
			su = wizard.getS(TRAKTID[who]['saved'])
			n = TRAKTID[who]['name']
			if u is None or u == '': return
			elif su == '': traktIt('update', who)
			elif not u == su:
				if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to save the [COLOR %s]Trakt Data[/COLOR] for [COLOR %s]%s[/COLOR]?" % (COLOR2, COLOR1, COLOR1, n), "Addon: [COLOR springgreen][B]%s[/B][/COLOR]" % u, "Saved:[/COLOR] [COLOR red][B]%s[/B][/COLOR]" % su if not su == '' else 'Saved:[/COLOR] [COLOR red][B]None[/B][/COLOR]', yeslabel="[B][COLOR springgreen]Save Data[/COLOR][/B]", nolabel="[B][COLOR red]No Cancel[/COLOR][/B]"):
					traktIt('update', who)
			else: traktIt('update', who)

def importlist(who):
	if who == 'all':
		for log in TRAKTID:
			if os.path.exists(TRAKTID[log]['file']):
				importlist(log)
	elif TRAKTID[who]:
		if os.path.exists(TRAKTID[who]['file']):
			d  = TRAKTID[who]['default']
			sa = TRAKTID[who]['saved']
			su = wizard.getS(sa)
			n  = TRAKTID[who]['name']
			f  = open(TRAKTID[who]['file'],mode='r'); g = f.read().replace('\n','').replace('\r','').replace('\t',''); f.close();
			m  = re.compile('<trakt><id>%s</id><value>(.+?)</value></trakt>' % d).findall(g)
			if len(m) > 0:
				if not m[0] == su:
					if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to import the [COLOR %s]Trakt Data[/COLOR] for [COLOR %s]%s[/COLOR]?" % (COLOR2, COLOR1, COLOR1, n), "File: [COLOR springgreen][B]%s[/B][/COLOR]" % m[0], "Saved:[/COLOR] [COLOR red][B]%s[/B][/COLOR]" % su if not su == '' else 'Saved:[/COLOR] [COLOR red][B]None[/B][/COLOR]', yeslabel="[B]Save Data[/B]", nolabel="[B]No Cancel[/B]"):
						wizard.setS(sa, m[0])
						wizard.log('[Import Data] %s: %s' % (who, str(m)), xbmc.LOGNOTICE)
					else: wizard.log('[Import Data] Declined Import(%s): %s' % (who, str(m)), xbmc.LOGNOTICE)
				else: wizard.log('[Import Data] Duplicate Entry(%s): %s' % (who, str(m)), xbmc.LOGNOTICE)
			else: wizard.log('[Import Data] No Match(%s): %s' % (who, str(m)), xbmc.LOGNOTICE)

def activateTrakt(who):
	if TRAKTID[who]:
		if os.path.exists(TRAKTID[who]['path']):
			act = TRAKTID[who]['activate']
			addonid = wizard.addonId(TRAKTID[who]['plugin'])
			if act == '': addonid.openSettings()
			else: url = xbmc.executebuiltin(TRAKTID[who]['activate'])
		else: DIALOG.ok(ADDONTITLE, '%s is not currently installed.' % TRAKTID[who]['name'])
	else:
		wizard.refresh()
		return
	check = 0
	while traktUser(who) is None:
		if check == 30: break
		check += 1
		time.sleep(10)
	wizard.refresh()
