import random;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class Browser:
    def __init__(self):
        CURRENTDIR = '/Users/hunter/Documents/projects/personal/bots/chromedriver'
        chrome_option = webdriver.ChromeOptions();
        agents = [
            "Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0",
            "Mozilla/5.0 (Linux; Android 5.0.1; LGLK430 Build/LRX21Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
        ]
        agent = agents[random.randint(0, len(agents) - 1)];
        chrome_option.add_argument("user-agent="+agent);
        chrome_option.add_argument("--headless");
        chrome_option.add_argument("--no-sandbox");
        chrome_option.add_argument("--mute-audio");
        self.driver = webdriver.Chrome(CURRENTDIR, chrome_options=chrome_option)

    def runFind(self, words):
        print("...Metodo nao implementado....");
    
    def __del__(self):
        self.driver.close();