import tls_client.exceptions
from core import *
from core.plugins.log import *
from core.discordutils import *


class thread:
    def __init__(self, thread_amt: str, func, tokens: list = [], args: list = []) -> None:
        self.maxworkers = int(thread_amt)
        self.func = func
        self.tokens = tokens
        self.args = args

    def work(self):
        futures = []
        if self.tokens:
            with ThreadPoolExecutor(max_workers=self.maxworkers) as exe:
                for token in self.tokens:
                    exe.submit(Discord.online, token)
                    self.args.insert(0, token)
                    try:
                        future = exe.submit(self.func, *self.args)
                        futures.append(future)
                    except Exception as e:
                        log.fail(e)
                    self.args.remove(token)

                for future in futures:
                    try:
                        future.result()
                    except tls_client.exceptions.TLSClientExeption as e:
                        log.fail(f'TLS exception -> {e}')
                    except Exception as e:
                        log.fail(e)
        else:
            log.warn('No tokens were passed, input your tokens inside of tokens.txt (if other features work, it is most likely a code error, please let me know)')
