from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>The BeautifulSoup Training</title>
    </head>
    <body>
        <p class="title"><b>The BeautifulSoup Training</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        
        <p class="story">...</p>
'''

print( '{0:^50}\n'.format( 'BeautifulSoup 기본 사용법' ) )
print( '\n{0:=<50}\n'.format( 'dom.prettify() ' ) )
dom = BeautifulSoup( html, 'html.parser' )
print( dom.prettify() )

print( '\n{0:=<50}\n'.format( 'dom.title ' ) )
print( dom.title )

print( '\n{0:=<50}\n'.format( 'dom.title.string ' ) )
print( dom.title.string )

print( '\n{0:=<50}\n'.format( 'dom.title.parent.name ' ) )
print( dom.title.parent.name )

print( '\n{0:=<50}\n'.format( 'dom.p ' ) )
print( dom.p )

print( '\n{0:=<50}\n'.format( 'dom.find_all( "a" ) ' ) )
print( dom.find_all( 'a' ) )

print( '\n{0:=<50}\n'.format( 'dom.get_text() ' ) )
print( dom.get_text() )

print( '{0:^50}\n'.format( 'requests 기본 사용법' ) )
import requests

url = "https://www.daum.net"
response = requests.get( url )
response_text = response.text

print( '\n{0:=<50}\n'.format( 'Daum 실시간 검색어 scraping ' ) )
dom = BeautifulSoup( response_text, 'html.parser' )
top_list = dom.select( "#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div > span.txt_issue > a" )

print( top_list )

print( '\n{0:=<50}\n'.format( 'Daum 실시간 검색어 1위 ' ) )
print( top_list[ 0 ].text )

print( '\n{0:=<50}\n'.format( 'Daum 실시간 검색어 목록 ' ) )
for top in top_list:
    print( top.text )

print( '\n{0:=<50}\n'.format( 'Daum 실시간 검색어 목록 ' ) )

for index in range( 0, len( top_list ), 2 ):
    print( top_list[ index ].text )