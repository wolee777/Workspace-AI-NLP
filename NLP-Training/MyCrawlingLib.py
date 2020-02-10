import requests

'''
    GET 방식 Web Page Response
'''
def getDownload(url, param = None, retries = 3):
    resp = None

    try:
        resp = requests.get( url, params = param )  # , headers = header )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= resp.status_code < 600 and retries > 0:
            print( 'Retries : {0}'.format( retries ) )
            return getDownload( url, param, retries - 1 )
        else:
            print( resp.status_code )
            print( resp.reason )
            print( resp.request.headers )

    return resp

'''
    POST 방식 Web Page Response
'''
def postDownload( url, data = None, param = None, retries = 3 ):
    resp = None

    try:
        resp = requests.post( url, data = data, params = param )  # , headers = header )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= resp.status_code < 600 and retries > 0:
            print( 'Retries : {0}'.format( retries ) )
            return getDownload( url, data, retries - 1 )
        else:
            print( resp.status_code )
            print( resp.reason )
            print( resp.request.headers )

    return resp

'''
    POST 방식 Web Page Response( Cookie data 포함 )
'''
def postDownloadCookie( url, data = None, param = None, cookie = None, retries = 3 ):
    resp = None

    try:
        resp = requests.post( url, data = data, cookies = cookie, params = param )  # , headers = header )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= resp.status_code < 600 and retries > 0:
            print( 'Retries : {0}'.format( retries ) )
            return getDownload( url, data, cookie, retries - 1 )
        else:
            print( resp.status_code )
            print( resp.reason )
            print( resp.request.headers )

    return resp
