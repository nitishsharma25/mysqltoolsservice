# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Module containing constants used throughout the service"""

MYSQL_PROVIDER_NAME = 'MySQL'
MARIADB_PROVIDER_NAME = 'MariaDB'
MSSQL_PROVIDER_NAME = 'MSSQL'

SUPPORTED_PROVIDERS = [MYSQL_PROVIDER_NAME, MARIADB_PROVIDER_NAME]

DEFAULT_DB = {
    MYSQL_PROVIDER_NAME: "",
    MARIADB_PROVIDER_NAME: ""
}

DEFAULT_PORT = {
    MYSQL_PROVIDER_NAME: 3306,
    MARIADB_PROVIDER_NAME: 3306
}

# Service names
ADMIN_SERVICE_NAME = 'admin'
CAPABILITIES_SERVICE_NAME = 'capabilities'
CONNECTION_SERVICE_NAME = 'connection'
LANGUAGE_SERVICE_NAME = 'language_service'
METADATA_SERVICE_NAME = 'metadata'
OBJECT_EXPLORER_NAME = 'object_explorer'
QUERY_EXECUTION_SERVICE_NAME = 'query_execution'
SCRIPTING_SERVICE_NAME = 'scripting'
WORKSPACE_SERVICE_NAME = 'workspace'
EDIT_DATA_SERVICE_NAME = 'edit_data'
TASK_SERVICE_NAME = 'tasks'
