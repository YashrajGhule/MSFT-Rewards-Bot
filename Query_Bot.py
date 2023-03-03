import selenium.webdriver
from selenium.webdriver.common.by import By
import time

username = input("Enter Username/Email: ")
psswd = input("Enter Password: ")
# DATAFILE CAN BE DOWNLOADED FROM trends.google.com
datafile = input("Enter Path of Datafile: ")
platform = input("Enter Platform (Android/Windows) :")


options = selenium.webdriver.ChromeOptions()
service = selenium.webdriver.chrome.service.Service(r"chromedriver.exe")

# ANDROID : Mozilla/5.0 (Linux; Android 12; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 EdgA/110.0.1587.54
# WINDOWS : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.14
if platform.lower() == "android":
    print("Microsoft Edge on Android 12")
    options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/110.0.1587.54")
elif platform.lower() == "windows":
    print("Microsoft Edge on Windows 10")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.14")
options.add_argument("webdriver=false")

options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = selenium.webdriver.Chrome(service=service,options=options)

driver.get("https://rewards.bing.com/")

driver.find_element(By.NAME,"loginfmt").send_keys(username)
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(0.1*len(username))

driver.find_element(By.NAME,"passwd").send_keys(psswd)
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(0.1*len(psswd))

try:
    driver.find_element(By.ID,"idSIButton9").click()
except:
    pass

driver.get("https://www.bing.com/")

data = open(datafile,"r")
query_list = data.read().split("\n")
data.close()

count = 0
queries = int(input("Enter Number of queries: "))

#Start from 4th index as actual query starts from 5th line
for query in query_list[4:]:
    if query == "" or query == "TOP" or query == "RISING":
        continue
    if count == queries:
        print(count,"queries performed")
        queries = int(input("Enter Number of queries: "))
        count = 0
        if queries == 0:
            break
    sb_form_q = driver.find_element(By.ID,"sb_form_q")
    print(query.split(",")[0])
    sb_form_q.clear()
    sb_form_q.send_keys(query.split(",")[0])
    sb_form_q.submit()
    time.sleep(0.1*len(query.split(",")[0]))
    count += 1

# https://www.bing.com/search?q=hello&qs=n&form=QBRE&sp=-1&ghc=1&lq=1&pq=hello&sc=1-5&sk=&cvid=B24B7665B0AE4CB197D43A53EC22BE49&ghsh=0&ghacc=0&ghpl=
# https://www.bing.com/search?q=world&qs=n&form=QBRE&sp=-1&ghc=1&lq=1&pq=wor&sc=1-3&sk=&cvid=ED42B84F3DC549AFB19B72EB703BD2A9&ghsh=0&ghacc=0&ghpl=

driver.quit()