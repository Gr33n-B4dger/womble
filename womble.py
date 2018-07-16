+#Import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Opens Headless chrome and navigates to IPVoid
options = Options()
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
print ("\nWelcome to Wobbly Womble!")
driver.get("http://ipvoid.com/ip-blacklist-check")
print ("\nLeaving Wimbledon...")

#Finds IP Address field
#print ("Finding IP address field...")
ipaddr_field = driver.find_element(By.XPATH, '//*[@id="ipAddr"]')
IP4check = raw_input("\nReady! \n\nEnter IP:")
ipaddr_field.send_keys(IP4check)

ipaddr_field.submit()

#Prints results to console
print ("\nWombling...")
blacklists = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]')
print ("\nBlacklist Status for:"), IP4check
print blacklists.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]').text

#Add in loop
def again():
#    print ("\nGo again?")
#    repeat = raw_input("\nGo again?")
#    if repeat == "y" or repeat ==  "yes":
        ipaddr_field = driver.find_element(By.XPATH, '//*[@id="ipAddr"]')
        IP4check = raw_input("\nReady! \nEnter IP:")
        ipaddr_field.send_keys(IP4check)
#        print ("Thank you!")
        ipaddr_field.submit()
#Prints results to console
        print ("Wombling...")
        blacklists = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]')
        print ("Blacklist Status for:"), IP4check
        print blacklists.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]').text
#    else:
#        print("Thank you for wombling")

#//*[@id="ipAddr"]
while True:
    repeat = raw_input("\nGo again? (y/n)")
    if repeat == "y":
        again()
    if repeat == "n":
        print "\nThank you for wombling\n"
        break
