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
from src.modules.reaction import *
from src.modules.display_changer import *

auto_update()
time.sleep(1.5)

while True:
    ui().cls()
    ui().title('Lime V2 free - discord.gg/spamming')
    ui().banner()
    ui().stats()
    ui().menu()

    choice = ui().ask('Choice')

    options = {
        '>>': lambda: (ui().menu2(), ui().ask('Choice')),
        '1': joiner().main,
        '2': leaver().main,
        '3': isinserver().main,
        '4': log.premium_only,
        '5': log.premium_only,
        '6': message_spammer().main,
        '7': log.premium_only,
        '8': log.premium_only,
        '9': log.premium_only,
        '10': log.premium_only,
        '11': checker().main,
        '12': log.premium_only,
        '13': log.premium_only,
        '14': display_changer().main,
        '15': log.premium_only,
        '16': log.premium_only,
        '17': reaction().main,
        '18': log.premium_only,
        '19': log.premium_only,
        '20': log.premium_only,
        '21': log.premium_only,
        '22': log.premium_only,
        '23': log.premium_only,
        '24': log.premium_only,
        '25': log.premium_only,
        '26': log.premium_only,
        '27': log.premium_only,
        '28': log.premium_only,
        '29': log.premium_only,
        '30': log.premium_only,
    }

    if choice in options:
        options[choice]()
    else:
        log.info('Main', 'That option does not exist', True)

    log.info('Main', 'Finished! Enter to continue | If you like the tool make sure to leave a vouch!', True)

