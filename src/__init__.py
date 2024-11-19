DBG = False
VERSION = 2.07

import sys, os, traceback; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import json
import threading
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
import re
import random
from tkinter import messagebox
from typing import cast
import string
import queue
import tkinter as tk
from tkinter import filedialog
import webbrowser
import base64
from io import BytesIO
import zipfile
import requests
import tls_client
from colorama import Back as B, Style as S
from datetime import datetime as dt
import ab5
import uuid
from bs4 import BeautifulSoup


with open('output\\errors.txt', 'w') as f:
    f.write('')

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'    

class co:
    red = rgb(255, 0, 0)
    black = rgb(77, 76, 76)
    darkred = rgb(92, 1, 1)
    green = rgb(2, 173, 66)
    blue = rgb(0, 146, 250)
    darkblue = rgb(5, 105, 171)
    yellow = rgb(255, 232, 25)
    orange = rgb(255, 158, 3)
    cyan = rgb(0, 245, 233)
    magenta = rgb(245, 0, 241)
    white = rgb(255, 255, 255)

def __INFLOG__(module, message, inp=False, ts=True):
    if ts:
        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '
    else:
        ts = ''
    if inp:
        input(f'{ts}{co.green}[{module}]{co.black} >> {co.green}[{message}]{S.RESET_ALL}')
    else:
        print(f'{ts}{co.green}[{module}]{co.black} >> {co.green}[{message}]{S.RESET_ALL}')

os.system('cls')
size = os.get_terminal_size().columns
banner = f"""
{r'    __    _                    __  __   ____'.center(size)}
{r'   / /   (_)___ ___  ____     /  /  /  /__ /'.center(size)}
{r'  / /   / / __ `__  / _  /   /  /  /  __/ / '.center(size)}
{r' / /___/ / / / / / / ___/   /  /  /  / __/  '.center(size)}
{r'/_____/_/_/ /_/ /_/____/   /_____/  /____/  '.center(size)}
"""
print(ab5.vgratient(banner, [0, 255, 96], [128, 163, 91]))
__INFLOG__('Main', 'Launching!')
__INFLOG__('Main', 'Checking file structure...')

if os.path.abspath(__file__).startswith(os.path.join(os.path.expanduser('~'), 'Downloads')):
    messagebox.showinfo('Info', 'Script is inside of the downloads folder! Please move all files of lime to the desktop to avoid any issues!!')
    exit()