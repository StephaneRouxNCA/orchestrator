from orchestrator.core.idm import IdMOperations

def createNewServiceRoleKeystone(KEYSTONE_PROTOCOL,
                                 KEYSTONE_HOST,
                                 KEYSTONE_PORT,
                                 SERVICE_NAME,
                                 SERVICE_ADMIN_USER,
                                 SERVICE_ADMIN_PASSWORD,
                                 NEW_ROLE_NAME):

    '''Creates a new role Service (aka domain role keystone).

    In case of HTTP error, return HTTP error
    
    Params:
        - KEYSTONE_PROTOCOL: HTTP or HTTPS
        - KEYSTONE_HOST: Keystone HOSTNAME or IP
        - KEYSTONE_PORT: Keystone PORT
        - SERVICE_NAME: Service name
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - NEW_ROLE_NAME: New role name
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
        # 2.  Create role
        #
        ID_ROLE = ko.createRoleDomain(SERVICE_ADMIN_TOKEN, ID_DOM1,
                                      NEW_ROLE_NAME)
        print "ID of user %s: %s" % (NEW_ROLE_NAME, ID_ROLE)


    except Exception, ex:
        print ex
        return ex.message[0]
    
    print "Summary report:"
    print "ID_DOM1=%s" % ID_DOM1
    print "ID_ROLE=%s" % ID_ROLE
