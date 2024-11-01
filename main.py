import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *
from src.plugins.error_chandler import *
from src.plugins.files import *; files()
from src.plugins.log import *
from src.plugins.ui import *

from src.modules.joiner import *
from src.modules.leaver import *
from src.modules.isinserver import *
from src.modules.message_spammer import *
from src.modules.checker import *

ui().cls()
ui().title('Lime V2 free - discord.gg/spamming')
ui().banner()
log.info('Main', 'Startring up!')


while True:
    ui().cls()
    ui().title('Lime V2 free - discord.gg/spamming')
    ui().banner()
    ui().stats()
    ui().menu()

    options = { # use lime for 100000000 free options
        '>>': lambda: [ui().menu2(), ui().ask('Choice')],
        '1': joiner().main(),
        '2': leaver().main(),
        '3': isinserver().main(),
        '6': message_spammer().main(),
        '11': checker().main(),
    }
    
    choice = ui().ask('Choice')
    if choice in options:
        options[choice]()
    else:
        log().premium_only()
        
    log.info('Main', 'Finished! Enter to continue', True)    
