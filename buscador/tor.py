import time;

from  browser  import *;

class Tor (Browser):
    def __init_(self, socks5=None):
        super()._init_(socks5=socks5);
    def test(self):
        self.driver.get("https://check.torproject.org");
        time.sleep(20);