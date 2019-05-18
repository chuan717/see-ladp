import ldap3
import logging

from django.conf.LDAP_SETTINGS import LDAP_SETTINGS


class LDAPClient:

    def __init__(self):
        self.ldap_server = LDAP_SETTINGS.['SERVER']
        self.bind_user = LDAP_SETTINGS['BIND_USER']
        self.bind_password = LDAP_SETTINGS['BIND_PASSWORD']
        self.ldap_domain = LDAP_SETTINGS['BIND_DOMAIN']
        self.base_dn = LDAP_SETTINGS['BASE_DN']
        self.ldap_port = LDAP_SETTINGS['PORT']

    def ldap_bind(self):
        """ Establish ldap connection """

        bind_upn = "{}@{}".format(self.bind_user, self.ldap_domain)

        server = ldap3.Server(host=self.ldap_server, port=self.ldap_port, use_ssl=False, get_info='ALL')

        conn = ldap3.Connection(server, user=bind_upn, password=self.bind_password, auto_bind='NONE', version=3,
                                authentication='SIMPLE', client_strategy='SYNC', auto_referrals=False,
                                check_names=True, read_only=True, lazy=False, raise_exceptions=False)

        if not conn.bind():
            logging.error("ldap_bind: Bind error occurred: {}".format(conn.result))
            return False

        return conn

    def check_auth(self, username, password):
        """ Bind with user credentials to verify username and password """

        if password is not "":

            upn = "{}@{}".format(username, self.ldap_domain)

            server = ldap3.Server(host=self.ldap_server, port=self.ldap_port, use_ssl=False, get_info='ALL')

            conn = ldap3.Connection(server, user=upn, password=password, auto_bind='NONE', version=3,
                                    authentication='SIMPLE', client_strategy='SYNC', auto_referrals=False,
                                    check_names=True, read_only=True, lazy=False, raise_exceptions=False)

            if conn.bind():
                return True
            else:
                return False

        return False

