'''
Several methods are provided to create/drop tables/sequences/extensions/foreign data wrapper servers
in postgres database.

Main Method: setup_udl2_schema(conf)
Main method: teardown_udl2_schema(conf)

Created on May 10, 2013

@author: ejen
'''
from sqlalchemy.schema import CreateSequence, DropSequence, DropTable, DropSchema
import argparse
from config import ref_table_data, sr_ref_table_data
from edudl2.udl2_util.config_reader import read_ini_file
from edudl2.udl2.defaults import UDL2_DEFAULT_CONFIG_PATH_FILE
from edudl2.database.metadata.udl2_metadata import generate_udl2_sequences
from edudl2.database.udl2_connector import get_target_connection, initialize_db_udl,\
    initialize_db_target,\
    get_udl_connection
from edudl2.database.populate_ref_info import populate_ref_column_map,\
    populate_stored_proc
from sqlalchemy.sql.expression import text


def _parse_args():
    '''
    private method to parse command line options when call from shell. We use it to setup/teardown database
    automatically by configuration (this helps jenkins/Continous Integration)
    '''
    parser = argparse.ArgumentParser('database')
    parser.add_argument('--config_file', dest='config_file',
                        help="full path to configuration file for UDL2, default is /opt/wgen/edware-udl/etc/udl2_conf.py")
    parser.add_argument('--action', dest='action', required=False,
                        help="'setup' for setting up udl2 database. " +
                             "'teardown' for tear down udl2 database")
    args = parser.parse_args()
    return (parser, args)


def drop_schema(schema_name):
    '''
    drop schemas according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    with get_udl_connection() as conn:
        conn.execute(DropSchema(schema_name, cascade=True))


def drop_tables():
    '''
    drop tables according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print("drop tables")
    try:
        with get_udl_connection() as conn:
            metadata = conn.get_metadata()
            for table in reversed(metadata.sorted_tables):
                conn.execute(DropTable(table))
    except Exception as e:
        print("Error happens when tearing down tables: " + e)


def create_udl2_sequence(schema_name):
    '''
    create sequences according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print("create sequences")
    with get_udl_connection() as conn:
        metadata = conn.get_metadata()
        for sequence in generate_udl2_sequences(schema_name, metadata):
            conn.execute(CreateSequence(sequence))


def drop_udl2_sequences():
    '''
    drop sequences according to configuration file
    '''
    try:
        print("drop sequences")
        with get_udl_connection() as conn:
            for seq in generate_udl2_sequences():
                conn.execute(DropSequence(seq))
    except Exception as e:
        print("Error occurs when tearing down sequence: " + e)


def create_foreign_data_wrapper_extension(schema_name):
    '''
    create foreign data wrapper extension according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print('create foreign data wrapper extension')
    with get_udl_connection() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS file_fdw"))


def drop_foreign_data_wrapper_extension():
    '''
    drop foreign data wrapper extension according to configuration file
    '''
    print('drop foreign data wrapper extension')
    with get_udl_connection() as conn:
        conn.execute(text("DROP EXTENSION IF EXISTS file_fdw CASCADE"))


def create_dblink_extension(cls):
    '''
    create dblink extension according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print('create dblink extension')
    with cls() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS dblink"))


def drop_dblink_extension(cls):
    '''
    drop dblink extension according to configuration file
    '''
    print('drop dblink extension')
    with cls() as conn:
        conn.execute(text("DROP EXTENSION IF EXISTS dblink CASCADE"))


def create_foreign_data_wrapper_server(fdw_server):
    '''
    create server for foreign data wrapper according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print('create foreign data wrapper server')
    with get_udl_connection() as conn:
        conn.execute(text("CREATE SERVER %s FOREIGN DATA WRAPPER file_fdw" % (fdw_server)))


def drop_foreign_data_wrapper_server(fdw_server):
    '''
    drop server for foreign data wrapper according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    print('drop foreign data wrapper server')
    with get_udl_connection() as conn:
        conn.execute(text("DROP SERVER IF EXISTS %s CASCADE" % (fdw_server)))


def load_reference_data(udl2_conf):
    '''
    load the reference data into the reference tables
    @param udl2_conf: The configuration dictionary for
    '''
    asmt_ref_table_info = ref_table_data.ref_table_conf
    populate_ref_column_map(asmt_ref_table_info, udl2_conf['ref_tables']['assessment'])

    sr_ref_table_info = sr_ref_table_data.ref_table_conf
    populate_ref_column_map(sr_ref_table_info, udl2_conf['ref_tables']['studentregistration'])


def load_stored_proc(udl2_conf):
    '''
    Generate and load the stored procedures to be used for transformations and
    validations into the database.
    @param udl2_conf: The configuration dictionary for
    '''
    populate_stored_proc(udl2_conf['ref_tables']['assessment'], udl2_conf['ref_tables']['studentregistration'])


def setup_udl2_schema(udl2_conf):
    '''
    create whole udl2 database schema according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    # Setup udl2 schema
    initialize_db_udl(udl2_conf, allow_create_schema=True)
    udl2_schema_name = udl2_conf['udl2_db']['db_schema']
    create_udl2_sequence(udl2_schema_name)
    create_dblink_extension(get_udl_connection)
    create_foreign_data_wrapper_extension(udl2_schema_name)
    create_foreign_data_wrapper_server(udl2_conf['udl2_db']['fdw_server'])

    # Create dblink in pre-prod database
    initialize_db_target(udl2_conf)
    create_dblink_extension(get_target_connection)

    # load data and stored procedures into udl tables
    load_reference_data(udl2_conf['udl2_db'])
    load_stored_proc(udl2_conf['udl2_db'])


def teardown_udl2_schema(udl2_conf):
    '''
    drop whole udl2 database schema according to configuration file
    @param udl2_conf: The configuration dictionary for
    '''
    # Tear down udl2 schema
    initialize_db_udl(udl2_conf)
    drop_udl2_sequences()
    drop_tables()
    drop_foreign_data_wrapper_server(udl2_conf['udl2_db']['fdw_server'])
    drop_foreign_data_wrapper_extension()
    drop_dblink_extension(get_udl_connection)
    drop_schema(udl2_conf['udl2_db']['db_schema'])

    # Drop dblink in pre-prod
    initialize_db_target(udl2_conf)
    drop_dblink_extension(get_target_connection)


def main():
    '''
    create or drop udl2 database objects according to command line.
    The purpose for this script is to enable clean up whole database artifacts or create
    whole database artifacts without problem. Since UDL uses databases to clean data. Database object
    in UDL can be dropped or recreated at will for changes. So we can verifiy system
    '''
    (parser, args) = _parse_args()
    if args.config_file is None:
        config_path_file = UDL2_DEFAULT_CONFIG_PATH_FILE
    else:
        config_path_file = args.config_file
    conf_tup = read_ini_file(config_path_file)
    udl2_conf = conf_tup[0]

    if args.action is None:
        parser.print_help()
        return
    if args.action == 'setup':
        setup_udl2_schema(udl2_conf)
    elif args.action == 'teardown':
        teardown_udl2_schema(udl2_conf)

if __name__ == '__main__':
    main()