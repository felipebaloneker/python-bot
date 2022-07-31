import random; 
from browser import *;

class Google (Browser):
    def __init__(self):
        super().__init__();
    def runFind(self,words):
        print("Pesquisando:", words )
        pages = ["https://www.google.com.br","https://google.com","https://www.google.es","https://www.google.cz"]
        
        page = pages[random.randint(0, len(pages) -1)];
        print("Google:", page);
        
        self.driver.get(page)
        input_q = self.driver.find_element_by_xpath("//input[@name='q']");
        input_q.send_keys(words);
        input_q.send_keys(Keys.RETURN);

        buffer_links = []
        buffer_quadros = self.driver.find_elements_by_xpath("//div[@class='g' and div[1]/div[1]/div[1]/a]");
        for i in range(len(buffer_quadros)):
            try:
                link = buffer_quadros[i].find_element_by_xpath("./div[1]/div[1]/div[1]/a").get_attribute("href");
                print(link)
                buffer_links.append(link);
            except:
                print("Ignore empty element.");
        return buffer_links;