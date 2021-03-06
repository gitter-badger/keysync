import os
__all__ = ['adium', 'gibberbot', 'irssi', 'jitsi', 'pidgin', 'gajim',]

import adium, gibberbot, irssi, jitsi, pidgin, gajim
apps = { 'adium'     : adium.AdiumProperties,
         'gibberbot' : gibberbot.GibberbotProperties,
         'irssi'     : irssi.IrssiProperties,
         'jitsi'     : jitsi.JitsiProperties,
         'pidgin'    : pidgin.PidginProperties,
         'gajim'     : gajim.GajimProperties,
        }
apps_supported = apps.keys()

def make_outdir(output_folder, subdir):
    dir = os.path.join(output_folder, subdir)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


