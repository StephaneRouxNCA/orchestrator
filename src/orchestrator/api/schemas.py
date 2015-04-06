json = {
    ###############
    "ServiceCreate": {
    ###############
        "name": "Service",
        "dependencies": {
            "DOMAIN_NAME": [
                "DOMAIN_ADMIN_USER",
                "DOMAIN_ADMIN_PASSWORD"
            ],
            "DOMAIN_ADMIN_USER": [
                "DOMAIN_NAME",
                "DOMAIN_ADMIN_PASSWORD"
            ],
            "DOMAIN_ADMIN_PASSWORD": [
                "DOMAIN_ADMIN_USER",
                "DOMAIN_NAME"
            ]
        },
        "properties": {
            "DOMAIN_NAME": {
                "type": "string",
            },
            "DOMAIN_ADMIN_USER": {
                "type": "string",
            },
            "DOMAIN_ADMIN_PASSWORD": {
                "type": "string",
            },
            "DOMAIN_ADMIN_TOKEN": {
                "type": "string",
            },
            "NEW_SERVICE_NAME": {
                "type": "string",
                "maxLength": 50,
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "NEW_SERVICE_DESCRIPTION": {
                "type": "string",
            },
            "NEW_SERVICE_ADMIN_USER": {
                "type": "string",
                "maxLength": 50,
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "NEW_SERVICE_ADMIN_PASSWORD": {
                "type": "string",
                "minLength": 6,
            },
            "NEW_SERVICE_ADMIN_EMAIL": {
                "type": "string",
                "pattern": "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
            },
        },
        # "oneof": {
        #     "required": [
        #         "NEW_SERVICE_NAME",
        #         "NEW_SERVICE_ADMIN_USER",
        #         "NEW_SERVICE_ADMIN_PASSWORD",
        #         "DOMAIN_ADMIN_USER"],
        #     "required": [
        #         "NEW_SERVICE_NAME",
        #         "NEW_SERVICE_ADMIN_USER",
        #         "NEW_SERVICE_ADMIN_PASSWORD",
        #         "DOMAIN_ADMIN_TOKEN"],
        # }
        "required": [
                "NEW_SERVICE_NAME",
                "NEW_SERVICE_ADMIN_USER",
                "NEW_SERVICE_ADMIN_PASSWORD"
        ]
    },
    #############
    "ServiceList": {
    #############
        "name": "ServiceList",
        "dependencies": {
            "DOMAIN_ADMIN_USER": [
                "DOMAIN_ADMIN_PASSWORD"
            ],
            "DOMAIN_ADMIN_PASSWORD": [
                "DOMAIN_ADMIN_USER",
            ]
        },
        "properties": {
            "DOMAIN_NAME": {
                "type": "string",
            },
            "DOMAIN_ADMIN_USER": {
                "type": "string",
            },
            "DOMAIN_ADMIN_PASSWORD": {
                "type": "string",
            },
            "DOMAIN_ADMIN_TOKEN": {
                "type": "string",
            },
            "DOMAIN_ID": {
                "type": "string",
            },
        },
        #"required": [ ],
    },
    ################
    "SubServiceList": {
    ################
        "name": "SubServiceList",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SUBSERVICE_ID": {
                "type": "string",
            },
        },
        #"required": [ ],
    },
    #################
    "SubServiceCreate": {
    #################
        "name": "SubServiceCreate",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "NEW_SUBSERVICE_NAME": {
                "type": "string",
                "maxLength": 50,
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "NEW_SUBSERVICE_DESCRIPTION": {
                "type": "string",
            },
        },
        "required": [
            "NEW_SUBSERVICE_NAME"
        ],
    },
    #######
    "User": {
    #######
        "name": "User",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "USER_NAME": {
                "type": "string",
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "USER_ID": {
                "type": "string",
            },
            "USER_DATA_VALUE": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "pattern": "^([A-Za-z0-9_]+)$",
                        },
                    "password": {
                        "type": "string",
                        "minLength": 6,
                        },
                    "emails": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "value": {
                                    "type": "string",
                                    "pattern": "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
                                    },
                                }
                            },
                        "maxItems": 4
                        },
                    },
                "additionalProperties": False,
                #"required": ["user", "emails"]
            },
        },
        #"required": [ ],
    },
    ##########
    "UserList": {
    ##########
        "name": "UserList",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ],
            "NEW_SERVICE_USER_NAME": [
                "NEW_SERVICE_USER_PASSWORD"
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "NEW_SERVICE_USER_NAME": {
                "type": "string",
                "maxLength": 50,
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "NEW_SERVICE_USER_PASSWORD":{
                "type": "string",
                "minLength": 6,
            },
            "NEW_SERVICE_USER_EMAIL":{
                "type": "string",
                "pattern": "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
            },
        },
        #"required": [ ],
    },
    #######
    "Role": {
    #######
        "name": "Role",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "NEW_ROLE_NAME": {
                "type": "string",
                "maxLength": 50,
                "pattern": "^([A-Za-z0-9_]+)$",
            },
            "XACML_POLICY": {
                "type": "string",
            },
        },
        "required": [
            "NEW_ROLE_NAME"
        ],
    },
    ####################
    "RoleAssignmentList": {
    ####################
        "name": "RoleAssignmentList",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SUBSERVICE_ID": {
                "type": "string",
            },
            "USER_ID": {
                "type": "string",
            },
        },
    },
    #############
    "AssignRole": {
    #############
        "name": "AssignRole",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "SERVICE_USER_NAME": {
                "type": "string",
            },
            "SERVICE_USER_ID": {
                "type": "string",
            },
            "SUBSERVICE_NAME": {
                "type": "string",
            },
            "SUBSERVICE_ID": {
                "type": "string",
            },
            "ROLE_NAME": {
                "type": "string",
            },
            "ROLE_ID": {
                "type": "string",
            },
        },
        "required": [
            "ROLE_NAME",
            "SERVICE_USER_NAME"
        ],
    },

    ########
    "Trust": {
    ########
        "name": "Trust",
        "dependencies": {
            "SERVICE_ADMIN_USER": [
                "SERVICE_ADMIN_PASSWORD"
            ],
            "SERVICE_ADMIN_PASSWORD": [
                "SERVICE_ADMIN_USER",
            ]
        },
        "properties": {
            "SERVICE_ADMIN_USER": {
                "type": "string",
            },
            "SERVICE_ADMIN_PASSWORD": {
                "type": "string",
            },
            "SERVICE_ADMIN_TOKEN": {
                "type": "string",
            },
            "SERVICE_ID": {
                "type": "string",
            },
            "SERVICE_NAME": {
                "type": "string",
            },
            "SUBSERVICE_ID": {
                "type": "string",
            },
            "SUBSERVICE_NAME": {
                "type": "string",
            },
            "ROLE_NAME": {
                "type": "string",
            },
            "ROLE_ID": {
                "type": "string",
            },
            "TRUSTEE_USER_NAME": {
                "type": "string",
            },
            "TRUSTEE_USER__ID": {
                "type": "string",
            },
            "TRUSTOR_USER_NAME": {
                "type": "string",
            },
            "TRUSTOR_USER__ID": {
                "type": "string",
            },
        },
        #"required": [
        #],
    },

}

# The JSON Schema above can be used to test the validity of the JSON code below:
example_data = {
    "DOMAIN_NAME": "admin_domain",
    "DOMAIN_ADMIN_USER": "cloud_admin",
    "DOMAIN_ADMIN_PASSWORD": "password",
    "DOMAIN_ADMIN_TOKEN": "",
    "NEW_SERVICE_NAME": "SmartValencia",
    "NEW_SERVICE_DESCRIPTION": "SmartValencia city",
    "NEW_SERVICE_ADMIN_USER": "adm1",
    "NEW_SERVICE_ADMIN_PASSWORD": "password",
}
