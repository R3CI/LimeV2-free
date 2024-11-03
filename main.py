import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *
from src.plugins.error_chandler import *
from src.plugins.files import *; files()
from src.plugins.log import *
from src.plugins.ui import *
from src.plugins.auto_update import *

from src.modules.joiner import *
from src.modules.leaver import *
from src.modules.isinserver import *
from src.modules.message_spammer import *
from src.modules.checker import *

ui().cls()
ui().title('Lime V2 free - discord.gg/spamming')
ui().banner()
log.info('Main', 'Startring up!')
auto_update()

time.sleep(2.5)

while True:
    ui().cls()
    ui().title('Lime V2 free - discord.gg/spamming')
    ui().banner()
    ui().stats()
    ui().menu()

    x = ui().ask('Choice')

    options = {
        '>>': lambda: [ui().menu2(), ui().ask('Choice')],
        '1': joiner().main,
        '2': leaver().main,
        '3': isinserver().main,
        '4': log.premium_only(),
        '5': log.premium_only(),
        '6': message_spammer().main,
        '7': log.premium_only(),
        '8': log.premium_only(),
        '9': log.premium_only(),
        '10': log.premium_only(),
        '11': log.premium_only(),
        '11': checker().main,
    }

    choice = ui().ask('Choice')
    if choice in options:
        options[choice]()

    else:
        log.info('Main', 'That option does not exist yet', True)    
        
    log.info('Main', 'Finished! Enter to continue', True)    
