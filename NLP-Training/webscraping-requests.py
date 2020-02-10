import requests
import MyCrawlingLib as mcl

print( '{0:=<50}\n'.format( 'GET 방식 Response - 100' ) )
url = 'http://www.crawler-test.com/status_codes/status_100'
mcl.getDownload( url )

print( '\n{0:=<50}\n'.format( 'GET 방식 Response - 200' ) )
url = 'http://www.crawler-test.com/status_codes/status_200'
mcl.getDownload( url )

print( '\n{0:=<50}\n'.format( 'GET 방식 Response - 300' ) )
url = 'http://www.crawler-test.com/status_codes/status_300'
mcl.getDownload( url )

print( '\n{0:=<50}\n'.format( 'GET 방식 Response - 400' ) )
url = 'http://www.crawler-test.com/status_codes/status_400'
mcl.getDownload( url )

print( '\n{0:=<50}\n'.format( 'GET 방식 Response - 500' ) )
url = 'http://www.crawler-test.com/status_codes/status_500'
mcl.getDownload( url )

print( '\n{0:=<50}\n'.format( 'POST 방식 Response' ) )
url = 'http://pythonscraping.com/pages/files/processing.php'
data = { 'firstname':'테스트', 'lastname':1234 }
html = mcl.postDownload( url, data )

print( html.request.body )
print( html.request.headers )
print( html.text )

print( '\n{0:=<50}\n'.format( 'POST 방식 Response - Cookie 포함' ) )
url = 'http://pythonscraping.com/pages/cookies/login.php'
data = { 'username':'test', 'password':'password' }
html = mcl.postDownload( url, data )
cookie = html.cookies.get_dict()

html = requests.post( url, cookies = cookie )
html.text

print( '\n{0:=<50}\n'.format( 'POST 방식 Response - Session 방식' ) )
session = requests.Session()
data = { 'username':'test', 'password':'password' }

html = session.post( url, data )

html = session.post( url )
print( html.text )
