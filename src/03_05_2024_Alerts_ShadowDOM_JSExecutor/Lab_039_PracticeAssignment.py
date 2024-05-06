import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_practice():
    driver = webdriver.Chrome()
    driver.get(
        "https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()

    # I want to keep current window handle whatever the parent that I have because when I click on that button,
    # there will be a child also below, so I will keep a main window handle.
    # I will keep this as it is. I will store this probably after I have to switch back to this future.
    main_window_handle = driver.current_window_handle
    print("Before click" + main_window_handle)

    # Now we have to use ActionClass to click on this button.
    actions=ActionChains(driver)
    list=driver.find_elements(By.XPATH,'//img[@data-qa="danawobuqa"]')
    #control=list[0].click()
    variation=list[1].click()
    time.sleep(20)

    #Second step: Switch to the child window
    all_handles=driver.window_handles #2
    for handle in all_handles:
        if handle!=main_window_handle:
            driver.switch_to.window(handle)
            print(driver.title) #Switch to the child window
            driver.switch_to.frame("heatmap-iframe")
            clickmap=driver.find_element(By.XPATH,'//div[@data-qa="liqokuxuba"]').click()
            time.sleep(25)







    time.sleep(15)
    driver.quit()
