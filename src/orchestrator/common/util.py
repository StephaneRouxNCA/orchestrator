import urllib2
import base64
import json



class RestOperations(object):
    '''
       IoT IdM (keystone + keypass)
    '''

    def __init__(self,
                 KEYSTONE_PROTOCOL=None,
                 KEYSTONE_HOST=None,
                 KEYSTONE_PORT=None,
                 KEYPASS_PROTOCOL=None,
                 KEYPASS_HOST=None,
                 KEYPASS_PORT=None
             ):

        self.KEYSTONE_PROTOCOL=KEYSTONE_PROTOCOL
        self.KEYSTONE_HOST=KEYSTONE_HOST
        self.KEYSTONE_PORT=KEYSTONE_PORT
        self.KEYPASS_PROTOCOL=KEYPASS_PROTOCOL
        self.KEYPASS_HOST=KEYPASS_HOST
        self.KEYPASS_PORT=KEYPASS_PORT
        if KEYSTONE_PROTOCOL and KEYSTONE_HOST and KEYSTONE_PORT:
            self.base_url = KEYSTONE_PROTOCOL+'://'+KEYSTONE_HOST+':'+KEYSTONE_PORT+'/'


    def rest_request(self, url, method, user=None, password=None,
                     data=None, json_data=True, relative_url=True,
                     auth_token=None, fiware_service=None):
        '''Does an (optionally) authorized REST request with optional JSON data.

        In case of HTTP error, the exception is returned normally instead of
        raised and, if JSON error data is present in the response, .msg will
        contain the error detail.'''
        user = user or None
        password = password or None

        if relative_url:
            # Create real url
            url = self.base_url + url

        if data:
            if json_data:
                request = urllib2.Request(
                    url, data=json.dumps(data))
            else:
                request = urllib2.Request(url, data=data)
        else:
            request = urllib2.Request(url)
        request.get_method = lambda: method

        if json_data:
            request.add_header('Accept', 'application/json')
            request.add_header('Content-Type', 'application/json')
        else:
            request.add_header('Accept', 'application/xml')
            request.add_header('Content-Type', 'application/xml')

        if user and password:
            base64string = base64.encodestring(
            '%s:%s' % (user, password))[:-1]
            authheader = "Basic %s" % base64string
            request.add_header("Authorization", authheader)

        if auth_token:
            request.add_header('X-Auth-Token', auth_token)

        if fiware_service:
            request.add_header('Fiware-Service', fiware_service)

        res = None

        try:
            res = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            res = e
            data = res.read()
            try:
                data_json = json.loads(data)
                res.raw_json = data_json
                if data_json and 'detail' in data_json:
                    res.msg = data_json['detail']
            except ValueError:
                res.msg = data
            except Exception, e:
                print e

        return res
