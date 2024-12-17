DBG = False
VERSION = 2.16

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
import io
import tkinter as tk
from tkinter import filedialog
import webbrowser
import ctypes

if len(sys.argv) > 1:
    pass
else:
    os.system('py START.py')
    exit()

import base64
import requests
import tls_client
from colorama import Back as B, Style as S
from datetime import datetime as dt
import ab5
from bs4 import BeautifulSoup
from io import BytesIO
import zipfile

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