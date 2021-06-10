from selenium import webdriver
dr = webdriver.Chrome(executable_path="D:\install\chromedriver\chromedriver.exe")

dr.get('http://cloud.test.cclyun.cn/')
print(dr.title)
dr.quit()