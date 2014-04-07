'''
Created on Nov 8, 2013

@author: dip
'''
import unittest
from smarter.extracts.student_assessment import get_extract_assessment_query
from edcore.utils.utils import compile_query_to_sql_text
from pyramid.testing import DummyRequest
from pyramid import testing
from edcore.tests.utils.unittest_with_edcore_sqlite import Unittest_with_edcore_sqlite,\
    UnittestEdcoreDBConnection, get_unittest_tenant_name
from pyramid.registry import Registry
from smarter.security.roles.default import DefaultRole  # @UnusedImport
from sqlalchemy.sql.expression import select
from edauth.tests.test_helper.create_session import create_test_session
from pyramid.security import Allow
from edauth.security.user import RoleRelation
import edauth
from smarter.security.constants import RolesConstants


class TestStudentAssessment(Unittest_with_edcore_sqlite):

    def setUp(self):
        self.__request = DummyRequest()
        # Must set hook_zca to false to work with uniittest_with_sqlite
        reg = Registry()
        reg.settings = {}
        self.__config = testing.setUp(registry=reg, request=self.__request, hook_zca=False)
        self.__tenant_name = get_unittest_tenant_name()
        defined_roles = [(Allow, RolesConstants.SAR_EXTRACTS, ('view', 'logout'))]
        edauth.set_roles(defined_roles)
        # Set up context security
        dummy_session = create_test_session([RolesConstants.SAR_EXTRACTS])
        dummy_session.set_user_context([RoleRelation(RolesConstants.SAR_EXTRACTS, get_unittest_tenant_name(), "NC", "228", "242")])
        self.__config.testing_securitypolicy(dummy_session.get_user())

    def tearDown(self):
        self.__request = None
        testing.tearDown()

    def test_get_extract_assessment_query(self):
        params = {'stateCode': 'CA',
                  'asmtYear': '2015',
                  'asmtType': 'SUMMATIVE',
                  'asmtSubject': 'Math',
                  'extractType': 'studentAssessment'}
        query = get_extract_assessment_query(params)
        self.assertIsNotNone(query)
        self.assertIn('fact_asmt_outcome.asmt_type', str(query._whereclause))

    def test_get_extract_assessment_query_limit(self):
        params = {'stateCode': 'CA',
                  'asmtYear': '2015',
                  'asmtType': 'SUMMATIVE',
                  'asmtSubject': 'Math',
                  'extractType': 'studentAssessment'}
        query = get_extract_assessment_query(params).limit(541)
        self.assertIsNotNone(query)
        self.assertIn('541', str(query._limit))

    def test_get_extract_assessment_query_compiled(self):
        params = {'stateCode': 'CA',
                  'asmtYear': '2015',
                  'asmtType': 'SUMMATIVE',
                  'asmtSubject': 'Math',
                  'extractType': 'studentAssessment'}
        query = compile_query_to_sql_text(get_extract_assessment_query(params))
        self.assertIsNotNone(query)
        self.assertIsInstance(query, str)
        self.assertIn('SUMMATIVE', query)

    def test_compile_query_to_sql_text(self):
        with UnittestEdcoreDBConnection() as connection:
            fact = connection.get_table('fact_asmt_outcome')
            query = select([fact.c.state_code], from_obj=[fact])
            query = query.where(fact.c.state_code == 'UT')
            str_query = compile_query_to_sql_text(query)
            self.assertIn("fact_asmt_outcome.state_code = 'UT'", str_query)

    def test_get_extract_assessment_query_results(self):
        params = {'stateCode': 'NC',
                  'asmtYear': '2015',
                  'asmtType': 'SUMMATIVE',
                  'asmtSubject': 'Math',
                  'asmt_grade': '3'}
        query = get_extract_assessment_query(params)
        self.assertIsNotNone(query)
        with UnittestEdcoreDBConnection() as connection:
            results = connection.get_result(query)
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        # Check for columns are in results
        self.assertIn('acc_streamline_mode', results[0])
        self.assertIn('acc_asl_human_nonembed', results[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
