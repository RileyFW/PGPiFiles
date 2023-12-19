import pause as pause
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import ActionChains

websites = ["https://www.cognytics.com/home?TokenID=47a29d35-8abd-406d-ba67-8ce6bfd5cc76&DashboardName=Machine%20Timeline&ShowMenu=false&ShowControlbar=false&ShowFilters=false", "https://www.cognytics.com/home?TokenID=052cd1db-78cd-47f8-8ed9-53ff8932fdd4&DashboardName=Machine%20Timeline&ShowMenu=false&ShowControlbar=false&ShowFilters=false"]
refreshTime = 10 #refresh time in minutes

def writeToLog(text):
    log = open("log.log", "a")
    log.write(text + "\n")
    log.flush()
    os.fsync(log.fileno())

def clickButton(driver):
    # try to click button
    a = ActionChains(driver)
    try:
        m = driver.find_element("xpath",
                                '/html/body/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/blockquote[2]/div/div/div[5]/div[1]')
        a.move_to_element(m).perform()
        #driver.find_element("id", "button-1021-btnIconEl").click()
        driver.find_element("id", "button-1022-btnIconEl").click()
        writeToLog("Clicked button\n")
        while True:
            try:
                a.move_by_offset(0, 50).perform()
            except:
                break
    except:
        pause.seconds(1)
        clickButton(driver)

def handleError(driver, currentSite):
    try:
        driver.get(websites[currentSite])
    except:
        pause.seconds(1)
        handleError(driver, currentSite)

def run():
    # clear the log on program start
    log = open("log.log", "w")
    log.write("")
    log.close()
    writeToLog("Starting program\n")
    currentSite = 0
    service = webdriver.FirefoxService("/home/admin/.cargo/bin/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.fullscreen_window()
    try:
        driver.get(websites[currentSite])
    except:
        #keep trying until the address is live
        handleError(driver, currentSite)


    while True:
        clickButton(driver)
        pause.minutes(refreshTime)
        currentSite = (currentSite + 1) % len(websites)
        try:
            driver.get(websites[currentSite])
        except:
            handleError(driver, currentSite)
        writeToLog("Switched to site " + str(currentSite) + "\n")


if __name__ == '__main__':
    run()

