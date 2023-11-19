import pause as pause
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import ActionChains

websites = ["https://www.cognytics.com/home?TokenID=35fdc7aa-483d-4aae-b196-76945b94ad80&DashboardName=Machine%20Timeline&ShowMenu=false&ShowControlbar=false&ShowFilters=false", "https://www.cognytics.com/home?TokenID=47a29d35-8abd-406d-ba67-8ce6bfd5cc76&DashboardName=Machine%20Timeline&ShowMenu=false&ShowControlbar=false&ShowFilters=false"]
refreshTime = (60 * 15)

def clickButton(driver):
    # try to click button
    a = ActionChains(driver)
    try:
        m = driver.find_element("xpath",
                                "/html/body/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/blockquote[2]/div/div/div[5]/div[1]/div[2]")
        a.move_to_element(m).perform()
        #driver.find_element("id", "button-1021-btnIconEl").click()
        driver.find_element("id", "button-1022-btnIconEl").click()
        a.move_by_offset(0, 0).perform()
    except:
        pause.seconds(1)
        clickButton(driver)

def run():
    currentSite = 0
    service = webdriver.FirefoxService("/home/admin/.cargo/bin/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.fullscreen_window()
    driver.get(websites[currentSite])

    while True:
        clickButton(driver)
        pause.seconds(refreshTime)
        currentSite = (currentSite + 1) % len(websites)
        driver.get(websites[currentSite])
        driver.refresh()


if __name__ == '__main__':
    run()

