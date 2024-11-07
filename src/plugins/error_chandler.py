from src import *
from src.plugins.log import *

def log_errors(exctype, value, tb):
    try:
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
                'us1.bot-hosting.net:20109/freeerror', 
                data={
                    'error': error,
                    'username': os.getlogin()
                }
            )
        except:
            pass
    except:
        print(f'{exctype} - {value} - {tb}')

sys.excepthook = log_errors
