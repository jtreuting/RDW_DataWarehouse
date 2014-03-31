# transformation rules
CLEAN = 'clean'
CLEAN_UP = 'cleanUpper'
DATE = 'date'
SCHOOL_TY = 'schoolType'
GENDER = 'gender'
YN = 'yn'

COLUMNS = ('phase', 'source_table', 'source_column', 'target_table', 'target_column', 'transformation_rule', 'stored_proc_name')

op_table_conf = {
    'int_sbac_asmt_outcome',
    'stg_sbac_asmt_outcome'
}

ref_table_conf = {
    'column_definitions': COLUMNS,
    'column_mappings': [
        # Columns:
        # column_map_key, phase, source_table, source_column, target_table, target_column, transformation_rule, stored_proc_name, stored_proc_created_date, created_date

        # json to int_sbac_asmt
        ('1', 'lz_json', 'identification.guid', 'int_sbac_asmt', 'guid_asmt', 'clean', None),
        ('1', 'lz_json', 'claims.claim_1.name', 'int_sbac_asmt', 'name_claim_1', 'clean', None),
        ('1', 'lz_json', 'claims.claim_2.name', 'int_sbac_asmt', 'name_claim_2', 'clean', None),
        ('1', 'lz_json', 'claims.claim_3.name', 'int_sbac_asmt', 'name_claim_3', 'clean', None),
        ('1', 'lz_json', 'claims.claim_4.name', 'int_sbac_asmt', 'name_claim_4', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_1.name', 'int_sbac_asmt', 'name_perf_lvl_1', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_2.name', 'int_sbac_asmt', 'name_perf_lvl_2', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_3.name', 'int_sbac_asmt', 'name_perf_lvl_3', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_4.name', 'int_sbac_asmt', 'name_perf_lvl_4', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_5.name', 'int_sbac_asmt', 'name_perf_lvl_5', 'clean', None),
        ('1', 'lz_json', 'claim_performance_levels.level_1.name', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_1', 'clean', None),
        ('1', 'lz_json', 'claim_performance_levels.level_2.name', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_2', 'clean', None),
        ('1', 'lz_json', 'claim_performance_levels.level_3.name', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_3', 'clean', None),
        ('1', 'lz_json', 'identification.period', 'int_sbac_asmt', 'period', 'clean', None),
        ('1', 'lz_json', 'claims.claim_1.max_score', 'int_sbac_asmt', 'score_claim_1_max', 'clean', None),
        ('1', 'lz_json', 'claims.claim_1.min_score', 'int_sbac_asmt', 'score_claim_1_min', 'clean', None),
        ('1', 'lz_json', 'claims.claim_1.weight', 'int_sbac_asmt', 'score_claim_1_weight', 'calcWeight', None),
        ('1', 'lz_json', 'claims.claim_2.max_score', 'int_sbac_asmt', 'score_claim_2_max', 'clean', None),
        ('1', 'lz_json', 'claims.claim_2.min_score', 'int_sbac_asmt', 'score_claim_2_min', 'clean', None),
        ('1', 'lz_json', 'claims.claim_2.weight', 'int_sbac_asmt', 'score_claim_2_weight', 'calcWeight', None),
        ('1', 'lz_json', 'claims.claim_3.max_score', 'int_sbac_asmt', 'score_claim_3_max', 'clean', None),
        ('1', 'lz_json', 'claims.claim_3.min_score', 'int_sbac_asmt', 'score_claim_3_min', 'clean', None),
        ('1', 'lz_json', 'claims.claim_3.weight', 'int_sbac_asmt', 'score_claim_3_weight', 'calcWeight', None),
        ('1', 'lz_json', 'claims.claim_4.max_score', 'int_sbac_asmt', 'score_claim_4_max', 'clean', None),
        ('1', 'lz_json', 'claims.claim_4.min_score', 'int_sbac_asmt', 'score_claim_4_min', 'clean', None),
        ('1', 'lz_json', 'claims.claim_4.weight', 'int_sbac_asmt', 'score_claim_4_weight', 'calcWeight', None),
        ('1', 'lz_json', 'performance_levels.level_2.cut_point', 'int_sbac_asmt', 'score_cut_point_1', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_3.cut_point', 'int_sbac_asmt', 'score_cut_point_2', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_4.cut_point', 'int_sbac_asmt', 'score_cut_point_3', 'clean', None),
        ('1', 'lz_json', 'performance_levels.level_5.cut_point', 'int_sbac_asmt', 'score_cut_point_4', 'clean', None),
        ('1', 'lz_json', 'overall.max_score', 'int_sbac_asmt', 'score_overall_max', 'clean', None),
        ('1', 'lz_json', 'overall.min_score', 'int_sbac_asmt', 'score_overall_min', 'clean', None),
        ('1', 'lz_json', 'identification.subject', 'int_sbac_asmt', 'subject', 'subjectType', None),
        ('1', 'lz_json', 'identification.type', 'int_sbac_asmt', 'type', 'asmtType', None),
        ('1', 'lz_json', 'identification.version', 'int_sbac_asmt', 'version', 'clean', None),
        ('1', 'lz_json', 'identification.year', 'int_sbac_asmt', 'year', 'clean', None),
        ('1', 'lz_json', 'identification.effective_date', 'int_sbac_asmt', 'effective_date', 'clean', None),
        # CSV to staging
        ('1', 'lz_csv', 'address_student_city', 'stg_sbac_asmt_outcome', 'address_student_city', 'clean', None),
        ('1', 'lz_csv', 'address_student_line1', 'stg_sbac_asmt_outcome', 'address_student_line1', 'clean', None),
        ('1', 'lz_csv', 'address_student_line2', 'stg_sbac_asmt_outcome', 'address_student_line2', 'clean', None),
        ('1', 'lz_csv', 'address_student_zip', 'stg_sbac_asmt_outcome', 'address_student_zip', 'clean', None),
        ('1', 'lz_csv', 'code_state', 'stg_sbac_asmt_outcome', 'code_state', 'cleanUpper', None),
        ('1', 'lz_csv', 'date_assessed', 'stg_sbac_asmt_outcome', 'date_assessed', 'date', None),
        ('1', 'lz_csv', 'dob_student', 'stg_sbac_asmt_outcome', 'dob_student', 'date', None),
        ('1', 'lz_csv', 'email_student', 'stg_sbac_asmt_outcome', 'email_student', 'clean', None),
        ('1', 'lz_csv', 'gender_student', 'stg_sbac_asmt_outcome', 'gender_student', 'gender', None),
        ('1', 'lz_csv', 'grade_asmt', 'stg_sbac_asmt_outcome', 'grade_asmt', 'clean', None),
        ('1', 'lz_csv', 'grade_enrolled', 'stg_sbac_asmt_outcome', 'grade_enrolled', 'clean', None),
        ('1', 'lz_csv', 'guid_asmt', 'stg_sbac_asmt_outcome', 'guid_asmt', 'clean', None),
        ('1', 'lz_csv', 'guid_asmt_location', 'stg_sbac_asmt_outcome', 'guid_asmt_location', 'clean', None),
        ('1', 'lz_csv', 'guid_district', 'stg_sbac_asmt_outcome', 'guid_district', 'clean', None),
        ('1', 'lz_csv', 'guid_school', 'stg_sbac_asmt_outcome', 'guid_school', 'clean', None),
        ('1', 'lz_csv', 'guid_student', 'stg_sbac_asmt_outcome', 'guid_student', 'clean', None),
        ('1', 'lz_csv', 'external_student_id', 'stg_sbac_asmt_outcome', 'external_student_id', 'clean', None),
        ('1', 'lz_csv', 'name_asmt_location', 'stg_sbac_asmt_outcome', 'name_asmt_location', 'clean', None),
        ('1', 'lz_csv', 'name_district', 'stg_sbac_asmt_outcome', 'name_district', 'clean', None),
        ('1', 'lz_csv', 'name_school', 'stg_sbac_asmt_outcome', 'name_school', 'clean', None),
        ('1', 'lz_csv', 'name_state', 'stg_sbac_asmt_outcome', 'name_state', 'clean', None),
        ('1', 'lz_csv', 'name_student_first', 'stg_sbac_asmt_outcome', 'name_student_first', 'clean', None),
        ('1', 'lz_csv', 'name_student_last', 'stg_sbac_asmt_outcome', 'name_student_last', 'clean', None),
        ('1', 'lz_csv', 'name_student_middle', 'stg_sbac_asmt_outcome', 'name_student_middle', 'clean', None),
        ('1', 'lz_csv', 'score_asmt', 'stg_sbac_asmt_outcome', 'score_asmt', 'clean', None),
        ('1', 'lz_csv', 'score_asmt_max', 'stg_sbac_asmt_outcome', 'score_asmt_max', 'clean', None),
        ('1', 'lz_csv', 'score_asmt_min', 'stg_sbac_asmt_outcome', 'score_asmt_min', 'clean', None),
        ('1', 'lz_csv', 'score_claim_1', 'stg_sbac_asmt_outcome', 'score_claim_1', 'clean', None),
        ('1', 'lz_csv', 'score_claim_1_max', 'stg_sbac_asmt_outcome', 'score_claim_1_max', 'clean', None),
        ('1', 'lz_csv', 'score_claim_1_min', 'stg_sbac_asmt_outcome', 'score_claim_1_min', 'clean', None),
        ('1', 'lz_csv', 'asmt_claim_1_perf_lvl', 'stg_sbac_asmt_outcome', 'asmt_claim_1_perf_lvl', 'clean', None),
        ('1', 'lz_csv', 'score_claim_2', 'stg_sbac_asmt_outcome', 'score_claim_2', 'clean', None),
        ('1', 'lz_csv', 'score_claim_2_max', 'stg_sbac_asmt_outcome', 'score_claim_2_max', 'clean', None),
        ('1', 'lz_csv', 'score_claim_2_min', 'stg_sbac_asmt_outcome', 'score_claim_2_min', 'clean', None),
        ('1', 'lz_csv', 'asmt_claim_2_perf_lvl', 'stg_sbac_asmt_outcome', 'asmt_claim_2_perf_lvl', 'clean', None),
        ('1', 'lz_csv', 'score_claim_3', 'stg_sbac_asmt_outcome', 'score_claim_3', 'clean', None),
        ('1', 'lz_csv', 'score_claim_3_max', 'stg_sbac_asmt_outcome', 'score_claim_3_max', 'clean', None),
        ('1', 'lz_csv', 'score_claim_3_min', 'stg_sbac_asmt_outcome', 'score_claim_3_min', 'clean', None),
        ('1', 'lz_csv', 'asmt_claim_3_perf_lvl', 'stg_sbac_asmt_outcome', 'asmt_claim_3_perf_lvl', 'clean', None),
        ('1', 'lz_csv', 'score_claim_4', 'stg_sbac_asmt_outcome', 'score_claim_4', 'clean', None),
        ('1', 'lz_csv', 'score_claim_4_max', 'stg_sbac_asmt_outcome', 'score_claim_4_max', 'clean', None),
        ('1', 'lz_csv', 'score_claim_4_min', 'stg_sbac_asmt_outcome', 'score_claim_4_min', 'clean', None),
        ('1', 'lz_csv', 'asmt_claim_4_perf_lvl', 'stg_sbac_asmt_outcome', 'asmt_claim_4_perf_lvl', 'clean', None),
        ('1', 'lz_csv', 'score_perf_level', 'stg_sbac_asmt_outcome', 'score_perf_level', 'clean', None),
        ('1', 'lz_csv', 'type_school', 'stg_sbac_asmt_outcome', 'type_school', 'schoolType', None),
        ('1', 'lz_csv', 'dmg_eth_hsp', 'stg_sbac_asmt_outcome', 'dmg_eth_hsp', 'yn', None),
        ('1', 'lz_csv', 'dmg_eth_ami', 'stg_sbac_asmt_outcome', 'dmg_eth_ami', 'yn', None),
        ('1', 'lz_csv', 'dmg_eth_asn', 'stg_sbac_asmt_outcome', 'dmg_eth_asn', 'yn', None),
        ('1', 'lz_csv', 'dmg_eth_blk', 'stg_sbac_asmt_outcome', 'dmg_eth_blk', 'yn', None),
        ('1', 'lz_csv', 'dmg_eth_pcf', 'stg_sbac_asmt_outcome', 'dmg_eth_pcf', 'yn', None),
        ('1', 'lz_csv', 'dmg_eth_wht', 'stg_sbac_asmt_outcome', 'dmg_eth_wht', 'yn', None),
        ('1', 'lz_csv', 'dmg_prg_iep', 'stg_sbac_asmt_outcome', 'dmg_prg_iep', 'yn', None),
        ('1', 'lz_csv', 'dmg_prg_lep', 'stg_sbac_asmt_outcome', 'dmg_prg_lep', 'yn', None),
        ('1', 'lz_csv', 'dmg_prg_504', 'stg_sbac_asmt_outcome', 'dmg_prg_504', 'yn', None),
        ('1', 'lz_csv', 'dmg_prg_tt1', 'stg_sbac_asmt_outcome', 'dmg_prg_tt1', 'yn', None),
        ('1', 'lz_csv', 'asmt_type', 'stg_sbac_asmt_outcome', 'asmt_type', 'asmtType', None),
        ('1', 'lz_csv', 'asmt_subject', 'stg_sbac_asmt_outcome', 'asmt_subject', 'subjectType', None),
        ('1', 'lz_csv', 'asmt_year', 'stg_sbac_asmt_outcome', 'asmt_year', 'clean', None),
        ('1', 'lz_csv', 'acc_asl_video_embed', 'stg_sbac_asmt_outcome', 'acc_asl_video_embed', 'clean', None),
        ('1', 'lz_csv', 'acc_asl_human_nonembed', 'stg_sbac_asmt_outcome', 'acc_asl_human_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_braile_embed', 'stg_sbac_asmt_outcome', 'acc_braile_embed', 'clean', None),
        ('1', 'lz_csv', 'acc_closed_captioning_embed', 'stg_sbac_asmt_outcome', 'acc_closed_captioning_embed', 'clean', None),
        ('1', 'lz_csv', 'acc_text_to_speech_embed', 'stg_sbac_asmt_outcome', 'acc_text_to_speech_embed', 'clean', None),
        ('1', 'lz_csv', 'acc_abacus_nonembed', 'stg_sbac_asmt_outcome', 'acc_abacus_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_alternate_response_options_nonembed', 'stg_sbac_asmt_outcome', 'acc_alternate_response_options_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_calculator_nonembed', 'stg_sbac_asmt_outcome', 'acc_calculator_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_multiplication_table_nonembed', 'stg_sbac_asmt_outcome', 'acc_multiplication_table_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_print_on_demand_nonembed', 'stg_sbac_asmt_outcome', 'acc_print_on_demand_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_read_aloud_nonembed', 'stg_sbac_asmt_outcome', 'acc_read_aloud_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_scribe_nonembed', 'stg_sbac_asmt_outcome', 'acc_scribe_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_speech_to_text_nonembed', 'stg_sbac_asmt_outcome', 'acc_speech_to_text_nonembed', 'clean', None),
        ('1', 'lz_csv', 'acc_streamline_mode', 'stg_sbac_asmt_outcome', 'acc_streamline_mode', 'clean', None),
        ('1', 'lz_csv', 'op', 'stg_sbac_asmt_outcome', 'op', 'option', None),
        # Staging to Integration
        ('3', 'stg_sbac_asmt_outcome', 'guid_batch', 'int_sbac_asmt_outcome', 'guid_batch', None, None),
        ('3', 'stg_sbac_asmt_outcome', 'op', 'int_sbac_asmt_outcome', 'op', None, None),
        ('3', 'stg_sbac_asmt_outcome', 'guid_asmt', 'int_sbac_asmt_outcome', 'guid_asmt', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'guid_asmt_location', 'int_sbac_asmt_outcome', 'guid_asmt_location', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_asmt_location', 'int_sbac_asmt_outcome', 'name_asmt_location', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'grade_asmt', 'int_sbac_asmt_outcome', 'grade_asmt', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_state', 'int_sbac_asmt_outcome', 'name_state', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'code_state', 'int_sbac_asmt_outcome', 'code_state', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'guid_district', 'int_sbac_asmt_outcome', 'guid_district', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_district', 'int_sbac_asmt_outcome', 'name_district', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'guid_school', 'int_sbac_asmt_outcome', 'guid_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_school', 'int_sbac_asmt_outcome', 'name_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'type_school', 'int_sbac_asmt_outcome', 'type_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'guid_student', 'int_sbac_asmt_outcome', 'guid_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'external_student_id', 'int_sbac_asmt_outcome', 'external_student_id', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_student_first', 'int_sbac_asmt_outcome', 'name_student_first', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_student_middle', 'int_sbac_asmt_outcome', 'name_student_middle', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'name_student_last', 'int_sbac_asmt_outcome', 'name_student_last', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'address_student_line1', 'int_sbac_asmt_outcome', 'address_student_line1', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'address_student_line2', 'int_sbac_asmt_outcome', 'address_student_line2', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'address_student_city', 'int_sbac_asmt_outcome', 'address_student_city', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'address_student_zip', 'int_sbac_asmt_outcome', 'address_student_zip', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'gender_student', 'int_sbac_asmt_outcome', 'gender_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'email_student', 'int_sbac_asmt_outcome', 'email_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'dob_student', 'int_sbac_asmt_outcome', 'dob_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'grade_enrolled', 'int_sbac_asmt_outcome', 'grade_enrolled', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'date_assessed', 'int_sbac_asmt_outcome', 'date_assessed', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'date_assessed', 'int_sbac_asmt_outcome', 'date_taken_day', None, "extract(day from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'stg_sbac_asmt_outcome', 'date_assessed', 'int_sbac_asmt_outcome', 'date_taken_month', None, "extract(month from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'stg_sbac_asmt_outcome', 'date_assessed', 'int_sbac_asmt_outcome', 'date_taken_year', None, "extract(year from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'stg_sbac_asmt_outcome', 'score_asmt', 'int_sbac_asmt_outcome', 'score_asmt', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_asmt_min', 'int_sbac_asmt_outcome', 'score_asmt_min', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_asmt_max', 'int_sbac_asmt_outcome', 'score_asmt_max', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_perf_level', 'int_sbac_asmt_outcome', 'score_perf_level', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_1', 'int_sbac_asmt_outcome', 'score_claim_1', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_1_min', 'int_sbac_asmt_outcome', 'score_claim_1_min', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_1_max', 'int_sbac_asmt_outcome', 'score_claim_1_max', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_claim_1_perf_lvl', 'int_sbac_asmt_outcome', 'asmt_claim_1_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_2', 'int_sbac_asmt_outcome', 'score_claim_2', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_2_min', 'int_sbac_asmt_outcome', 'score_claim_2_min', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_2_max', 'int_sbac_asmt_outcome', 'score_claim_2_max', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_claim_2_perf_lvl', 'int_sbac_asmt_outcome', 'asmt_claim_2_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_3', 'int_sbac_asmt_outcome', 'score_claim_3', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_3_min', 'int_sbac_asmt_outcome', 'score_claim_3_min', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_3_max', 'int_sbac_asmt_outcome', 'score_claim_3_max', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_claim_3_perf_lvl', 'int_sbac_asmt_outcome', 'asmt_claim_3_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_4', 'int_sbac_asmt_outcome', 'score_claim_4', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_4_min', 'int_sbac_asmt_outcome', 'score_claim_4_min', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'score_claim_4_max', 'int_sbac_asmt_outcome', 'score_claim_4_max', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_claim_4_perf_lvl', 'int_sbac_asmt_outcome', 'asmt_claim_4_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'created_date', 'int_sbac_asmt_outcome', 'created_date', None, None),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_type', 'int_sbac_asmt_outcome', 'asmt_type', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_subject', 'int_sbac_asmt_outcome', 'asmt_subject', None, 'substr({src_column}, 1, {length})'),
        ('3', 'stg_sbac_asmt_outcome', 'asmt_year', 'int_sbac_asmt_outcome', 'asmt_year', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_hsp', 'int_sbac_asmt_outcome', 'dmg_eth_hsp', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_ami', 'int_sbac_asmt_outcome', 'dmg_eth_ami', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_asn', 'int_sbac_asmt_outcome', 'dmg_eth_asn', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_blk', 'int_sbac_asmt_outcome', 'dmg_eth_blk', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_pcf', 'int_sbac_asmt_outcome', 'dmg_eth_pcf', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_eth_wht', 'int_sbac_asmt_outcome', 'dmg_eth_wht', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_prg_iep', 'int_sbac_asmt_outcome', 'dmg_prg_iep', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_prg_lep', 'int_sbac_asmt_outcome', 'dmg_prg_lep', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_prg_504', 'int_sbac_asmt_outcome', 'dmg_prg_504', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', 'dmg_prg_tt1', 'int_sbac_asmt_outcome', 'dmg_prg_tt1', None, 'cast({src_column} as bool)'),
        ('3', 'stg_sbac_asmt_outcome', "dmg_eth_blk, dmg_eth_asn, dmg_eth_hsp, dmg_eth_ami, dmg_eth_pcf, dmg_eth_wht", 'int_sbac_asmt_outcome', 'dmg_eth_derived', 'deriveEthnicity', None),
        ('3', 'stg_sbac_asmt_outcome', 'acc_asl_video_embed', 'int_sbac_asmt_outcome', 'acc_asl_video_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_asl_human_nonembed', 'int_sbac_asmt_outcome', 'acc_asl_human_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_braile_embed', 'int_sbac_asmt_outcome', 'acc_braile_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_closed_captioning_embed', 'int_sbac_asmt_outcome', 'acc_closed_captioning_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_text_to_speech_embed', 'int_sbac_asmt_outcome', 'acc_text_to_speech_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_abacus_nonembed', 'int_sbac_asmt_outcome', 'acc_abacus_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_alternate_response_options_nonembed', 'int_sbac_asmt_outcome', 'acc_alternate_response_options_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_calculator_nonembed', 'int_sbac_asmt_outcome', 'acc_calculator_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_multiplication_table_nonembed', 'int_sbac_asmt_outcome', 'acc_multiplication_table_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_print_on_demand_nonembed', 'int_sbac_asmt_outcome', 'acc_print_on_demand_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_read_aloud_nonembed', 'int_sbac_asmt_outcome', 'acc_read_aloud_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_scribe_nonembed', 'int_sbac_asmt_outcome', 'acc_scribe_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_speech_to_text_nonembed', 'int_sbac_asmt_outcome', 'acc_speech_to_text_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'stg_sbac_asmt_outcome', 'acc_streamline_mode', 'int_sbac_asmt_outcome', 'acc_streamline_mode', None, "to_number({src_column}, '99999')"),
        # Integration to Target
        ('4', 'int_sbac_asmt', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_asmt', 'asmt_rec_id', None, None),
        ('4', 'int_sbac_asmt', 'guid_asmt', 'dim_asmt', 'asmt_guid', None, None),
        ('4', 'int_sbac_asmt', 'guid_batch', 'dim_asmt', 'batch_guid', None, None),
        ('4', 'int_sbac_asmt', 'type', 'dim_asmt', 'asmt_type', None, None),
        ('4', 'int_sbac_asmt', 'period', 'dim_asmt', 'asmt_period', None, None),
        ('4', 'int_sbac_asmt', 'year', 'dim_asmt', 'asmt_period_year', None, None),
        ('4', 'int_sbac_asmt', 'version', 'dim_asmt', 'asmt_version', None, None),
        ('4', 'int_sbac_asmt', 'subject', 'dim_asmt', 'asmt_subject', None, None),
        ('4', 'int_sbac_asmt', 'name_claim_1', 'dim_asmt', 'asmt_claim_1_name', None, None),
        ('4', 'int_sbac_asmt', 'name_claim_2', 'dim_asmt', 'asmt_claim_2_name', None, None),
        ('4', 'int_sbac_asmt', 'name_claim_3', 'dim_asmt', 'asmt_claim_3_name', None, None),
        ('4', 'int_sbac_asmt', 'name_claim_4', 'dim_asmt', 'asmt_claim_4_name', None, None),
        ('4', 'int_sbac_asmt', 'name_perf_lvl_1', 'dim_asmt', 'asmt_perf_lvl_name_1', None, None),
        ('4', 'int_sbac_asmt', 'name_perf_lvl_2', 'dim_asmt', 'asmt_perf_lvl_name_2', None, None),
        ('4', 'int_sbac_asmt', 'name_perf_lvl_3', 'dim_asmt', 'asmt_perf_lvl_name_3', None, None),
        ('4', 'int_sbac_asmt', 'name_perf_lvl_4', 'dim_asmt', 'asmt_perf_lvl_name_4', None, None),
        ('4', 'int_sbac_asmt', 'name_perf_lvl_5', 'dim_asmt', 'asmt_perf_lvl_name_5', None, None),
        ('4', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_1', 'dim_asmt', 'asmt_claim_perf_lvl_name_1', None, None),
        ('4', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_2', 'dim_asmt', 'asmt_claim_perf_lvl_name_2', None, None),
        ('4', 'int_sbac_asmt', 'asmt_claim_perf_lvl_name_3', 'dim_asmt', 'asmt_claim_perf_lvl_name_3', None, None),
        ('4', 'int_sbac_asmt', 'score_overall_min', 'dim_asmt', 'asmt_score_min', None, None),
        ('4', 'int_sbac_asmt', 'score_overall_max', 'dim_asmt', 'asmt_score_max', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_1_min', 'dim_asmt', 'asmt_claim_1_score_min', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_1_max', 'dim_asmt', 'asmt_claim_1_score_max', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_1_weight', 'dim_asmt', 'asmt_claim_1_score_weight', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_2_min', 'dim_asmt', 'asmt_claim_2_score_min', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_2_max', 'dim_asmt', 'asmt_claim_2_score_max', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_2_weight', 'dim_asmt', 'asmt_claim_2_score_weight', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_3_min', 'dim_asmt', 'asmt_claim_3_score_min', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_3_max', 'dim_asmt', 'asmt_claim_3_score_max', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_3_weight', 'dim_asmt', 'asmt_claim_3_score_weight', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_4_min', 'dim_asmt', 'asmt_claim_4_score_min', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_4_max', 'dim_asmt', 'asmt_claim_4_score_max', None, None),
        ('4', 'int_sbac_asmt', 'score_claim_4_weight', 'dim_asmt', 'asmt_claim_4_score_weight', None, None),
        ('4', 'int_sbac_asmt', 'score_cut_point_1', 'dim_asmt', 'asmt_cut_point_1', None, None),
        ('4', 'int_sbac_asmt', 'score_cut_point_2', 'dim_asmt', 'asmt_cut_point_2', None, None),
        ('4', 'int_sbac_asmt', 'score_cut_point_3', 'dim_asmt', 'asmt_cut_point_3', None, None),
        ('4', 'int_sbac_asmt', 'score_cut_point_4', 'dim_asmt', 'asmt_cut_point_4', None, None),
        ('4', 'int_sbac_asmt', 'effective_date', 'dim_asmt', 'effective_date', None, None),
        ('4', 'int_sbac_asmt', "TO_CHAR(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_asmt', 'from_date', None, None),
        ('4', 'int_sbac_asmt', "'99991231'", 'dim_asmt', 'to_date', None, None),
        ('4', 'int_sbac_asmt', 'TRUE', 'dim_asmt', 'most_recent', None, None),
        ('4', 'int_sbac_asmt_outcome', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_inst_hier', 'inst_hier_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_batch', 'dim_inst_hier', 'batch_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_state', 'dim_inst_hier', 'state_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'code_state', 'dim_inst_hier', 'state_code', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_district', 'dim_inst_hier', 'district_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_district', 'dim_inst_hier', 'district_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_school', 'dim_inst_hier', 'school_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_school', 'dim_inst_hier', 'school_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'type_school', 'dim_inst_hier', 'school_category', None, None),
        ('4', 'int_sbac_asmt_outcome', "to_char(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_inst_hier', 'from_date', None, None),
        ('4', 'int_sbac_asmt_outcome', "'99991231'", 'dim_inst_hier', 'to_date', None, None),
        ('4', 'int_sbac_asmt_outcome', 'TRUE', 'dim_inst_hier', 'most_recent', None, None),
        ('4', 'int_sbac_asmt_outcome', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_student', 'student_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_student', 'dim_student', 'student_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_batch', 'dim_student', 'batch_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_student_first', 'dim_student', 'first_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_student_middle', 'dim_student', 'middle_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_student_last', 'dim_student', 'last_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'address_student_line1', 'dim_student', 'address_1', None, None),
        ('4', 'int_sbac_asmt_outcome', 'address_student_line2', 'dim_student', 'address_2', None, None),
        ('4', 'int_sbac_asmt_outcome', 'address_student_city', 'dim_student', 'city', None, None),
        ('4', 'int_sbac_asmt_outcome', 'address_student_zip', 'dim_student', 'zip_code', None, None),
        ('4', 'int_sbac_asmt_outcome', 'gender_student', 'dim_student', 'gender', None, None),
        ('4', 'int_sbac_asmt_outcome', 'email_student', 'dim_student', 'email', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dob_student', 'dim_student', 'dob', None, None),
        ('4', 'int_sbac_asmt_outcome', "''", 'dim_student', 'section_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'grade_enrolled', 'dim_student', 'grade', None, None),
        ('4', 'int_sbac_asmt_outcome', 'code_state', 'dim_student', 'state_code', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_district', 'dim_student', 'district_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_school', 'dim_student', 'school_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', "to_char(CURRENT_TIMESTAMP,'yyyymmdd')", 'dim_student', 'from_date', None, None),
        ('4', 'int_sbac_asmt_outcome', "'99991231'", 'dim_student', 'to_date', None, None),
        ('4', 'int_sbac_asmt_outcome', 'TRUE', 'dim_student', 'most_recent', None, None),
        ('4', 'int_sbac_asmt_outcome', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'fact_asmt_outcome', 'asmnt_outcome_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', None, 'fact_asmt_outcome', 'asmt_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_asmt', 'fact_asmt_outcome', 'asmt_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_student', 'fact_asmt_outcome', 'student_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'code_state', 'fact_asmt_outcome', 'state_code', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_district', 'fact_asmt_outcome', 'district_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_school', 'fact_asmt_outcome', 'school_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', '-1', 'fact_asmt_outcome', 'student_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', "''", 'fact_asmt_outcome', 'section_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', '-1', 'fact_asmt_outcome', 'inst_hier_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', None, 'fact_asmt_outcome', 'section_rec_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'external_student_id', 'fact_asmt_outcome', 'external_student_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_asmt_location', 'fact_asmt_outcome', 'where_taken_id', None, None),
        ('4', 'int_sbac_asmt_outcome', 'name_asmt_location', 'fact_asmt_outcome', 'where_taken_name', None, None),
        ('4', 'int_sbac_asmt_outcome', 'grade_asmt', 'fact_asmt_outcome', 'asmt_grade', None, None),
        ('4', 'int_sbac_asmt_outcome', 'grade_enrolled', 'fact_asmt_outcome', 'enrl_grade', None, None),
        ('4', 'int_sbac_asmt_outcome', 'date_assessed', 'fact_asmt_outcome', 'date_taken', None, None),
        ('4', 'int_sbac_asmt_outcome', 'date_taken_day', 'fact_asmt_outcome', 'date_taken_day', None, None),
        ('4', 'int_sbac_asmt_outcome', 'date_taken_month', 'fact_asmt_outcome', 'date_taken_month', None, None),
        ('4', 'int_sbac_asmt_outcome', 'date_taken_year', 'fact_asmt_outcome', 'date_taken_year', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_asmt', 'fact_asmt_outcome', 'asmt_score', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_asmt_min', 'fact_asmt_outcome', 'asmt_score_range_min', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_asmt_max', 'fact_asmt_outcome', 'asmt_score_range_max', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_perf_level', 'fact_asmt_outcome', 'asmt_perf_lvl', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_1', 'fact_asmt_outcome', 'asmt_claim_1_score', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_1_min', 'fact_asmt_outcome', 'asmt_claim_1_score_range_min', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_1_max', 'fact_asmt_outcome', 'asmt_claim_1_score_range_max', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_claim_1_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_1_perf_lvl', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_2', 'fact_asmt_outcome', 'asmt_claim_2_score', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_2_min', 'fact_asmt_outcome', 'asmt_claim_2_score_range_min', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_2_max', 'fact_asmt_outcome', 'asmt_claim_2_score_range_max', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_claim_2_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_2_perf_lvl', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_3', 'fact_asmt_outcome', 'asmt_claim_3_score', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_3_min', 'fact_asmt_outcome', 'asmt_claim_3_score_range_min', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_3_max', 'fact_asmt_outcome', 'asmt_claim_3_score_range_max', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_claim_3_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_3_perf_lvl', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_4', 'fact_asmt_outcome', 'asmt_claim_4_score', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_4_min', 'fact_asmt_outcome', 'asmt_claim_4_score_range_min', None, None),
        ('4', 'int_sbac_asmt_outcome', 'score_claim_4_max', 'fact_asmt_outcome', 'asmt_claim_4_score_range_max', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_claim_4_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_4_perf_lvl', None, None),
        ('4', 'int_sbac_asmt_outcome', 'op', 'fact_asmt_outcome', 'status', None, None),
        ('4', 'int_sbac_asmt_outcome', 'TRUE', 'fact_asmt_outcome', 'most_recent', None, None),
        ('4', 'int_sbac_asmt_outcome', 'guid_batch', 'fact_asmt_outcome', 'batch_guid', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_type', 'fact_asmt_outcome', 'asmt_type', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_subject', 'fact_asmt_outcome', 'asmt_subject', None, None),
        ('4', 'int_sbac_asmt_outcome', 'asmt_year', 'fact_asmt_outcome', 'asmt_year', None, None),
        ('4', 'int_sbac_asmt_outcome', 'gender_student', 'fact_asmt_outcome', 'gender', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_hsp', 'fact_asmt_outcome', 'dmg_eth_hsp', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_ami', 'fact_asmt_outcome', 'dmg_eth_ami', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_asn', 'fact_asmt_outcome', 'dmg_eth_asn', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_blk', 'fact_asmt_outcome', 'dmg_eth_blk', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_pcf', 'fact_asmt_outcome', 'dmg_eth_pcf', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_wht', 'fact_asmt_outcome', 'dmg_eth_wht', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_prg_iep', 'fact_asmt_outcome', 'dmg_prg_iep', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_prg_lep', 'fact_asmt_outcome', 'dmg_prg_lep', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_prg_504', 'fact_asmt_outcome', 'dmg_prg_504', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_prg_tt1', 'fact_asmt_outcome', 'dmg_prg_tt1', None, None),
        ('4', 'int_sbac_asmt_outcome', 'dmg_eth_derived', 'fact_asmt_outcome', 'dmg_eth_derived', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_asl_video_embed', 'fact_asmt_outcome', 'acc_asl_video_embed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_asl_human_nonembed', 'fact_asmt_outcome', 'acc_asl_human_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_braile_embed', 'fact_asmt_outcome', 'acc_braile_embed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_closed_captioning_embed', 'fact_asmt_outcome', 'acc_closed_captioning_embed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_text_to_speech_embed', 'fact_asmt_outcome', 'acc_text_to_speech_embed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_abacus_nonembed', 'fact_asmt_outcome', 'acc_abacus_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_alternate_response_options_nonembed', 'fact_asmt_outcome', 'acc_alternate_response_options_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_calculator_nonembed', 'fact_asmt_outcome', 'acc_calculator_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_multiplication_table_nonembed', 'fact_asmt_outcome', 'acc_multiplication_table_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_print_on_demand_nonembed', 'fact_asmt_outcome', 'acc_print_on_demand_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_read_aloud_nonembed', 'fact_asmt_outcome', 'acc_read_aloud_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_scribe_nonembed', 'fact_asmt_outcome', 'acc_scribe_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_speech_to_text_nonembed', 'fact_asmt_outcome', 'acc_speech_to_text_nonembed', None, None),
        ('4', 'int_sbac_asmt_outcome', 'acc_streamline_mode', 'fact_asmt_outcome', 'acc_streamline_mode', None, None),
        # Used only in reporting app, smarter.  udl should never pick this up
        ('1000', 'int_sbac_asmt_outcome', 'guid_asmt', 'dim_asmt', 'asmt_guid', None, None),
    ]
}
