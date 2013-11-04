'''
Created on Jul 16, 2013

@author: tosako
'''
import unittest
from sqlalchemy.sql.expression import true, false, null, select
from smarter.reports.helpers.filters import _get_filter,\
    has_filters, apply_filter_to_query, FILTERS_PROGRAM_IEP, FILTERS_GENDER,\
    FILTERS_GENDER_FEMALE, FILTERS_ETHNICITY, FILTERS_ETHNICITY_MULTI,\
    FILTERS_GENDER_MALE, FILTERS_ETHNICITY_AMERICAN, FILTERS_PROGRAM_TT1,\
    FILTERS_PROGRAM_504, FILTERS_PROGRAM_LEP, FILTERS_GRADE, YES, NOT_STATED, NO
from edcore.tests.utils.unittest_with_edcore_sqlite import Unittest_with_edcore_sqlite_no_data_load,\
    UnittestEdcoreDBConnection
from smarter.reports.helpers.constants import Constants


class TestDemographics(Unittest_with_edcore_sqlite_no_data_load):

    def test_get_demographic_program_filter(self):
        test_filter = {}
        value = _get_filter(FILTERS_PROGRAM_IEP, None, test_filter)
        self.assertFalse(value)
        test_filter = {FILTERS_PROGRAM_IEP: [YES]}
        value = _get_filter(FILTERS_PROGRAM_IEP, True, test_filter)
        self.assertEqual(str(value), str(True == true()))
        test_filter = {FILTERS_PROGRAM_IEP: [NO]}
        value = _get_filter(FILTERS_PROGRAM_IEP, False, test_filter)
        self.assertEqual(str(value), str(False == false()))
        test_filter = {FILTERS_PROGRAM_IEP: [NOT_STATED]}
        value = _get_filter(FILTERS_PROGRAM_IEP, None, test_filter)
        self.assertEqual(str(value), str(None == null()))
        test_filter = {FILTERS_PROGRAM_IEP: [YES, NO, NOT_STATED]}
        value = _get_filter(FILTERS_PROGRAM_IEP, None, test_filter)
        self.assertEqual(3, len(value))
        test_filter = {FILTERS_PROGRAM_IEP: [YES, 'whatever']}
        value = _get_filter(FILTERS_PROGRAM_IEP, True, test_filter)
        self.assertEqual(str(value), str(True == true()))

    def test_has_filters_with_empty_params(self):
        self.assertFalse(has_filters({}))

    def test_has_filters_with_no_filters(self):
        self.assertFalse(has_filters({'notDemographicFilter': 'a'}))

    def test_has_filters_with_filters(self):
        self.assertTrue(has_filters({FILTERS_PROGRAM_IEP: 'a'}))
        self.assertTrue(has_filters({FILTERS_PROGRAM_504: 'a'}))
        self.assertTrue(has_filters({FILTERS_PROGRAM_LEP: 'a'}))
        self.assertTrue(has_filters({FILTERS_PROGRAM_TT1: 'a'}))
        self.assertTrue(has_filters({FILTERS_ETHNICITY: 'a'}))
        self.assertTrue(has_filters({FILTERS_GENDER: 'a'}))
        self.assertTrue(has_filters({FILTERS_GRADE: 'a'}))

    def test_apply_filter_to_query_with_no_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {})
            self.assertIsNone(query._whereclause)

    def test_apply_filter_to_query_with_grade_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_GRADE: ['3', '4']})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.asmt_grade", str(query._whereclause))

    def test_apply_filter_to_query_with_iep_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_PROGRAM_IEP: [YES]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.dmg_prg_iep", str(query._whereclause))

    def test_apply_filter_to_query_with_lep_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_PROGRAM_LEP: [NO]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.dmg_prg_lep", str(query._whereclause))

    def test_apply_filter_to_query_with_504_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_PROGRAM_504: [NOT_STATED]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.dmg_prg_504", str(query._whereclause))

    def test_apply_filter_to_query_with_tt1_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_PROGRAM_TT1: [YES]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.dmg_prg_tt1", str(query._whereclause))

    def test_apply_filter_to_query_with_ethnic_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_ETHNICITY: [FILTERS_ETHNICITY_AMERICAN]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.dmg_eth_derived", str(query._whereclause))

    def test_apply_filter_to_query_with_gender_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            query = apply_filter_to_query(query, fact_asmt_outcome, {FILTERS_GENDER: [FILTERS_GENDER_FEMALE, FILTERS_GENDER_MALE]})
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.gender", str(query._whereclause))

    def test_apply_filter_to_query_with_multi_filters(self):
        with UnittestEdcoreDBConnection() as connection:
            fact_asmt_outcome = connection.get_table(Constants.FACT_ASMT_OUTCOME)
            query = select([fact_asmt_outcome.c.school_guid],
                           from_obj=([fact_asmt_outcome]))
            filters = {FILTERS_GENDER: [FILTERS_GENDER_FEMALE],
                       FILTERS_PROGRAM_IEP: [NOT_STATED],
                       FILTERS_ETHNICITY: [FILTERS_ETHNICITY_MULTI]}
            query = apply_filter_to_query(query, fact_asmt_outcome, filters)
            self.assertIsNotNone(query._whereclause)
            self.assertIn("fact_asmt_outcome.gender", str(query._whereclause))
            self.assertIn("fact_asmt_outcome.dmg_eth_derived", str(query._whereclause))
            self.assertIn("fact_asmt_outcome.dmg_prg_iep", str(query._whereclause))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_value_NONE']
    unittest.main()