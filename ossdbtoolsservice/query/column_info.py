# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List

from ossdbtoolsservice.query.contracts import DbColumn

def get_columns_info(cursor) -> List[DbColumn]:

    if cursor.description is None:
        raise ValueError('Cursor description is not available')

    if cursor.connection is None:
        # if no connection is provided, just return basic column info constructed from the cursor description
        return [DbColumn.from_cursor_description(index, column) for index, column in enumerate(cursor.description)]

    columns_info = []
    for index, column in enumerate(cursor.description):
        db_column = DbColumn.from_cursor_description(index, column)
        db_column.provider = cursor.provider
        columns_info.append(db_column)
    return columns_info
