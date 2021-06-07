from selenium import webdriver
dr = webdriver.Chrome(executable_path="D:\package\chromedriver\chromedriver.exe")

dr.get('http://cloud.test.cclyun.cn/')
print(dr.title)
dr.quit()