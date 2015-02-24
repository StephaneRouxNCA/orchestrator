import sys
import pprint
from orchestrator.core.flow.Projects import Projects



def main():

    print "This script prints subservices of service"

    print ""
    
    SCRIPT_NAME=sys.argv[0]
    NUM_ARGS_EXPECTED=6

    if (len(sys.argv) - 1 < NUM_ARGS_EXPECTED):
        print "Usage: %s [args]" % SCRIPT_NAME
        print "Args: "
        print "  <KEYSTONE_PROTOCOL>             HTTP or HTTPS"
        print "  <KEYSTONE_HOST>                 Keystone HOSTNAME or IP"
        print "  <KEYSTONE_PORT>                 Keystone PORT"
        print "  <SERVICE_NAME>                  Service name"
        print "  <SERVICE_ADMIN_USER>            Service admin username"
        print "  <SERVICE_ADMIN_PASSWORD>        Service admin password"
        print ""
        print "  Typical usage:"
        print "     %s http           \\" % SCRIPT_NAME
        print "                                 localhost      \\"
        print "                                 5000           \\"
        print "                                 SmartValencia  \\"
        print "                                 adm1           \\"
        print "                                 password       \\"
        print ""
        print "For bug reporting, please contact with:"
        print "<iot_support@tid.es>"
        return

    KEYSTONE_PROTOCOL=sys.argv[1]
    KEYSTONE_HOST=sys.argv[2]
    KEYSTONE_PORT=sys.argv[3]
    SERVICE_NAME=sys.argv[4]
    SERVICE_ADMIN_USER=sys.argv[5]
    SERVICE_ADMIN_PASSWORD=sys.argv[6]

    flow = Projects(KEYSTONE_PROTOCOL,
                            KEYSTONE_HOST,
                            KEYSTONE_PORT)
    
    subservices = flow.projects(None,
                                SERVICE_NAME,
                                SERVICE_ADMIN_USER,
                                SERVICE_ADMIN_PASSWORD,
                                None)
    pprint.pprint(subservices)



if __name__ == '__main__':
    
    main()