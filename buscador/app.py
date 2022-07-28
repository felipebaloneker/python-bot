class Tor (Browser):
    def __init_(self, socks5=None):
        super()._init_(socks5=socks5);
    def test(self):
        self.driver.get("https://check.torproject.org");
        time.sleep(20);


class Browser:
    def _init_(self, socks5=None):
        chrome_options = webdriver.ChromeOptions()
        if socks5 != None:
            chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:"+socks5);
        # agentList = open("../agents.txt","r").read()
        # agents = [agentList]
        agents = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];
        agent = agents[random.randint(0, len(agents) -1)];
        chrome_options.add_argument("user-agent="+ agent)
        chrome_options.add_argument("--headless");
        chrome_options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options);
    def executeBusca(self, palavras):
        print("... Metodo nao implementado....");
    def __del__(self):
        self.driver.close();

        