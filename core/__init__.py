import os, sys, time, subprocess, ctypes

__VERSION__ = '1.01'
__CFG_VERSION__ = '1.0'
__CHANGELOG__ = '''
1.01
- Fixes
- Port to the new srouce
- Made it open src
'''

__FULLCHANGELOG__ = '''
1.0
- Release

1.01
- Fixes
- Port to the new srouce
- Made it open src
'''
__DEBUG__ = False

# Ignore this shitty code | loading
OPACITY = 230 # (0-255)
CMD = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SetWindowLongW(CMD, -16, ctypes.windll.user32.GetWindowLongW(CMD, -16) | 0x80000)
ctypes.windll.user32.SetLayeredWindowAttributes(CMD, 0, OPACITY, 0x2)

os.system('cls')
os.system(f'title Lime {__VERSION__} - Loading...')
try:
    from pystyle import Colorate, Colors
    size = os.get_terminal_size().columns - 3
    thing = f'''
{'    dMP     dMP dMMMMMMMMb  dMMMMMP '.center(size)}
{'   dMP     amr dMP"dMP"dMP dMP      '.center(size)}
{'  dMP     dMP dMP dMP dMP dMMMP     '.center(size)}
{' dMP     dMP dMP dMP dMP dMP        '.center(size)}
{'dMMMMMP dMP dMP dMP dMP dMMMMMP     '.center(size)}
{''.center(size)}
{'    dMP    .aMMMb  .aMMMb  dMMMMb  dMP dMMMMb  .aMMMMP               '.center(size)}
{'   dMP    dMP"dMP dMP"dMP dMP VMP amr dMP dMP dMP"                   '.center(size)}
{'  dMP    dMP dMP dMMMMMP dMP dMP dMP dMP dMP dMP MMP"                '.center(size)}
{' dMP    dMP.aMP dMP dMP dMP.aMP dMP dMP dMP dMP.dMP  amr   amr   amr '.center(size)}
{'dMMMMMP VMMMP" dMP dMP dMMMMP" dMP dMP dMP  VMMMP"  dMP   dMP   dMP  '.center(size)}
'''
    print(Colorate.Horizontal(Colors.green_to_white, thing))
    
    print('\n\n')

except ModuleNotFoundError:
    pass

# main modules
try:
    from colorama import Fore, init; init(autoreset=True)
    import tls_client
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    import threading
    import requests
    import uuid
    import tkinter as tk
    from tkinter import filedialog
    import toml
    import random
    import webbrowser
    import re
    import socket
    import psutil
    from pypresence import Presence
    import string
    from datetime import timezone, datetime as dt
    import json
    import base64
    import websocket

# getting libs 
except ModuleNotFoundError as e:
    print(f'Found libs that need to be installed, wait for the script to finish ({e})')
    choice = input('Use more info mode? (y/n) -> ')
    if choice in ['y', 'Y']:
        choice = True
    else:
        choice = False
    time.sleep(2)
    libs = [
        'tls-client',
        'typing-extensions',
        'websocket-client',
        'colorama',
        'pystyle',
        'uuid',
        'requests',
        'pypresence',
        'toml',
        'psutil',
    ]
    
    print('Updating pip...')
    if choice:
        os.system(f'python.exe -m pip install --upgrade pip')
    else:
        os.system(f'python.exe -m pip install -q --upgrade pip')

    for lib in libs:
        print(f'Installing {lib}...')
        time.sleep(0.5)
        if choice:
            os.system(f'pip install {lib}')
        else:
            os.system(f'pip install -q {lib}')
    

    print('\n\nFinished all! Restarting in 2s...')
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)