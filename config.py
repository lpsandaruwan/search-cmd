"""
Contains configurations for searchable models
"""

MODELS = [
    {
        "model": "user",
        "index": 1,
        "display_name": "Users",
        "init_data_file": "JsonStore/users.json",
        "query_db_file": "db/users.json",
        "data_reset_on_startup": True,
        "fields": {
            "_id": "int",
            "url": "string",
            "external_id": "string",
            "name": "string",
            "alias": "string",
            "created_at": "string",
            "active": "string",
            "verified": "string",
            "shared": "string",
            "locale": "string",
            "timezone": "string",
            "last_login_at": "string",
            "email": "string",
            "phone": "string",
            "signature": "string",
            "organization_id": "int",
            "tags": "list",
            "suspended": "bool",
            "role": "string"
        },
        "printable_fields": ["external_id", "name", "alias", "created_at", "active", "verified", "shared",
                             "locale", "timezone", "last_login_at", "email", "phone", "signature", "organization_id",
                             "tags", "suspended", "role"]
    },
    {
        "model": "ticket",
        "index": 2,
        "display_name": "Tickets",
        "init_data_file": "JsonStore/tickets.json",
        "query_db_file": "db/tickets.json",
        "data_reset_on_startup": True,
        "fields": {
            "_id": "string",
            "url": "string",
            "external_id": "string",
            "created_at": "string",
            "type": "string",
            "subject": "string",
            "description": "string",
            "priority": "string",
            "status": "string",
            "submitter_id": "int",
            "assignee_id": "int",
            "organization_id": "int",
            "tags": "list",
            "has_incidents": "bool",
            "due_at": "string",
            "via": "string"
        },
        "printable_fields": ["created_at", "type", "subject", "description", "priority", "status", "submitter_id",
                             "assignee_id", "organization_id", "tags", "has_incidents", "due_at", "via"]
    },
    {
        "model": "organization",
        "index": 3,
        "display_name": "Organizations",
        "init_data_file": "JsonStore/organizations.json",
        "query_db_file": "db/organizations.json",
        "data_reset_on_startup": True,
        "fields": {
            "_id": "int",
            "url": "string",
            "external_id": "string",
            "name": "string",
            "domain_names": "list",
            "created_at": "string",
            "details": "string",
            "shared_tickets": "bool",
            "tags": "list"
        },
        "printable_fields": ["external_id", "name", "domain_names", "list", "created_at", "details", "shared_tickets",
                             "tags"]
    },
]
