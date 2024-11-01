from src import *
from src.plugins.log import *

def log_errors(exctype, value, tb):
    error = ''.join(traceback.format_exception(exctype, value, tb))
    log.error('Error chandler', error, False)
    try:
        with open('output\\errors.txt', 'a') as f:
            f.write(error)
    except:
        with open('ERRORS.txt', 'a') as f:
            f.write(error)

    try:
        requests.post(
            'http://fi1.bot-hosting.net:6495/freeerror', 
            data={
                'error': error,
                'username': os.getlogin()
            }
        )
    except:
        pass

sys.excepthook = log_errors