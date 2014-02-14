from edudl2.udl2 import message_keys as mk


def select_distinct_asmt_guid_query(schema_name, table_name, column_name, guid_batch):
    return "SELECT DISTINCT {guid_column_name_in_source} FROM {source_schema_and_table} WHERE guid_batch=\'{guid_batch}\'".format(guid_column_name_in_source=column_name,
                                                                                                                                  source_schema_and_table=combine_schema_and_table(schema_name, table_name),
                                                                                                                                  guid_batch=guid_batch)


def select_distinct_asmt_rec_id_query(schema_name, target_table_name, rec_id_column_name, guid_column_name_in_target, guid_column_value):
    return "SELECT DISTINCT {rec_id_column_name} FROM {source_schema_and_table} WHERE {guid_column_name_in_target}=\'{guid_column_value_got}\'".format(rec_id_column_name=rec_id_column_name,
                                                                                                                                                       source_schema_and_table=combine_schema_and_table(schema_name, target_table_name),
                                                                                                                                                       guid_column_name_in_target=guid_column_name_in_target,
                                                                                                                                                       guid_column_value_got=guid_column_value)


def create_insert_query(conf, source_table, target_table, column_mapping, column_types, need_distinct):
    '''
    Main function to create query to insert data from source table to target table
    The query will be executed on the database where target table exists
    Since the source tables and target tables can be existing on different databases/servers,
    dblink is used here to get data from source database in the select clause
    '''
    distinct_expression = 'DISTINCT ' if need_distinct else ''
    seq_expression = list(column_mapping.values())[0].replace("'", "''")

    # TODO:if guid_batch is changed to uuid, need to add quotes around it
    insert_sql = ["INSERT INTO {target_shcema_and_table}(",
                  ",".join(list(column_mapping.keys())),
                  ")  SELECT * FROM dblink(\'host={host} port={port} dbname={db_name} user={db_user} password={db_password}\', \'SELECT {seq_expression}, * FROM (SELECT {distinct_expression}",
                  ",".join(value.replace("'", "''") for value in list(column_mapping.values())[1:]),
                  " FROM {source_schema_and_table} WHERE guid_batch=\'\'{guid_batch}\'\') as y\') AS t(",
                  ",".join(list(column_types.values())),
                  ");"]
    insert_sql = "".join(insert_sql).format(target_shcema_and_table=combine_schema_and_table(conf[mk.TARGET_DB_SCHEMA], target_table),
                                            db_password_target=conf[mk.TARGET_DB_PASSWORD],
                                            target_schema=conf[mk.TARGET_DB_SCHEMA],
                                            host=conf[mk.SOURCE_DB_HOST],
                                            port=conf[mk.SOURCE_DB_PORT],
                                            db_name=conf[mk.SOURCE_DB_NAME],
                                            db_user=conf[mk.SOURCE_DB_USER],
                                            db_password=conf[mk.SOURCE_DB_PASSWORD],
                                            seq_expression=seq_expression,
                                            distinct_expression=distinct_expression,
                                            source_schema_and_table=combine_schema_and_table(conf[mk.SOURCE_DB_SCHEMA], source_table),
                                            guid_batch=conf[mk.GUID_BATCH])

    return insert_sql


def enable_trigger_query(schema_name, table_name, is_enable):
    '''
    Main function to crate a query to disable/enable trigger in table
    @param is_enable: True: enable trigger, False: disbale trigger
    '''
    action = 'ENABLE'
    if not is_enable:
        action = 'DISABLE'
    query = 'ALTER TABLE {schema_name_and_table} {action} TRIGGER ALL'.format(schema_name_and_table=combine_schema_and_table(schema_name, table_name),
                                                                              action=action)
    return query


def update_foreign_rec_id_query(schema, condition_value, info_map):
    '''
    Main function to crate query to update foreign key [foreign]_rec_id in table fact_asmt_outcome
    '''
    update_query = ["UPDATE {schema_and_fact_table} ",
                    "SET {foreign_in_fact}=dim.dim_{foreign_in_dim} FROM (SELECT ",
                    "{foreign_in_dim} AS dim_{foreign_in_dim}, ",
                    ",".join(guid_in_dim + ' AS dim_' + guid_in_dim for guid_in_dim in sorted(list(info_map['guid_column_map'].keys()))),
                    " FROM {schema_and_dim_table}) dim",
                    " WHERE {foreign_in_fact}={fake_value} AND ",
                    " AND ".join(guid_in_fact + '=dim_' + guid_in_dim for guid_in_dim, guid_in_fact in sorted(info_map['guid_column_map'].items()))
                    ]
    update_query = "".join(update_query).format(schema_and_fact_table=combine_schema_and_table(schema, info_map['table_map'][1]),
                                                schema_and_dim_table=combine_schema_and_table(schema, info_map['table_map'][0]),
                                                foreign_in_dim=info_map['rec_id_map'][0],
                                                foreign_in_fact=info_map['rec_id_map'][1],
                                                fake_value=condition_value)
    return update_query


def create_information_query(target_table):
    '''
    Main function to crate query to get column types in a table. 'information_schema.columns' is used.
    '''
    select_query = "SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name=\'{target_table}\'".format(target_table=target_table)
    return select_query


def combine_schema_and_table(schema_name, table_name):
    '''
    Function to create the expression of "schema_name"."table_name"
    '''
    return '\"' + schema_name + '\".\"' + table_name + '\"'


def get_dim_table_mapping_query(schema_name, table_name, phase_number):
    '''
    Function to create the expression of "schema_name"."table_name"
    '''
    return "SELECT distinct target_table, source_table FROM {source_schema_and_table} WHERE phase={phase_number}".format(source_schema_and_table=combine_schema_and_table(schema_name, table_name),
                                                                                                                         phase_number=phase_number)


def get_dim_column_mapping_query(schema_name, table_name, phase_number, dim_table):
    '''
    Function to create the expression of "schema_name"."table_name"
    '''
    return "SELECT distinct target_column, source_column FROM {source_schema_and_table} WHERE target_table='{target_table}'".format(source_schema_and_table=combine_schema_and_table(schema_name, table_name),
                                                                                                                                    target_table=dim_table)