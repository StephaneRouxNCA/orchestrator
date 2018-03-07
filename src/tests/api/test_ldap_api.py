import uuid
import json
from settings import custom_dev as settings

from test_api import TestRestOperations

LDAP_ADMIN_USER="admin"
LDAP_ADMIN_PASSWORD="4pass1w0rd"

USER_NAME="adm"
USER_PASSWORD="4pass1w0rd"

ORC_PROTOCOL="http"
ORC_HOST="localhost"
ORC_PORT="8084"


class Test_LDAPUser_RestView(object):

    def __init__(self):
        self.suffix = str(uuid.uuid4())[:8]
        self.payload_data_ok = {
            "LDAP_ADMIN_USER": LDAP_ADMIN_USER,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "NEW_USER_NAME": USER_NAME+"_%s" % self.suffix,
            "NEW_USER_PASSWORD": USER_PASSWORD,
            "NEW_USER_EMAIL": USER_NAME+"_%s@acme.org" % self.suffix,
            "NEW_USER_DESCRIPTION": USER_NAME+"_%s description" % self.suffix,
            "GROUP_NAMES": ["SubServiceCustomerGroup"]
        }
        self.payload_data1_ok = {
            "LDAP_ADMIN_USER": LDAP_ADMIN_USER,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "FILTER": "*"+USER_NAME+"_%s*" % self.suffix
        }
        self.payload_data1b_ok = {
            "LDAP_ADMIN_USER": LDAP_ADMIN_USER,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "USER_NAME": USER_NAME+"_%s" % self.suffix
        }
        self.payload_data2_ok = {
            "USER_NAME": USER_NAME+"_%s" % self.suffix,
            "USER_PASSWORD": USER_PASSWORD
        }
        self.suffix = str(uuid.uuid4())[:8]
        self.payload_data4_ok = {
            "NEW_USER_NAME": USER_NAME+"_%s" % self.suffix,
            "NEW_USER_PASSWORD": USER_PASSWORD,
            "NEW_USER_EMAIL": USER_NAME+"_%s@acme.org" % self.suffix,
            "NEW_USER_DESCRIPTION": USER_NAME+"_%s description" % self.suffix,
            "GROUP_NAMES": ["SubServiceCustomerGroup"]
        }
        self.TestRestOps = TestRestOperations(PROTOCOL=ORC_PROTOCOL,
                                              HOST=ORC_HOST,
                                              PORT=ORC_PORT)

    def test_post_ok(self):
        res = self.TestRestOps.rest_request(
            method="POST",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data_ok)
        assert res.code == 201, (res.code, res.msg, res.raw_json)

    def test_get_ok(self):
        res = self.TestRestOps.rest_request(
            method="GET",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data1_ok)
        assert res.code == 200, (res.code, res.msg, res.raw_json)

    def test_get2_ok(self):
        res = self.TestRestOps.rest_request(
            method="GET",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data2_ok)
        assert res.code == 200, (res.code, res.msg, res.raw_json)

    def test_delete_ok(self):
        res = self.TestRestOps.rest_request(
            method="DELETE",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data1b_ok)
        assert res.code == 200, (res.code, res.msg, res.raw_json)

    def test_post2_ok(self):
        res = self.TestRestOps.rest_request(
            method="POST",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data4_ok)
        assert res.code == 201, (res.code, res.msg, res.raw_json)        



class Test_LDAPAuth_RestView(object):

    def __init__(self):
        self.suffix = str(uuid.uuid4())[:8]

        self.payload_data3_ok = {
            "LDAP_ADMIN_USER": LDAP_ADMIN_USER,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "NEW_USER_NAME": USER_NAME+"_%s" % self.suffix,
            "NEW_USER_PASSWORD": USER_PASSWORD,
            "NEW_USER_EMAIL": USER_NAME+"_%s@acme.org" % self.suffix,
            "NEW_USER_DESCRIPTION": USER_NAME+"_%s description" % self.suffix,
            "GROUP_NAMES": ["SubServiceCustomerGroup"],
        }
        self.payload_data3b_ok = {
            "USER_NAME": USER_NAME+"_%s" % self.suffix,
            "USER_PASSWORD": USER_PASSWORD
        }
        self.payload_data3c_ok = {
            "LDAP_ADMIN_USER": LDAP_ADMIN_USER,
            "LDAP_ADMIN_PASSWORD": LDAP_ADMIN_PASSWORD,
            "USER_NAME": USER_NAME+"_%s" % self.suffix
        }
        self.TestRestOps = TestRestOperations(PROTOCOL=ORC_PROTOCOL,
                                              HOST=ORC_HOST,
                                              PORT=ORC_PORT)

    def test_post_and_delete_ok(self):
        res = self.TestRestOps.rest_request(
            method="POST",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data3_ok)
        assert res.code == 201, (res.code, res.msg, res.raw_json)

        res = self.TestRestOps.rest_request(
            method="POST",
            url="/v1.0/ldap/auth",
            json_data=True,
            data=self.payload_data3b_ok)
        assert res.code == 201, (res.code, res.msg, res.raw_json)

        res = self.TestRestOps.rest_request(
            method="DELETE",
            url="/v1.0/ldap/user",
            json_data=True,
            data=self.payload_data3c_ok)
        assert res.code == 200, (res.code, res.msg, res.raw_json)


if __name__ == '__main__':

    # Tests
    test_LdapUser = Test_LDAPUser_RestView()
    test_LdapUser.test_post_ok()
    test_LdapUser.test_get_ok() 
    test_LdapUser.test_get2_ok()
    test_LdapUser.test_delete_ok()
    test_LdapUser.test_post2_ok()

    test_LdapAuth = Test_LDAPAuth_RestView()
    test_LdapAuth.test_post_and_delete_ok()
