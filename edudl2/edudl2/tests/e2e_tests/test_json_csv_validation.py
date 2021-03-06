# (c) 2014 Amplify Education, Inc. All rights reserved, subject to the license
# below.
#
# Education agencies that are members of the Smarter Balanced Assessment
# Consortium as of August 1, 2014 are granted a worldwide, non-exclusive, fully
# paid-up, royalty-free, perpetual license, to access, use, execute, reproduce,
# display, distribute, perform and create derivative works of the software
# included in the Reporting Platform, including the source code to such software.
# This license includes the right to grant sublicenses by such consortium members
# to third party vendors solely for the purpose of performing services on behalf
# of such consortium member educational agencies.

'''
Created on Oct 28, 2013
@author: bpatel
'''
## This test verify in case of corrupted json and csv ,
## udl fails and error has been captured in UDL_BATCH table.
## also verify that post udl has been successful.

import unittest
import os
import subprocess
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler
from uuid import uuid4
from time import sleep
from multiprocessing import Process
from edudl2.database.udl2_connector import get_udl_connection
from sqlalchemy.sql.expression import and_, select
from edudl2.udl2.constants import Constants
from edudl2.tests.e2e_tests import UDLE2ETestCase


FACT_TABLE = 'fact_asmt_outcome_vw'


class ValidateTableData(UDLE2ETestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.udl_connector = get_udl_connection()
        self.tenant_dir = '/opt/edware/zones/landing/arrivals/cat/test_user/filedrop/'
        here = os.path.dirname(__file__)
        self.driver_path = os.path.join(here, "..", "..", "..", "scripts", "driver.py")

    @classmethod
    def teardownClass(self):
        self.udl_connector.close_connection()
        if os.path.exists(self.tenant_dir):
            shutil.rmtree(self.tenant_dir)

    #Run the UDL with specified file
    def run_udl_with_file(self, guid_batch, file_to_load):
        arch_file = self.copy_file_to_tmp(file_to_load)
        command = "python {driver_path} -a {file_path} -g {guid}".format(driver_path=self.driver_path, file_path=arch_file, guid=self.guid_batch_id)
        subprocess.call(command, shell=True)
        self.check_job_completion(self.udl_connector, guid_batch)

    #Check the batch table periodically for completion of the UDL pipeline, waiting up to max_wait seconds
    def check_job_completion(self, connector, guid_batch_id, max_wait=60):
        batch_table = connector.get_table(Constants.UDL2_BATCH_TABLE)
        query = select([batch_table.c.udl_phase], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'UDL_COMPLETE'))
        timer = 0
        result = connector.execute(query).fetchall()
        while timer < max_wait and not result:
            sleep(0.25)
            timer += 0.25
            result = connector.execute(query).fetchall()

    #copy files to tenant directory
    def copy_file_to_tmp(self, file_to_copy):
        # create tenant dir if not exists
        if not os.path.exists(self.tenant_dir):
            os.makedirs(self.tenant_dir)
        return shutil.copy2(file_to_copy, self.tenant_dir)

    #In UDL_Batch Table,After each udl run verify that UDL_Complete task is Failure and Post_udl cleanup task is successful
    def verify_udl_failure(self, udl_connector, guid_batch_id):
        status = [('FAILURE',)]
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        query = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'UDL_COMPLETE'))
        query2 = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_post_etl.task'))
        batch_table_data = udl_connector.execute(query).fetchall()
        batch_table_post_udl = udl_connector.execute(query2).fetchall()
        self.assertEquals(status, batch_table_data)
        self.assertEquals([('SUCCESS',)], batch_table_post_udl)

    #verify that with different asmt_guid in jsona nd csv lead to UDL pipeline failure with valid exception
    def verify_asmt_guid(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        batch_table_status = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_file_content_validator.task'))
        batch_data_tasklevel = udl_connector.execute(batch_table_status).fetchall()
        self.assertEquals([('FAILURE',)], batch_data_tasklevel)

    #Verify that udl is failing due to corrcet task failure.For i.e if json is missing udl should fail due to missing file at file expander task
    def verify_missing_json(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        batch_table_status = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_file_expander.task'))
        batch_data_tasklevel = udl_connector.execute(batch_table_status).fetchall()
        self.assertEquals([('FAILURE',)], batch_data_tasklevel)

    #Verify that UDL is failing at Decription task
    def verify_corrupt_source(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        batch_table_status = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_file_decrypter.task'))
        batch_data_tasklevel = udl_connector.execute(batch_table_status).fetchall()
        self.assertEquals([('FAILURE',)], batch_data_tasklevel)

    #Verify udl is failing at simple file validator
    def verify_corrupt_csv(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        batch_table_status = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_file_validator.task'))
        batch_data_corrupt_csv = udl_connector.execute(batch_table_status).fetchall()
        self.assertEquals([('FAILURE',)], batch_data_corrupt_csv)

    #Verify udl is failing at get load type
    def verify_invalid_load(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        batch_table_status = select([batch_table.c.udl_phase_step_status], and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'udl2.W_get_load_type.task'))
        batch_data_invalid_load = udl_connector.execute(batch_table_status).fetchall()
        self.assertEquals([('FAILURE',)], batch_data_invalid_load)

    #Validate that the notification to the callback url was successful
    def verify_notification_success(self, udl_connector, guid_batch_id):
        batch_table = udl_connector.get_table(Constants.UDL2_BATCH_TABLE)
        query = select([batch_table.c.udl_phase_step_status],
                       and_(batch_table.c.guid_batch == guid_batch_id, batch_table.c.udl_phase == 'UDL_JOB_STATUS_NOTIFICATION'))
        result = udl_connector.execute(query).fetchall()
        for row in result:
            notification_status = row['udl_phase_step_status']
            self.assertEqual('SUCCESS', notification_status)

    def test_run_udl_corrupt_guid(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_gpg_file('test_asmt_guid_validation')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
        self.verify_asmt_guid(self.udl_connector, self.guid_batch_id)

    def test_run_udl_ext_col_csv(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_file('corrupt_csv_ext_col.tar.gz.gpz')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
        self.verify_corrupt_csv(self.udl_connector, self.guid_batch_id)

    def test_run_udl_miss_csv(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_file('corrupt_csv_ext_col.tar.gz.gpz')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)

    def test_run_udl_corrupt_json(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_file('corrupt_json.tar.gz.gpz')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)

    def test_run_udl_corrupt_source(self):
        self.guid_batch_id = str(uuid4())
        corrupt_file = self.require_file('test_corrupted_source_file_tar_gzipped.tar.gz.gpg')
        self.run_udl_with_file(self.guid_batch_id, corrupt_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
        self.verify_corrupt_source(self.udl_connector, self.guid_batch_id)

    def test_run_udl_missing_json(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_gpg_file('test_missing_json_file')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
        self.verify_missing_json(self.udl_connector, self.guid_batch_id)

    def test_run_udl_invalid_load_json(self):
        self.guid_batch_id = str(uuid4())
        gpg_file = self.require_gpg_file('test_invalid_load_json_file_tar_gzipped')
        self.run_udl_with_file(self.guid_batch_id, gpg_file)
        self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
        self.verify_invalid_load(self.udl_connector, self.guid_batch_id)

    def test_run_udl_sr_csv_missing_column(self):
        self.guid_batch_id = str(uuid4())
        sr_data = self.require_gpg_file('test_sr_csv_missing_column')

        # Start the http post server subprocess
        self.start_post_server()

        try:
            self.run_udl_with_file(self.guid_batch_id, sr_data)
            self.verify_udl_failure(self.udl_connector, self.guid_batch_id)
            self.verify_corrupt_csv(self.udl_connector, self.guid_batch_id)
            self.verify_notification_success(self.udl_connector, self.guid_batch_id)
        except Exception:
            self.shutdown_post_server()
            raise

        # End the http post server subprocess
        self.shutdown_post_server()

    def start_post_server(self):
        self.receive_requests = True
        try:
            self.proc = Process(target=self.run_post_server)
            self.proc.start()
        except Exception:
            pass

    def run_post_server(self):
        try:
            server_address = ('127.0.0.1', 50472)
            self.post_server = HTTPServer(server_address, HTTPPOSTHandler)
            self.post_server.timeout = 0.25
            while self.receive_requests:
                self.post_server.handle_request()
        finally:
            print('POST Service stop receiving requests.')

    def shutdown_post_server(self):
        try:
            self.receive_requests = False
            sleep(0.5)  # Give server time to stop listening
            self.proc.terminate()
            self.post_server.shutdown()
        except Exception:
            pass


# This class handles our HTTP POST requests with success responses
class HTTPPOSTHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(201)
        self.end_headers()

    def log_message(self, format, *args):
        return


if __name__ == '__main__':
    unittest.main()
