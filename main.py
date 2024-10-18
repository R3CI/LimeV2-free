import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from core import *
from core import __VERSION__, __CHANGELOG__, __FULLCHANGELOG__
from core.plugins import *
from core.modules import *

webbrowser.open('https://discord.gg/spamming')

while True:
    rpc.update('In the main menu')
    cmd.cls()
    cmd.title(f'Lime {__VERSION__} | Tokens {get.token_count()} | Proxies {get.proxy_count()} | dsc.gg/limetool | Made by R3CI')
    UI().banner()
    UI().menu()
    choicething = Colorate.Horizontal(Colors.green_to_white, f'''
┏━━{os.getlogin()}@Lime
┗━━━> ''')
    choice = input(choicething)
    options = {
        '1': (server_managment.menu, 'Server managment'),
        '2': (token_managment.menu, 'Token managment'),
        '3': (spamming_memnu.menu, 'Spamming menu'),
        '4': (bypass_menu.menu, 'Bypass menu'),
        '5': (vc_menu.menu, 'VC menu'),
        '6': (webhook_menu.menu, 'Webhook menu'), 
        '7': (log.log('UI', 'This feature is paid ONLY'), 'Server admin menu'),
        '8': (log.log('UI', 'This feature is paid ONLY'), 'Mass report menu'),
        '9': (log.log('UI', 'This feature is paid ONLY'), 'Mass DM menu'),
        '10': (spam_call.menu, 'Spam call'),
        '11': (button_spammer.menu, 'Button spammer'),
        '12': (log.log('UI', 'Just use button spammer for that'), 'Mass ticket maker'),
        '13': (mass_friender.menu, 'Mass friender'),
        '14': (reaction_bomber.menu, 'Reaction bomber'),
        '15': (mass_invite_maker.menu, 'Mass invite maker'),
        '16': (poll_voter.menu, 'Poll voter'),
        '17': (log.wip, 'None'),
        '18': (log.wip, 'None'),
        '21': (log.wip, 'None'),
        '22': (log.wip, 'None'),
        '23': (log.wip, 'None'),
        '24': (log.wip, 'None')
    }   

    if choice in options:
        func, name = options[choice]
        rpc.update(f'Using {name}')
        cmd.cls()
        UI().banner()
        func()
        log.log('UI', 'Finished!, enter to continue', True)

    elif choice == '19':
        log.log('UI', 'This feature is paid ONLY', True)

    elif choice == '20':
        log.log('UI', 'This feature is paid ONLY', True)
    
    elif choice in ['REP', 'rep']:
        log.log('UI', 'For now report all issues to my dms (r3ci_)', True)

    elif choice in ['EX', 'ex']:
        UI().make_menu([
            'Changelog (old -> current version)',
            'Full changelog (start -> current)'
        ], True, 1)

        choice = UI().ask('CHOICE')
        if choice in ['01', '1']:
            print(Colorate.Horizontal(Colors.green_to_white, __CHANGELOG__))
            input(Colorate.Horizontal(Colors.green_to_white, 'Enter to continue'))

        elif choice in ['02', '2']:
            print(Colorate.Horizontal(Colors.green_to_white, __FULLCHANGELOG__))
            input(Colorate.Horizontal(Colors.green_to_white, 'Enter to continue'))
        
        elif choice == '<<':
            log.log('UI', 'Returning')

    else:
        log.log('UI', 'Not a valid option, enter to continue', True)
