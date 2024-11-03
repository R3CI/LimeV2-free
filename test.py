import os
try:
    import random
    import requests
    import discord
    import json
    import time
    import io
    import threading
    import asyncio
    import string
    from discord import Button, Embed, Color, app_commands, ButtonStyle, ui, TextStyle
    from discord.ui import Button, View
    import multiprocessing
    from quart import Quart, redirect, request, render_template, jsonify
    from discord.ext import commands, tasks
    from hypercorn.asyncio import serve
    from hypercorn.config import Config
    import collections
    from datetime import timedelta
    import hmac
    import datetime
    import hashlib
    import uuid
except Exception as e:
    print(e)
    libs = [
        'quart'
    ]
    
    for lib in libs:
        os.system(f'pip install {lib}')