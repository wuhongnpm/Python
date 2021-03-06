# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#adb shell dumpsys window | findstr mCurrentFocus
#adb shell getprop ro.product.model


from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "CJ-JD-70"
caps["appPackage"] = "com.ccl.appstore"
caps["appActivity"] = "com.ccl.appstore.Main2Activity"
caps["autoGrantPermissions"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#添加隐式等待
driver.implicitly_wait(1)

"""
#增加TouchAction
TouchAction(driver).long_press().move_to().release().perform();
driver.swipe()
"""
el1 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"Subscriptions\"]/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"Library\"]/android.widget.ImageView")
el2.click()
el3 = driver.find_element_by_accessibility_id("Search")
el3.click()
el4 = driver.find_element_by_id("com.google.android.youtube:id/search_edit_text")
el4.click()
el4.send_keys("wuhong")

driver.quit()