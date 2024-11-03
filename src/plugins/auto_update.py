from src import *
from src.plugins.log import *

class auto_update:
    def __init__(self):
        self.current = VERSION
        log.info('Auto update', f'Current version >> {self.current}')
        r = requests.get('https://github.com/R3CI/LimeV2-free/releases/latest')
        soup = BeautifulSoup(r.content, 'html.parser')
        self.newest = soup.find('span', {'class': 'css-truncate-target'}).text.strip()
        log.info('Auto update', f'Newest version >> {self.current}')

        if self.check():
            log.info('Auto update', 'Update available')
            self.currentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'LimeV2-latest-' + str(self.newest)))
            if not os.path.exists(self.currentdir):
                os.mkdir(self.currentdir)  
                
                r = requests.get(f'https://github.com/R3CI/LimeV2-free/archive/refs/tags/{self.newest}.zip')
                zip_file = BytesIO(r.content)
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    zip_ref.extractall(self.currentdir)

                messagebox.showinfo('Info', f'Auto updated lime! Updated script can be found on {self.currentdir}\nMake sure to transfer ur proxies and tokens!')
                exit()

        else:
            log.info('Auto update', 'No update available')


    def check(self):
        if float(self.current) != float(self.newest):
            return True
        else:
            return False

    def auto_update(self):
        if self.check():
            return True
        else:
            return False