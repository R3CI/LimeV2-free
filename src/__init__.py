DBG = False

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
import uuid
import queue
import tkinter as tk
from tkinter import filedialog
import webbrowser

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
webbrowser.open('https://discord.gg/spamming')
python_vers = []
for path in os.environ['PATH'].split(os.pathsep):
    try:
        pyfiles = os.listdir(path)
        for pyfile in pyfiles:
            if pyfile.startswith('python') and ('exe' in pyfile or 'bin' in pyfile):
                try:
                    version = subprocess.check_output([os.path.join(path, pyfile), '--version'], stderr=subprocess.STDOUT).decode().strip().split(' ')[1]
                    if version not in python_vers:
                        python_vers.append(version)

                except subprocess.CalledProcessError:
                    continue
                
    except (FileNotFoundError, PermissionError):
        continue

if len(python_vers) > 1:
    messagebox.showerror('Error', 'We have detected that you have multiple version of python installed! Please keep only ONE to avoid any issues! 3.12.7 is recommended')
    exit()

try:
    subprocess.run(['pip', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except FileNotFoundError:
    messagebox.showerror('Error', 'Pip not found! This is most likely due a bad installation of python! Install 3.12.1 and when installing add to path, install as admin and use advanced then make sure pip is checked and you install for all users!!!')
    exit()

if os.path.abspath(__file__).startswith(os.path.join(os.path.expanduser('~'), 'Downloads')):
    messagebox.showerror('Error', 'Script is inside of the downloads folder! Please move all files of lime to the desktop to avoid any issues!!')
    exit()

try:
    import base64
    import requests
    import tls_client
    from colorama import Back as B, Style as S
    from datetime import datetime as dt
    import ab5

except ModuleNotFoundError as e:
    for lib in [e.name, 'requests', 'tls-client', 'typing-extensions', 'colorama', 'datetime', 'ab5']:
        os.system(f'pip install {lib}')

    os.system('cls')
    messagebox.showinfo('Information', 'All needed libs ware downloaded! Please open the script again')