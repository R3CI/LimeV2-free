import os
import time

try:
    import requests
    import tls_client
    from colorama import Back as B, Style as S
    from datetime import datetime as dt
    import ab5
    from bs4 import BeautifulSoup
    from io import BytesIO
    import zipfile

except ModuleNotFoundError:
    print('Modules not found! Installing in 3s')
    time.sleep(3)

    libs = [
        'uuid',
        'ab5',
        'datetime',
        'colorama',
        'requests',
        'tls-client',
        'beautifulsoup4',
        'typing-extensions',
        'typing'
    ]

    for lib in libs:
        os.system(f'pip install {lib}')
    
    print('Modules installed! Starting in 3s')
    time.sleep(3)
    os.system('py main.py limev2')
    exit()

except Exception as e:
    print('Failed to import modules')
    print(e)
    input('Enter to quit...')
    exit()

os.system('py main.py limev2')