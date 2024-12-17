from src import *
from src.plugins.log import *
from src.plugins.files import *

r = requests.get('https://raw.githubusercontent.com/R3CI/discord-api/refs/heads/main/latest-headers.json')

ua = r.json().get('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9173 Chrome/128.0.6613.186 Electron/32.2.2 Safari/537.36')
xsup = r.json().get('X-Super-Properties', 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTczIiwib3NfdmVyc2lvbiI6IjEwLjAuMjYxMDAiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTczIENocm9tZS8xMjguMC42NjEzLjE4NiBFbGVjdHJvbi8zMi4yLjIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMyLjIuMiIsIm9zX3Nka192ZXJzaW9uIjoiMjYxMDAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNTE2NjIsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjU1OTkzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==')

sess = tls_client.Session(
    random_tls_extension_order=True, 
    client_identifier='chrome_120'
)

headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,pl;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://discord.com',
        'Referer': 'https://discord.com/@me',
        'Priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': ua,
        'X-Debug-Options': 'bugReporterEnabled',
        'X-Discord-Locale': 'en-US',
        'X-Discord-Timezone': 'Europe/Warsaw',
        'X-Super-Properties': xsup
    }

r = sess.get(
    'https://discord.com',
    headers=headers
)

cocks = r.cookies.get_dict()
cookies = {
    '__dcfduid': cocks['__dcfduid'],
    '__sdcfduid': cocks['__sdcfduid'],
    '_cfuvid': cocks['_cfuvid'],
    'locale': 'en-US',
    '__cfruid': cocks['__cfruid']
}

class client:
    def __init__(self, token=None):
        self.token = token
        self.proxy = None

        self.sess = tls_client.Session(
            ja3_string='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
            h2_settings={
                'HEADER_TABLE_SIZE': 65536,
                'MAX_CONCURRENT_STREAMS': 1000,
                'INITIAL_WINDOW_SIZE': 6291456,
                'MAX_HEADER_LIST_SIZE': 262144
            },
            h2_settings_order=[
                'HEADER_TABLE_SIZE',
                'MAX_CONCURRENT_STREAMS',
                'INITIAL_WINDOW_SIZE',
                'MAX_HEADER_LIST_SIZE'
            ],
            supported_signature_algorithms=[
                'ECDSAWithP256AndSHA256',
                'PSSWithSHA256',
                'PKCS1WithSHA256',
                'ECDSAWithP384AndSHA384',
                'PSSWithSHA384',
                'PKCS1WithSHA384',
                'PSSWithSHA512',
                'PKCS1WithSHA512'
            ],
            supported_versions=['GREASE', '1.3', '1.2'],
            key_share_curves=['GREASE', 'X25519'],
            cert_compression_algo='brotli',
            connection_flow=15663105,
            force_http1=False,
            random_tls_extension_order=True,
        )

        self.headers = headers
        self.cookies = cookies
        self.xsup = xsup
        self.ua = ua