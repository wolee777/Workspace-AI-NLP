from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print( '{0:^50}\n'.format( 'Selenium 기본 사용법' ) )
print( '\n{0:=<50}\n'.format( 'Selenium으로 특정 web site 표시 ' ) )
path = 'D:/Anaconda3/chromedriver.exe'
driver = webdriver.Chrome( path )
driver.get( 'https://www.google.co.kr' )

print( '\n{0:=<50}\n'.format( 'Selenium으로 검색 ' ) )
search = driver.find_element_by_name( "q" )
search.send_keys( "파이썬" )
search.submit()

print( '{0:^50}\n'.format( 'Selenium으로 Facebook HTML 분석 ' ) )
user = 'wolee777@gmail.com'
password = ''

path = 'D:/Anaconda3/chromedriver.exe'
driver = webdriver.Chrome( path )
driver.get( 'https://www.facebook.com' )
assert 'Facebook' in driver.title

element = driver.find_element_by_id( 'email' )
element.send_keys( user )
element = driver.find_element_by_id( 'pass' )
element.send_keys( password )
element.send_keys( Keys.RETURN )

