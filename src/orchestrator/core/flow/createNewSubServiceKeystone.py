from orchestrator.core.idm import IdMOperations

def createNewSubServiceKeystone(KEYSTONE_PROTOCOL,
                                KEYSTONE_HOST,
                                KEYSTONE_PORT,
                                SERVICE_NAME,
                                SERVICE_ADMIN_USER,
                                SERVICE_ADMIN_PASSWORD,
                                NEW_SUBSERVICE_NAME,
                                NEW_SUBSERVICE_DESCRIPTION):

    '''Creates a new SubService (aka project keystone).

    In case of HTTP error, return HTTP error
    
    Params:
        - KEYSTONE_PROTOCOL: HTTP or HTTPS
        - KEYSTONE_HOST: Keystone HOSTNAME or IP
        - KEYSTONE_PORT: Keystone PORT
        - SERVICE_NAME: Service name
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - SUBSERVICE_NAME: New subservice name
        - SUBSERVICE_DESCRIPTION: New subservice description
    '''
    
    #SUB_SERVICE_ADMIN_ROLE_NAME="SubServiceAdmin"
    #SUB_SERVICE_CUSTOMER_ROLE_NAME="SubServiceCustomer"

    ko=IdMOperations(KEYSTONE_PROTOCOL, KEYSTONE_HOST, KEYSTONE_PORT)

    try:
        SERVICE_ADMIN_TOKEN = ko.getToken(SERVICE_NAME, SERVICE_ADMIN_USER,
                                          SERVICE_ADMIN_PASSWORD)
        print "SERVICE_ADMIN_TOKEN=%s" % SERVICE_ADMIN_TOKEN


        #
        # 1. Create service (aka domain)
        #
        ID_DOM1 = ko.getDomain(SERVICE_ADMIN_TOKEN, SERVICE_NAME)

        print "ID of your service %s:%s" % (SERVICE_NAME, ID_DOM1)

        #
        # 2.  Create subservice (aka project)
        #
        ID_PRO1 = ko.createProject(SERVICE_ADMIN_TOKEN, ID_DOM1,
                                   NEW_SUBSERVICE_NAME, NEW_SUBSERVICE_DESCRIPTION)
        print "ID of user %s: %s" % (NEW_SUBSERVICE_NAME, ID_PRO1)


    except Exception, ex:
        print ex
        return ex.message[0]
    
    print "Summary report:"
    print "ID_DOM1=%s" % ID_DOM1
    print "SERVICE_ADMIN_TOKEN=%s" % SERVICE_ADMIN_TOKEN
