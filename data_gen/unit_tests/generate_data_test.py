"""
Unit tests for the generate_data module.

@author: nestep
@date: March 20, 2014
"""

import datetime
import os

from nose.tools import assert_raises

import generate_data as generate_data
import sbac_data_generation.generators.assessment as asmt_gen
import sbac_data_generation.generators.enrollment as enroll_gen
import sbac_data_generation.generators.hierarchy as hier_gen
import sbac_data_generation.generators.population as pop_gen

from sbac_data_generation.util.id_gen import IDGen

ID_GEN = IDGen()


def setup_module():
    # Verify output directory exists (some tested methods will write to disk)
    if not os.path.exists(generate_data.OUT_PATH_ROOT):
        os.makedirs(generate_data.OUT_PATH_ROOT)


def test_set_configuration_exception():
    assert_raises(ValueError, generate_data.assign_team_configuration_options, 'Unknown', 'North Carolina', 'NC',
                  'typical_1')


def test_set_configuration_state():
    # Set the configuration
    generate_data.assign_team_configuration_options('sonics', 'North Carolina', 'NC', 'typical_1')

    # Tests
    assert generate_data.STATES[0]['name'] == 'North Carolina'
    assert generate_data.STATES[0]['code'] == 'NC'
    assert generate_data.STATES[0]['type'] == 'typical_1'


def test_set_configuration_sonics():
    # Set the configuration
    generate_data.assign_team_configuration_options('sonics', 'North Carolina', 'NC', 'typical_1')

    # Tests
    assert len(generate_data.YEARS) == 3
    assert 2015 in generate_data.YEARS
    assert 2016 in generate_data.YEARS
    assert 2017 in generate_data.YEARS
    assert len(generate_data.ASMT_YEARS) == 3
    assert 2015 in generate_data.ASMT_YEARS
    assert 2016 in generate_data.ASMT_YEARS
    assert 2017 in generate_data.ASMT_YEARS
    assert len(generate_data.INTERIM_ASMT_PERIODS) == 3
    assert 'Fall' in generate_data.INTERIM_ASMT_PERIODS
    assert 'Winter' in generate_data.INTERIM_ASMT_PERIODS
    assert 'Spring' in generate_data.INTERIM_ASMT_PERIODS
    assert generate_data.NUMBER_REGISTRATION_SYSTEMS == 1


def test_set_configuration_arkanoids():
    # Set the configuration
    generate_data.assign_team_configuration_options('arkanoids', 'North Carolina', 'NC', 'typical_1')

    # Tests
    assert len(generate_data.YEARS) == 2
    assert 2015 in generate_data.YEARS
    assert 2016 in generate_data.YEARS
    assert len(generate_data.ASMT_YEARS) == 1
    assert 2016 in generate_data.ASMT_YEARS
    assert len(generate_data.INTERIM_ASMT_PERIODS) == 0
    assert generate_data.NUMBER_REGISTRATION_SYSTEMS == 1


def test_create_assessment_object():
    asmt = generate_data.create_assessment_object('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    assert asmt.asmt_type == 'SUMMATIVE'
    assert asmt.subject == 'ELA'


def test_create_assessment_object_summative():
    asmt = generate_data.create_assessment_object('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    assert asmt.period_year == 2015
    assert asmt.period == 'Spring 2015'
    assert asmt.effective_date == datetime.date(2015, 5, 15)
    assert asmt.from_date == datetime.date(2015, 5, 15)
    assert asmt.to_date == datetime.date(9999, 12, 31)


def test_create_assessment_object_interim_fall():
    asmt = generate_data.create_assessment_object('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN)
    assert asmt.period_year == 2015
    assert asmt.period == 'Fall 2014'
    assert asmt.effective_date == datetime.date(2014, 9, 15)
    assert asmt.from_date == datetime.date(2014, 9, 15)
    assert asmt.to_date == datetime.date(9999, 12, 31)


def test_create_assessment_object_interim_winter():
    asmt = generate_data.create_assessment_object('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN)
    assert asmt.period_year == 2015
    assert asmt.period == 'Winter 2014'
    assert asmt.effective_date == datetime.date(2014, 12, 15)
    assert asmt.from_date == datetime.date(2014, 12, 15)
    assert asmt.to_date == datetime.date(9999, 12, 31)


def test_create_assessment_object_interim_spring():
    asmt = generate_data.create_assessment_object('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)
    assert asmt.period_year == 2015
    assert asmt.period == 'Spring 2015'
    assert asmt.effective_date == datetime.date(2015, 3, 15)
    assert asmt.from_date == datetime.date(2015, 3, 15)
    assert asmt.to_date == datetime.date(9999, 12, 31)


def test_create_assessment_outcome_object_skipped():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=1,
                                                              retake_rate=0, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 0


def test_create_assessment_outcome_object_one_active_result():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=0,
                                                              retake_rate=0, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 1
    assert outcomes[0].result_status == 'C'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_object_retake_results():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=0,
                                                              retake_rate=1, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'I'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 20)


def test_create_assessment_outcome_object_one_deleted_result():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=0,
                                                              retake_rate=0, delete_rate=1, update_rate=0)

    # Tests
    assert len(outcomes) == 1
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_object_update_no_second_delete_results():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=0,
                                                              retake_rate=0, delete_rate=0, update_rate=1)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_object_update_second_delete_results():
    # Create objects
    asmt = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_object(student, asmt, section, inst_hier, ID_GEN, skip_rate=0,
                                                              retake_rate=0, delete_rate=1, update_rate=1)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'D'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_objects_no_interims_skipped():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=1, retake_rate=0, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 0


def test_create_assessment_outcome_objects_no_interims_one_active_result():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=0, retake_rate=0, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 1
    assert outcomes[0].result_status == 'C'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_objects_no_interims_retake_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=0, retake_rate=1, delete_rate=0, update_rate=0)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'I'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 20)


def test_create_assessment_outcome_objects_no_interim_one_deleted_result():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=0, retake_rate=0, delete_rate=1, update_rate=0)

    # Tests
    assert len(outcomes) == 1
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_objects_no_interim_update_no_second_delete_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=0, retake_rate=0, delete_rate=0, update_rate=1)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_objects_no_interim_update_second_delete_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, [], section, inst_hier, ID_GEN,
                                                               skip_rate=0, retake_rate=0, delete_rate=1, update_rate=1)

    # Tests
    assert len(outcomes) == 2
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].result_status == 'D'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)


def test_create_assessment_outcome_objects_interims_skipped():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=1, retake_rate=0, delete_rate=0,
                                                               update_rate=0)

    # Tests
    assert len(outcomes) == 0


def test_create_assessment_outcome_objects_interims_one_active_result():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=0, retake_rate=0, delete_rate=0,
                                                               update_rate=0)

    # Tests
    assert len(outcomes) == 4
    assert outcomes[0].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[0].result_status == 'C'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[2].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[2].result_status == 'C'
    assert outcomes[2].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[3].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[3].result_status == 'C'
    assert outcomes[3].date_taken == datetime.date(2015, 3, 15)


def test_create_assessment_outcome_objects_interims_retake_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=0, retake_rate=1, delete_rate=0,
                                                               update_rate=0)

    # Tests
    assert len(outcomes) == 8
    assert outcomes[0].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[0].result_status == 'I'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 20)
    assert outcomes[2].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[2].result_status == 'I'
    assert outcomes[2].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[3].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[3].result_status == 'C'
    assert outcomes[3].date_taken == datetime.date(2014, 9, 20)
    assert outcomes[4].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[4].result_status == 'I'
    assert outcomes[4].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[5].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[5].result_status == 'C'
    assert outcomes[5].date_taken == datetime.date(2014, 12, 20)
    assert outcomes[6].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[6].result_status == 'I'
    assert outcomes[6].date_taken == datetime.date(2015, 3, 15)
    assert outcomes[7].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[7].result_status == 'C'
    assert outcomes[7].date_taken == datetime.date(2015, 3, 20)


def test_create_assessment_outcome_objects_interim_one_deleted_result():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=0, retake_rate=0, delete_rate=1,
                                                               update_rate=0)

    # Tests
    assert len(outcomes) == 4
    assert outcomes[0].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[1].result_status == 'D'
    assert outcomes[1].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[2].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[2].result_status == 'D'
    assert outcomes[2].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[3].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[3].result_status == 'D'
    assert outcomes[3].date_taken == datetime.date(2015, 3, 15)


def test_create_assessment_outcome_objects_interim_update_no_second_delete_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=0, retake_rate=0, delete_rate=0,
                                                               update_rate=1)

    # Tests
    assert len(outcomes) == 8
    assert outcomes[0].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[1].result_status == 'C'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[2].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[2].result_status == 'D'
    assert outcomes[2].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[3].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[3].result_status == 'C'
    assert outcomes[3].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[4].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[4].result_status == 'D'
    assert outcomes[4].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[5].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[5].result_status == 'C'
    assert outcomes[5].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[6].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[6].result_status == 'D'
    assert outcomes[6].date_taken == datetime.date(2015, 3, 15)
    assert outcomes[7].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[7].result_status == 'C'
    assert outcomes[7].date_taken == datetime.date(2015, 3, 15)


def test_create_assessment_outcome_objects_interim_update_second_delete_results():
    # Create objects
    asmt_summ = asmt_gen.generate_assessment('SUMMATIVE', 'Spring', 2015, 'ELA', ID_GEN)
    interim_asmts = [asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Fall', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Winter', 2015, 'ELA', ID_GEN),
                     asmt_gen.generate_assessment('INTERIM COMPREHENSIVE', 'Spring', 2015, 'ELA', ID_GEN)]
    state = hier_gen.generate_state('devel', 'Example State', 'ES', ID_GEN)
    district = hier_gen.generate_district('Small Average', state, ID_GEN)
    school = hier_gen.generate_school('Elementary School', district, ID_GEN)
    clss = enroll_gen.generate_class('Class', 'ELA', school)
    section = enroll_gen.generate_section(clss, 'Section', 3, ID_GEN, 2015)
    student = pop_gen.generate_student(school, 3, ID_GEN, 2015)
    inst_hier = hier_gen.generate_institution_hierarchy(state, district, school, ID_GEN)

    # Create outcomes
    outcomes = generate_data.create_assessment_outcome_objects(student, asmt_summ, interim_asmts, section, inst_hier,
                                                               ID_GEN, skip_rate=0, retake_rate=0, delete_rate=1,
                                                               update_rate=1)

    # Tests
    assert len(outcomes) == 8
    assert outcomes[0].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[0].result_status == 'D'
    assert outcomes[0].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[1].assessment.asmt_type == 'SUMMATIVE'
    assert outcomes[1].result_status == 'D'
    assert outcomes[1].date_taken == datetime.date(2015, 5, 15)
    assert outcomes[2].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[2].result_status == 'D'
    assert outcomes[2].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[3].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[3].result_status == 'D'
    assert outcomes[3].date_taken == datetime.date(2014, 9, 15)
    assert outcomes[4].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[4].result_status == 'D'
    assert outcomes[4].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[5].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[5].result_status == 'D'
    assert outcomes[5].date_taken == datetime.date(2014, 12, 15)
    assert outcomes[6].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[6].result_status == 'D'
    assert outcomes[6].date_taken == datetime.date(2015, 3, 15)
    assert outcomes[7].assessment.asmt_type == 'INTERIM COMPREHENSIVE'
    assert outcomes[7].result_status == 'D'
    assert outcomes[7].date_taken == datetime.date(2015, 3, 15)