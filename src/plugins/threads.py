import tls_client.exceptions
from src import *
from src.plugins.log import *


class thread:
    def __init__(self, thread_amt, func, tokens=[], args=[]):
        self.maxworkers = int(thread_amt)
        self.func = func
        self.tokens = tokens
        self.args: list = args
        self.futures = []
        self.work()

    def work(self):
        if self.tokens:
            with ThreadPoolExecutor(max_workers=self.maxworkers) as exe:
                for token in self.tokens:
                    self.args.insert(0, token)
                    try:
                        future = exe.submit(self.func, *self.args)
                        self.futures.append(future)
                    except Exception as e:
                        log.error('Threads [main]', e)
                    self.args.remove(token)

                for future in self.futures:
                    try:
                        future.result()
                    except tls_client.exceptions.TLSClientExeption as e:
                        log.error('Threads [result]', f'TLS exception >> {e}')
                    except Exception as e:
                        log.error('Threads [result]', e)
        else:
            log.warn('Threads [main]', 'Please input ur tokens into input\\tokens.txt')
