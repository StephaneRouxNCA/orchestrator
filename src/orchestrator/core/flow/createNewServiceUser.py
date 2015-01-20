from orchestrator.core.idm import IdMOperations

def createNewServiceUserKeystone(KEYSTONE_PROTOCOL,
                                KEYSTONE_HOST,
                                KEYSTONE_PORT,
                                SERVICE_NAME,
                                SERVICE_ADMIN_USER,
                                SERVICE_ADMIN_PASSWORD,
                                NEW_USER_NAME,
                                NEW_USER_PASSWORD):

    '''Creates a new user Service (aka domain user keystone).

    In case of HTTP error, return HTTP error
    
    Params:
        - KEYSTONE_PROTOCOL: HTTP or HTTPS
        - KEYSTONE_HOST: Keystone HOSTNAME or IP
        - KEYSTONE_PORT: Keystone PORT
        - SERVICE_NAME: Service name
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - NEW_USER_NAME: New user name
        - NEW_USER_PASSWORD: New user password
    '''
    
    ko=IdMOperations(KEYSTONE_PROTOCOL, KEYSTONE_HOST, KEYSTONE_PORT)

    try:
        SERVICE_ADMIN_TOKEN = ko.getToken(SERVICE_NAME, SERVICE_ADMIN_USER,
                                          SERVICE_ADMIN_PASSWORD)
        print "SERVICE_ADMIN_TOKEN=%s" % SERVICE_ADMIN_TOKEN


        #
        # 1. Get service (aka domain)
        #
        ID_DOM1 = ko.getDomain(SERVICE_ADMIN_TOKEN, SERVICE_NAME)

        print "ID of your service %s:%s" % (SERVICE_NAME, ID_DOM1)

        #
        # 2.  Create user 
        #
        ID_USER = ko.createUserDomain(SERVICE_ADMIN_TOKEN, ID_DOM1,
                                      SERVICE_NAME, NEW_USER_NAME, NEW_USER_PASSWORD)
        print "ID of user %s: %s" % (NEW_USER_NAME, ID_USER)


    except Exception, ex:
        print ex
        return ex.message[0]
    
    print "Summary report:"
    print "ID_DOM1=%s" % ID_DOM1
    print "ID_USER=%s" % ID_USER
