# transformation rules
CLEAN = 'clean'
CLEAN_UP = 'cleanUpper'
DATE = 'date'
SCHOOL_TY = 'schoolType'
GENDER = 'gender'
YN = 'yn'


ref_table_conf = {
    'column_definitions': ('phase', 'source_table', 'source_column', 'target_table', 'target_column', 'transformation_rule', 'stored_proc_name'),
    'column_mappings': [
        # Columns:
        # column_map_key, phase, source_table, source_column, target_table, target_column, transformation_rule, stored_proc_name, stored_proc_created_date, created_date

        # json to int_sbac_asmt
        ('1', 'LZ_JSON', 'identification.guid', 'INT_SBAC_ASMT', 'guid_asmt', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_1.name', 'INT_SBAC_ASMT', 'name_claim_1', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_2.name', 'INT_SBAC_ASMT', 'name_claim_2', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_3.name', 'INT_SBAC_ASMT', 'name_claim_3', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_4.name', 'INT_SBAC_ASMT', 'name_claim_4', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_1.name', 'INT_SBAC_ASMT', 'name_perf_lvl_1', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_2.name', 'INT_SBAC_ASMT', 'name_perf_lvl_2', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_3.name', 'INT_SBAC_ASMT', 'name_perf_lvl_3', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_4.name', 'INT_SBAC_ASMT', 'name_perf_lvl_4', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_5.name', 'INT_SBAC_ASMT', 'name_perf_lvl_5', 'clean', None),
        ('1', 'LZ_JSON', 'claim_performance_levels.level_1.name', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_1', 'clean', None),
        ('1', 'LZ_JSON', 'claim_performance_levels.level_2.name', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_2', 'clean', None),
        ('1', 'LZ_JSON', 'claim_performance_levels.level_3.name', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_3', 'clean', None),
        ('1', 'LZ_JSON', 'identification.period', 'INT_SBAC_ASMT', 'period', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_1.max_score', 'INT_SBAC_ASMT', 'score_claim_1_max', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_1.min_score', 'INT_SBAC_ASMT', 'score_claim_1_min', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_1.weight', 'INT_SBAC_ASMT', 'score_claim_1_weight', 'calcWeight', None),
        ('1', 'LZ_JSON', 'claims.claim_2.max_score', 'INT_SBAC_ASMT', 'score_claim_2_max', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_2.min_score', 'INT_SBAC_ASMT', 'score_claim_2_min', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_2.weight', 'INT_SBAC_ASMT', 'score_claim_2_weight', 'calcWeight', None),
        ('1', 'LZ_JSON', 'claims.claim_3.max_score', 'INT_SBAC_ASMT', 'score_claim_3_max', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_3.min_score', 'INT_SBAC_ASMT', 'score_claim_3_min', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_3.weight', 'INT_SBAC_ASMT', 'score_claim_3_weight', 'calcWeight', None),
        ('1', 'LZ_JSON', 'claims.claim_4.max_score', 'INT_SBAC_ASMT', 'score_claim_4_max', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_4.min_score', 'INT_SBAC_ASMT', 'score_claim_4_min', 'clean', None),
        ('1', 'LZ_JSON', 'claims.claim_4.weight', 'INT_SBAC_ASMT', 'score_claim_4_weight', 'calcWeight', None),
        ('1', 'LZ_JSON', 'performance_levels.level_2.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_1', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_3.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_2', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_4.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_3', 'clean', None),
        ('1', 'LZ_JSON', 'performance_levels.level_5.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_4', 'clean', None),
        ('1', 'LZ_JSON', 'overall.max_score', 'INT_SBAC_ASMT', 'score_overall_max', 'clean', None),
        ('1', 'LZ_JSON', 'overall.min_score', 'INT_SBAC_ASMT', 'score_overall_min', 'clean', None),
        ('1', 'LZ_JSON', 'identification.subject', 'INT_SBAC_ASMT', 'subject', 'subjectType', None),
        ('1', 'LZ_JSON', 'identification.type', 'INT_SBAC_ASMT', 'type', 'asmtType', None),
        ('1', 'LZ_JSON', 'identification.version', 'INT_SBAC_ASMT', 'version', 'clean', None),
        ('1', 'LZ_JSON', 'identification.year', 'INT_SBAC_ASMT', 'year', 'clean', None),
        # CSV to staging
        ('1', 'LZ_CSV', 'address_student_city', 'STG_SBAC_ASMT_OUTCOME', 'address_student_city', 'clean', None),
        ('1', 'LZ_CSV', 'address_student_line1', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line1', 'clean', None),
        ('1', 'LZ_CSV', 'address_student_line2', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line2', 'clean', None),
        ('1', 'LZ_CSV', 'address_student_zip', 'STG_SBAC_ASMT_OUTCOME', 'address_student_zip', 'clean', None),
        ('1', 'LZ_CSV', 'code_state', 'STG_SBAC_ASMT_OUTCOME', 'code_state', 'cleanUpper', None),
        ('1', 'LZ_CSV', 'date_assessed', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'date', None),
        ('1', 'LZ_CSV', 'dob_student', 'STG_SBAC_ASMT_OUTCOME', 'dob_student', 'date', None),
        ('1', 'LZ_CSV', 'email_student', 'STG_SBAC_ASMT_OUTCOME', 'email_student', 'clean', None),
        ('1', 'LZ_CSV', 'gender_student', 'STG_SBAC_ASMT_OUTCOME', 'gender_student', 'gender', None),
        ('1', 'LZ_CSV', 'grade_asmt', 'STG_SBAC_ASMT_OUTCOME', 'grade_asmt', 'clean', None),
        ('1', 'LZ_CSV', 'grade_enrolled', 'STG_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'clean', None),
        ('1', 'LZ_CSV', 'guid_asmt', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt', 'clean', None),
        ('1', 'LZ_CSV', 'guid_asmt_location', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt_location', 'clean', None),
        ('1', 'LZ_CSV', 'guid_district', 'STG_SBAC_ASMT_OUTCOME', 'guid_district', 'clean', None),
        ('1', 'LZ_CSV', 'guid_school', 'STG_SBAC_ASMT_OUTCOME', 'guid_school', 'clean', None),
        ('1', 'LZ_CSV', 'guid_student', 'STG_SBAC_ASMT_OUTCOME', 'guid_student', 'clean', None),
        ('1', 'LZ_CSV', 'name_asmt_location', 'STG_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'clean', None),
        ('1', 'LZ_CSV', 'name_district', 'STG_SBAC_ASMT_OUTCOME', 'name_district', 'clean', None),
        ('1', 'LZ_CSV', 'name_school', 'STG_SBAC_ASMT_OUTCOME', 'name_school', 'clean', None),
        ('1', 'LZ_CSV', 'name_state', 'STG_SBAC_ASMT_OUTCOME', 'name_state', 'clean', None),
        ('1', 'LZ_CSV', 'name_student_first', 'STG_SBAC_ASMT_OUTCOME', 'name_student_first', 'clean', None),
        ('1', 'LZ_CSV', 'name_student_last', 'STG_SBAC_ASMT_OUTCOME', 'name_student_last', 'clean', None),
        ('1', 'LZ_CSV', 'name_student_middle', 'STG_SBAC_ASMT_OUTCOME', 'name_student_middle', 'clean', None),
        ('1', 'LZ_CSV', 'score_asmt', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt', 'clean', None),
        ('1', 'LZ_CSV', 'score_asmt_max', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'clean', None),
        ('1', 'LZ_CSV', 'score_asmt_min', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_1', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_1_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_1_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'clean', None),
        ('1', 'LZ_CSV', 'asmt_claim_1_perf_lvl', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_1_perf_lvl', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_2', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_2_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_2_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'clean', None),
        ('1', 'LZ_CSV', 'asmt_claim_2_perf_lvl', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_2_perf_lvl', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_3_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_3_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'clean', None),
        ('1', 'LZ_CSV', 'asmt_claim_3_perf_lvl', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_3_perf_lvl', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_4', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_4_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'clean', None),
        ('1', 'LZ_CSV', 'score_claim_4_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'clean', None),
        ('1', 'LZ_CSV', 'asmt_claim_4_perf_lvl', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_4_perf_lvl', 'clean', None),
        ('1', 'LZ_CSV', 'score_perf_level', 'STG_SBAC_ASMT_OUTCOME', 'score_perf_level', 'clean', None),
        ('1', 'LZ_CSV', 'type_school', 'STG_SBAC_ASMT_OUTCOME', 'type_school', 'schoolType', None),
        ('1', 'LZ_CSV', 'dmg_eth_hsp', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_eth_ami', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_eth_asn', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_eth_blk', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_eth_pcf', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_eth_wht', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_prg_iep', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_prg_lep', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_prg_504', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'yn', None),
        ('1', 'LZ_CSV', 'dmg_prg_tt1', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'yn', None),
        ('1', 'LZ_CSV', 'asmt_type', 'STG_SBAC_ASMT_OUTCOME', 'asmt_type', 'asmtType', None),
        ('1', 'LZ_CSV', 'asmt_subject', 'STG_SBAC_ASMT_OUTCOME', 'asmt_subject', 'subjectType', None),
        ('1', 'LZ_CSV', 'asmt_year', 'STG_SBAC_ASMT_OUTCOME', 'asmt_year', 'clean', None),
        ('1', 'LZ_CSV', 'acc_asl_video_embed', 'STG_SBAC_ASMT_OUTCOME', 'acc_asl_video_embed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_asl_human_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_asl_human_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_braile_embed', 'STG_SBAC_ASMT_OUTCOME', 'acc_braile_embed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_closed_captioning_embed', 'STG_SBAC_ASMT_OUTCOME', 'acc_closed_captioning_embed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_text_to_speech_embed', 'STG_SBAC_ASMT_OUTCOME', 'acc_text_to_speech_embed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_abacus_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_abacus_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_alternate_response_options_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_alternate_response_options_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_calculator_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_calculator_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_multiplication_table_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_multiplication_table_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_print_on_demand_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_print_on_demand_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_read_aloud_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_read_aloud_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_scribe_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_scribe_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_speech_to_text_nonembed', 'STG_SBAC_ASMT_OUTCOME', 'acc_speech_to_text_nonembed', 'clean', None),
        ('1', 'LZ_CSV', 'acc_streamline_mode', 'STG_SBAC_ASMT_OUTCOME', 'acc_streamline_mode', 'clean', None),
        # Staging to Integration
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_batch', 'INT_SBAC_ASMT_OUTCOME', 'guid_batch', None, None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt_location', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt_location', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'INT_SBAC_ASMT_OUTCOME', 'name_asmt_location', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'grade_asmt', 'INT_SBAC_ASMT_OUTCOME', 'grade_asmt', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_state', 'INT_SBAC_ASMT_OUTCOME', 'name_state', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'code_state', 'INT_SBAC_ASMT_OUTCOME', 'code_state', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_district', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_district', 'INT_SBAC_ASMT_OUTCOME', 'name_district', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_school', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_school', 'INT_SBAC_ASMT_OUTCOME', 'name_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'type_school', 'INT_SBAC_ASMT_OUTCOME', 'type_school', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_student', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_first', 'INT_SBAC_ASMT_OUTCOME', 'name_student_first', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_middle', 'INT_SBAC_ASMT_OUTCOME', 'name_student_middle', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_last', 'INT_SBAC_ASMT_OUTCOME', 'name_student_last', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line1', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line1', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line2', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line2', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_city', 'INT_SBAC_ASMT_OUTCOME', 'address_student_city', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_zip', 'INT_SBAC_ASMT_OUTCOME', 'address_student_zip', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'gender_student', 'INT_SBAC_ASMT_OUTCOME', 'gender_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'email_student', 'INT_SBAC_ASMT_OUTCOME', 'email_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dob_student', 'INT_SBAC_ASMT_OUTCOME', 'dob_student', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_day', None, "extract(day from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_month', None, "extract(month from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_year', None, "extract(year from to_date({src_column}, 'YYYYMMDD'))"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_min', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_max', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_perf_level', 'INT_SBAC_ASMT_OUTCOME', 'score_perf_level', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_min', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_max', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_1_perf_lvl', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_1_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_min', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_max', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_2_perf_lvl', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_2_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_min', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_max', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_3_perf_lvl', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_3_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_min', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_max', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_claim_4_perf_lvl', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_4_perf_lvl', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'created_date', 'INT_SBAC_ASMT_OUTCOME', 'created_date', None, None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_type', 'INT_SBAC_ASMT_OUTCOME', 'asmt_type', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_subject', 'INT_SBAC_ASMT_OUTCOME', 'asmt_subject', None, 'substr({src_column}, 1, {length})'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'asmt_year', 'INT_SBAC_ASMT_OUTCOME', 'asmt_year', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_504', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', None, 'cast({src_column} as bool)'),
        ('3', 'STG_SBAC_ASMT_OUTCOME', "dmg_eth_blk, dmg_eth_asn, dmg_eth_hsp, dmg_eth_ami, dmg_eth_pcf, dmg_eth_wht", 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_derived', 'deriveEthnicity', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_asl_video_embed', 'INT_SBAC_ASMT_OUTCOME', 'acc_asl_video_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_asl_human_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_asl_human_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_braile_embed', 'INT_SBAC_ASMT_OUTCOME', 'acc_braile_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_closed_captioning_embed', 'INT_SBAC_ASMT_OUTCOME', 'acc_closed_captioning_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_text_to_speech_embed', 'INT_SBAC_ASMT_OUTCOME', 'acc_text_to_speech_embed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_abacus_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_abacus_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_alternate_response_options_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_alternate_response_options_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_calculator_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_calculator_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_multiplication_table_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_multiplication_table_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_print_on_demand_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_print_on_demand_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_read_aloud_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_read_aloud_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_scribe_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_scribe_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_speech_to_text_nonembed', 'INT_SBAC_ASMT_OUTCOME', 'acc_speech_to_text_nonembed', None, "to_number({src_column}, '99999')"),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'acc_streamline_mode', 'INT_SBAC_ASMT_OUTCOME', 'acc_streamline_mode', None, "to_number({src_column}, '99999')"),
        # Integration to Target
        ('4', 'INT_SBAC_ASMT', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_asmt', 'asmt_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT', 'guid_asmt', 'dim_asmt', 'asmt_guid', None, None),
        ('4', 'INT_SBAC_ASMT', 'type', 'dim_asmt', 'asmt_type', None, None),
        ('4', 'INT_SBAC_ASMT', 'period', 'dim_asmt', 'asmt_period', None, None),
        ('4', 'INT_SBAC_ASMT', 'year', 'dim_asmt', 'asmt_period_year', None, None),
        ('4', 'INT_SBAC_ASMT', 'version', 'dim_asmt', 'asmt_version', None, None),
        ('4', 'INT_SBAC_ASMT', 'subject', 'dim_asmt', 'asmt_subject', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_claim_1', 'dim_asmt', 'asmt_claim_1_name', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_claim_2', 'dim_asmt', 'asmt_claim_2_name', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_claim_3', 'dim_asmt', 'asmt_claim_3_name', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_claim_4', 'dim_asmt', 'asmt_claim_4_name', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_perf_lvl_1', 'dim_asmt', 'asmt_perf_lvl_name_1', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_perf_lvl_2', 'dim_asmt', 'asmt_perf_lvl_name_2', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_perf_lvl_3', 'dim_asmt', 'asmt_perf_lvl_name_3', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_perf_lvl_4', 'dim_asmt', 'asmt_perf_lvl_name_4', None, None),
        ('4', 'INT_SBAC_ASMT', 'name_perf_lvl_5', 'dim_asmt', 'asmt_perf_lvl_name_5', None, None),
        ('4', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_1', 'dim_asmt', 'asmt_claim_perf_lvl_name_1', None, None),
        ('4', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_2', 'dim_asmt', 'asmt_claim_perf_lvl_name_2', None, None),
        ('4', 'INT_SBAC_ASMT', 'asmt_claim_perf_lvl_name_3', 'dim_asmt', 'asmt_claim_perf_lvl_name_3', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_overall_min', 'dim_asmt', 'asmt_score_min', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_overall_max', 'dim_asmt', 'asmt_score_max', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_1_min', 'dim_asmt', 'asmt_claim_1_score_min', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_1_max', 'dim_asmt', 'asmt_claim_1_score_max', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_1_weight', 'dim_asmt', 'asmt_claim_1_score_weight', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_2_min', 'dim_asmt', 'asmt_claim_2_score_min', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_2_max', 'dim_asmt', 'asmt_claim_2_score_max', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_2_weight', 'dim_asmt', 'asmt_claim_2_score_weight', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_3_min', 'dim_asmt', 'asmt_claim_3_score_min', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_3_max', 'dim_asmt', 'asmt_claim_3_score_max', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_3_weight', 'dim_asmt', 'asmt_claim_3_score_weight', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_4_min', 'dim_asmt', 'asmt_claim_4_score_min', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_4_max', 'dim_asmt', 'asmt_claim_4_score_max', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_claim_4_weight', 'dim_asmt', 'asmt_claim_4_score_weight', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_cut_point_1', 'dim_asmt', 'asmt_cut_point_1', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_cut_point_2', 'dim_asmt', 'asmt_cut_point_2', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_cut_point_3', 'dim_asmt', 'asmt_cut_point_3', None, None),
        ('4', 'INT_SBAC_ASMT', 'score_cut_point_4', 'dim_asmt', 'asmt_cut_point_4', None, None),
        ('4', 'INT_SBAC_ASMT', "TO_CHAR(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_asmt', 'from_date', None, None),
        ('4', 'INT_SBAC_ASMT', "'99991231'", 'dim_asmt', 'to_date', None, None),
        ('4', 'INT_SBAC_ASMT', 'TRUE', 'dim_asmt', 'most_recent', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_inst_hier', 'inst_hier_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_state', 'dim_inst_hier', 'state_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'dim_inst_hier', 'state_code', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'dim_inst_hier', 'district_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_district', 'dim_inst_hier', 'district_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'dim_inst_hier', 'school_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_school', 'dim_inst_hier', 'school_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'type_school', 'dim_inst_hier', 'school_category', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_inst_hier', 'from_date', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "'99991231'", 'dim_inst_hier', 'to_date', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_inst_hier', 'most_recent', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_student', 'student_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', 'dim_student', 'student_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_first', 'dim_student', 'first_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_middle', 'dim_student', 'middle_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_last', 'dim_student', 'last_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line1', 'dim_student', 'address_1', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line2', 'dim_student', 'address_2', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_city', 'dim_student', 'city', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_zip', 'dim_student', 'zip_code', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'gender_student', 'dim_student', 'gender', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'email_student', 'dim_student', 'email', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dob_student', 'dim_student', 'dob', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "''", 'dim_student', 'section_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'dim_student', 'grade', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'dim_student', 'state_code', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'dim_student', 'district_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'dim_student', 'school_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP,'yyyymmdd')", 'dim_student', 'from_date', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "'99991231'", 'dim_student', 'to_date', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_student', 'most_recent', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'fact_asmt_outcome', 'asmnt_outcome_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', None, 'fact_asmt_outcome', 'asmt_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', 'fact_asmt_outcome', 'student_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'fact_asmt_outcome', 'state_code', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'fact_asmt_outcome', 'district_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'fact_asmt_outcome', 'school_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', '-1', 'fact_asmt_outcome', 'student_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "''", 'fact_asmt_outcome', 'section_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', '-1', 'fact_asmt_outcome', 'inst_hier_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', None, 'fact_asmt_outcome', 'section_rec_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt_location', 'fact_asmt_outcome', 'where_taken_id', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'fact_asmt_outcome', 'where_taken_name', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_asmt', 'fact_asmt_outcome', 'asmt_grade', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'fact_asmt_outcome', 'enrl_grade', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', 'fact_asmt_outcome', 'date_taken', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_day', 'fact_asmt_outcome', 'date_taken_day', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_month', 'fact_asmt_outcome', 'date_taken_month', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_year', 'fact_asmt_outcome', 'date_taken_year', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt', 'fact_asmt_outcome', 'asmt_score', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'fact_asmt_outcome', 'asmt_score_range_min', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'fact_asmt_outcome', 'asmt_score_range_max', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_perf_level', 'fact_asmt_outcome', 'asmt_perf_lvl', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1', 'fact_asmt_outcome', 'asmt_claim_1_score', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'fact_asmt_outcome', 'asmt_claim_1_score_range_min', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'fact_asmt_outcome', 'asmt_claim_1_score_range_max', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_1_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_1_perf_lvl', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2', 'fact_asmt_outcome', 'asmt_claim_2_score', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'fact_asmt_outcome', 'asmt_claim_2_score_range_min', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'fact_asmt_outcome', 'asmt_claim_2_score_range_max', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_2_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_2_perf_lvl', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3', 'fact_asmt_outcome', 'asmt_claim_3_score', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'fact_asmt_outcome', 'asmt_claim_3_score_range_min', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'fact_asmt_outcome', 'asmt_claim_3_score_range_max', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_3_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_3_perf_lvl', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4', 'fact_asmt_outcome', 'asmt_claim_4_score', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'fact_asmt_outcome', 'asmt_claim_4_score_range_min', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'fact_asmt_outcome', 'asmt_claim_4_score_range_max', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_claim_4_perf_lvl', 'fact_asmt_outcome', 'asmt_claim_4_perf_lvl', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "''", 'fact_asmt_outcome', 'status', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'fact_asmt_outcome', 'most_recent', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_batch', 'fact_asmt_outcome', 'batch_guid', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_type', 'fact_asmt_outcome', 'asmt_type', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_subject', 'fact_asmt_outcome', 'asmt_subject', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'asmt_year', 'fact_asmt_outcome', 'asmt_year', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'gender_student', 'fact_asmt_outcome', 'gender', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'fact_asmt_outcome', 'dmg_eth_hsp', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'fact_asmt_outcome', 'dmg_eth_ami', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'fact_asmt_outcome', 'dmg_eth_asn', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'fact_asmt_outcome', 'dmg_eth_blk', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'fact_asmt_outcome', 'dmg_eth_pcf', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'fact_asmt_outcome', 'dmg_eth_wht', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'fact_asmt_outcome', 'dmg_prg_iep', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'fact_asmt_outcome', 'dmg_prg_lep', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'fact_asmt_outcome', 'dmg_prg_504', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'fact_asmt_outcome', 'dmg_prg_tt1', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_derived', 'fact_asmt_outcome', 'dmg_eth_derived', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_asl_video_embed', 'fact_asmt_outcome', 'acc_asl_video_embed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_asl_human_nonembed', 'fact_asmt_outcome', 'acc_asl_human_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_braile_embed', 'fact_asmt_outcome', 'acc_braile_embed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_closed_captioning_embed', 'fact_asmt_outcome', 'acc_closed_captioning_embed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_text_to_speech_embed', 'fact_asmt_outcome', 'acc_text_to_speech_embed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_abacus_nonembed', 'fact_asmt_outcome', 'acc_abacus_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_alternate_response_options_nonembed', 'fact_asmt_outcome', 'acc_alternate_response_options_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_calculator_nonembed', 'fact_asmt_outcome', 'acc_calculator_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_multiplication_table_nonembed', 'fact_asmt_outcome', 'acc_multiplication_table_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_print_on_demand_nonembed', 'fact_asmt_outcome', 'acc_print_on_demand_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_read_aloud_nonembed', 'fact_asmt_outcome', 'acc_read_aloud_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_scribe_nonembed', 'fact_asmt_outcome', 'acc_scribe_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_speech_to_text_nonembed', 'fact_asmt_outcome', 'acc_speech_to_text_nonembed', None, None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'acc_streamline_mode', 'fact_asmt_outcome', 'acc_streamline_mode', None, None),
        # Used only in reporting app, smarter.  udl should never pick this up
        ('1000', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt', 'dim_asmt', 'asmt_guid', None, None),
    ]
}
