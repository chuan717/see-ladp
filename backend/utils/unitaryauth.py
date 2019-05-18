# -*- coding: utf-8 -*-
import requests

from .ldap_client import LDAPClient


class UnitaryAuth(object):

    def __init__(self):
        self._ldap_client = LDAPClient()

    @property
    def authenticate(self):
        '''
            1. 请求认证接口, 入参：需要根据接口的定义, 一般是 用户名(username), 密码(password)
            2. 接口认证成功，本方法返回True， 失败返回False
            :return: True/False
        '''
        data = self.request.data

        username = data.get('username')
        password = data.get('password')

        return self._do_auth(username, password)

        # '''
        #     请求认证接口, 示例如下:
        # '''
        # auth_data = {
        #     'username':data.get('username'),
        #     'password':data.get('password')
        # }
        #
        # url ='http://127.0.0.1:8090/api/api-token-auth/'
        # res = requests.post(url, json=auth_data)
        # return True if res.ok else False

    def _do_auth(self, username, password):
        return self._ldap_client.check_auth(username, password)