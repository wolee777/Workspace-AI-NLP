from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

print( '{0:^50}\n'.format( 'Selenium과 BeautifulSoup을 이용하여 Web Scraping' ) )
print( '{0:=<50}\n'.format( '' ) )

user = 'wolee777@gmail.com'
password = 'yw949704*mc'

path = 'D:/Anaconda3/chromedriver.exe'
driver = webdriver.Chrome( path )
driver.get( 'https://www.facebook.com' )
assert 'Facebook' in driver.title

element = driver.find_element_by_id( 'email' )
element.send_keys( user )
element = driver.find_element_by_id( 'pass' )
element.send_keys( password )
element.send_keys( Keys.RETURN )

time.sleep( 5 )

# selector :  #u_0_a > div:nth-child(1) > div:nth-child(1) > div > a
# xpath    :  //*[@id="u_0_a"]/div[1]/div[1]/div/a
a = driver.find_element_by_xpath( '//*[@id="u_0_a"]/div[1]/div[1]/div/a' )
print( a )
driver.get( a.get_attribute( 'href' ) )

req = driver.page_source
dom = BeautifulSoup( req, 'html.parser' )
information_list = dom.select( '#u_ps_fetchstream_4_2_1' )
for information in information_list:
    print( information )
