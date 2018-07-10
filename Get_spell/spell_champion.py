from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class Load:
    
    def Waiting(self):
        timer = 0
        while(timer < 4):
            time.sleep(1)
            timer += 1 
        

    def load(self):
        print "Loading ..."
        i = 0
        scroll = Get_Spell().driver.find_element_by_xpath('//body')
        while i < 5:
            scroll.send_keys(Keys.END)
            i += 1
        i = 0
        self.Waiting()

class Get_Spell:
    def __init__(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

    def Print_Spell(self, url):
        self.driver.get(url)
        PNames = self.driver.find_element_by_xpath('//*[@id="PName"]/h3')
        QNames  = self.driver.find_element_by_xpath('//*[@id="QName"]/h3')
        WNames = self.driver.find_element_by_xpath('//*[@id="WName"]/h3')
        ENames = self.driver.find_element_by_xpath('//*[@id="EName"]/h3')
        RNames = self.driver.find_element_by_xpath('//*[@id="RName"]/h3')
        # count = len(PNames)
        print "Passif: ", PNames.text
        print "Q: ", QNames.text
        print "W: ", WNames.text
        print "E: ", ENames.text
        print "R: ", RNames.text

    def Launch(self, url):
        Load().load()
        self.Print_Spell(url)

    def Call(self, Names):
        i = 0
        Language = "fr"
        Name = ["Ashe", "Aatrox", "Ahri", "Udyr", "Garen"]
        count = len(Name)
        while i < count:
            try:
                print "------------------------------------- " + Name[i] + " -------------------------------------"
                # This is the French url, check on internet to get other language url
                self.Launch("https://euw.leagueoflegends.com/" + Language + "/game-info/champions/" + Name[i])
            except:
                print "Champions name doesn't exist"
            i += 1
        print "------------------------------------- END -------------------------------------"

Names = ["Ashe", "Aatrox", "Ahri", "Udyr", "Garen"]
Spell = Get_Spell()
Spell.Call(Names)