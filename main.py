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

    # yeah chosing system could be better but its the most relaible 🙏🙏🙏🙏
    x = ui().ask('Choice')

    if x == '>>':
        ui().menu2()
        x = ui().ask('Choice')
    
    elif x in ['01', '1']:
        joiner().main()
    
    elif x in ['02', '2']:
        leaver().main()
    
    elif x in ['03', '3']:
        isinserver().main()
    
    elif x in ['04', '4']:
        log().premium_only()
    
    elif x in ['05', '5']:
        log().premium_only()
    
    elif x in ['06', '6']:
        message_spammer().main()
    
    elif x in ['07', '7']:
        log().premium_only()
    
    elif x in ['08', '8']:
        log().premium_only()
    
    elif x in ['09', '9']:
        log().premium_only()
    
    elif x in ['10']:
        log().premium_only()
    
    elif x in ['11']:
        checker().main()

    elif x in ['12']:
        log().premium_only()

    elif x in ['13']:
        log().premium_only()

    else:
        log.info('Main', 'That option does not exist yet', True)    
        
    log.info('Main', 'Finished! Enter to continue', True)    