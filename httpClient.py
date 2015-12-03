import httplib


def httpRequest(method, route):
    conn = httplib.HTTPConnection('46.101.181.25', '5000')
    conn.request(method, route)
    response = conn.getresponse()
