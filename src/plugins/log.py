from src import *

class log:
    def basic(ts=False, color=co.white, message='None', type=None):
        if ts:
            ts = f'{co.black}{dt.now().strftime("%H %M %S")}'
        else:
            ts = ''

        if type == 'info':
            type = f'{co.green} (*)'

        elif type == 'error':
            type = f'{co.red} (!)'

        elif type == 'warning':
            type = f'{co.yellow} (#)'

        elif type == 'debug':
            type = f'{co.orange} ($)'

        elif type == None:
            type = ' '

        else:
            type = ' (*)'

        print(f'{ts}{type} >> {color}{message}{S.RESET_ALL}')
    
    def info(module, message, inp=False, ts=True):
        if ts:
            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '
        else:
            ts = ''
        if inp:
            input(f'{ts}{co.green}[{module}]{co.black} >> {co.green}[{message}]{S.RESET_ALL}')
        else:
            print(f'{ts}{co.green}[{module}]{co.black} >> {co.green}[{message}]{S.RESET_ALL}')

    def dbg(module, *message):
        if DBG:
            if len(message) == 1 and isinstance(message[0], str):
                message = [message[0]]
            message = ' | '.join(map(str, message))
            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")}'
            print(f'{ts} {co.yellow}[{module}]{co.black} >> {co.yellow}[{message}]{S.RESET_ALL}')

    def warn(module, message):
        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")}'
        print(f'{ts} {co.orange}[{module}]{co.black} >> {co.orange}[{message}]{S.RESET_ALL}')

    def hcap(module, message):
        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")}'
        print(f'{ts} {co.darkblue}[{module}]{co.black} >> {co.darkblue}[{message}]{S.RESET_ALL}')

    def error(module, message, ts=True):
        if not ts:
            ts = ''
        else:
            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '
        print(f'{ts}{co.red}[{module}]{co.black} >> {co.red}[{message}]{S.RESET_ALL}')
        
    def critical(module, message):
        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")}'
        print(f'{ts} {co.darkred}[{module}]{co.black} >> {co.darkred}[{message}]{S.RESET_ALL}')

    def premium_only():
        print(f'{co.green}[Main]{co.black} >> {co.green}[This is a premium only feature]{S.RESET_ALL}')

    def inwork():
        print(f'{co.green}[Main]{co.black} >> {co.green}[This feature is in work]{S.RESET_ALL}')

    def errordatabase(text):
        db = {
            '10014': 'Unknown emoji',
            '30010': 'Max reactions',
            '40007': 'Banned',
            '40002': 'Locked',
            '50109': 'Invalid JSON',
            '200000': 'Automod flagged',
            '50007': 'Not allowed',
            '50008': 'Unable to send',
            '50001': 'No access/Not inside',
            '50013': 'Missing permissions',
            '50024': 'Cant do that on this channel',
            '80003': 'Cant self friend',
            '50168': 'Not in a VC',
            '20028': 'Limited',
            '401: Unauthorized': 'Unauthorized',
            'Cloudflare': 'Cloudflare',
            'captcha_key': 'Hcaptcha',
            'Unauthorized': 'Unauthorized',
            'retry_after': 'Limited',
            'You need to verify': 'Locked',
            'Cannot send messages to this user': 'Disabled DMS',
            'You are being blocked from accessing our API': 'API BAN'
        }

        for key in db.keys():
            if key in text:
                return db[key]

        return text