from flask import make_response, request

class cookies:
    def set_cookies(ID):
        resp = make_response('set cookies')
        resp.set_cookie('userId', '{}'.format(ID), max_age=3600)
        return resp


def get_cookies():
    userid = request.cookies.get('userId')
    return userid