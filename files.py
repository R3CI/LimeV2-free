from core import *

class files:
    def makefiles():
        for file in [
                'data\\tokens.txt',
                'data\\proxies.txt',
                'config.toml',
            ]:
            if not os.path.exists(file):
                open(file, 'w').close()

    def makefolders():
        for folder in [
                'data',
                'data\\scrapes',
                'data\\scrapes\\usernames',
                'data\\scrapes\\ids'
            ]:
            os.makedirs(folder, exist_ok=True)

    def dotasks():
        for task in [
                files.makefolders,
                files.makefiles
            ]:
            task()
    
files.dotasks()