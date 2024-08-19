from core import *

class utils:
    def random_string(length: int) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def getnonce():
        return str((int(time.mktime(dt.now().timetuple())) * 1000 - 1420070400000) * 4194304)
    
    def gettimestamp():
        timestamp = "{:.0f}".format(time.time() * 1000)
        return timestamp
