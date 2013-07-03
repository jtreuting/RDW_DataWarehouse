from udl2_util.measurement import measure_cpu_plus_elasped_time


# transformation rules
CLEAN = 'clean'
CLEAN_UP = 'cleanUpper'
DATE = 'date'
SCHOOL_TY = 'schoolType'
STAFF_TY = 'staffType'
GENDER = 'gender'
YN = 'yn'


ref_table_conf = {
    'column_definitions': ('phase', 'source_table', 'source_column', 'target_table', 'target_column', 'transformation_rule'),
    'column_mappings': [
        # Columns:
        # column_map_key, phase, source_table, source_column, target_table, target_column, transformation_rule, stored_proc_name, stored_proc_created_date, created_date

        # json to int_sbac_asmt
        ('1', 'LZ_JSON', 'identification.guid', 'INT_SBAC_ASMT', 'guid_asmt', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_1.name', 'INT_SBAC_ASMT', 'name_claim_1', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_2.name', 'INT_SBAC_ASMT', 'name_claim_2', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_3.name', 'INT_SBAC_ASMT', 'name_claim_3', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_4.name', 'INT_SBAC_ASMT', 'name_claim_4', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_1.name', 'INT_SBAC_ASMT', 'name_perf_lvl_1', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_2.name', 'INT_SBAC_ASMT', 'name_perf_lvl_2', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_3.name', 'INT_SBAC_ASMT', 'name_perf_lvl_3', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_4.name', 'INT_SBAC_ASMT', 'name_perf_lvl_4', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_5.name', 'INT_SBAC_ASMT', 'name_perf_lvl_5', 'clean'),
        ('1', 'LZ_JSON', 'identification.period', 'INT_SBAC_ASMT', 'period', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_1.max_score', 'INT_SBAC_ASMT', 'score_claim_1_max', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_1.min_score', 'INT_SBAC_ASMT', 'score_claim_1_min', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_1.weight', 'INT_SBAC_ASMT', 'score_claim_1_weight', 'calcWeight'),
        ('1', 'LZ_JSON', 'claims.claim_2.max_score', 'INT_SBAC_ASMT', 'score_claim_2_max', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_2.min_score', 'INT_SBAC_ASMT', 'score_claim_2_min', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_2.weight', 'INT_SBAC_ASMT', 'score_claim_2_weight', 'calcWeight'),
        ('1', 'LZ_JSON', 'claims.claim_3.max_score', 'INT_SBAC_ASMT', 'score_claim_3_max', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_3.min_score', 'INT_SBAC_ASMT', 'score_claim_3_min', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_3.weight', 'INT_SBAC_ASMT', 'score_claim_3_weight', 'calcWeight'),
        ('1', 'LZ_JSON', 'claims.claim_4.max_score', 'INT_SBAC_ASMT', 'score_claim_4_max', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_4.min_score', 'INT_SBAC_ASMT', 'score_claim_4_min', 'clean'),
        ('1', 'LZ_JSON', 'claims.claim_4.weight', 'INT_SBAC_ASMT', 'score_claim_4_weight', 'calcWeight'),
        ('1', 'LZ_JSON', 'performance_levels.level_2.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_1', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_3.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_2', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_4.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_3', 'clean'),
        ('1', 'LZ_JSON', 'performance_levels.level_5.cut_point', 'INT_SBAC_ASMT', 'score_cut_point_4', 'clean'),
        ('1', 'LZ_JSON', 'overall.max_score', 'INT_SBAC_ASMT', 'score_overall_max', 'clean'),
        ('1', 'LZ_JSON', 'overall.min_score', 'INT_SBAC_ASMT', 'score_overall_min', 'clean'),
        ('1', 'LZ_JSON', 'identification.subject', 'INT_SBAC_ASMT', 'subject', 'subjectType'),
        ('1', 'LZ_JSON', 'identification.type', 'INT_SBAC_ASMT', 'type', 'asmtType'),
        ('1', 'LZ_JSON', 'identification.version', 'INT_SBAC_ASMT', 'version', 'clean'),
        ('1', 'LZ_JSON', 'identification.year', 'INT_SBAC_ASMT', 'year', 'clean'),
        # CSV to staging
        ('1', 'LZ_CSV', 'address_student_city', 'STG_SBAC_ASMT_OUTCOME', 'address_student_city', 'clean'),
        ('1', 'LZ_CSV', 'address_student_line1', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line1', 'clean'),
        ('1', 'LZ_CSV', 'address_student_line2', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line2', 'clean'),
        ('1', 'LZ_CSV', 'address_student_zip', 'STG_SBAC_ASMT_OUTCOME', 'address_student_zip', 'clean'),
        ('1', 'LZ_CSV', 'code_state', 'STG_SBAC_ASMT_OUTCOME', 'code_state', 'cleanUpper'),
        ('1', 'LZ_CSV', 'date_assessed', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'date'),
        ('1', 'LZ_CSV', 'dob_student', 'STG_SBAC_ASMT_OUTCOME', 'dob_student', 'date'),
        ('1', 'LZ_CSV', 'email_student', 'STG_SBAC_ASMT_OUTCOME', 'email_student', 'clean'),
        ('1', 'LZ_CSV', 'gender_student', 'STG_SBAC_ASMT_OUTCOME', 'gender_student', 'gender'),
        ('1', 'LZ_CSV', 'grade_asmt', 'STG_SBAC_ASMT_OUTCOME', 'grade_asmt', 'clean'),
        ('1', 'LZ_CSV', 'grade_enrolled', 'STG_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'clean'),
        ('1', 'LZ_CSV', 'guid_asmt', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt', 'clean'),
        ('1', 'LZ_CSV', 'guid_asmt_location', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt_location', 'clean'),
        ('1', 'LZ_CSV', 'guid_district', 'STG_SBAC_ASMT_OUTCOME', 'guid_district', 'clean'),
        ('1', 'LZ_CSV', 'guid_school', 'STG_SBAC_ASMT_OUTCOME', 'guid_school', 'clean'),
        ('1', 'LZ_CSV', 'guid_staff', 'STG_SBAC_ASMT_OUTCOME', 'guid_staff', 'clean'),
        ('1', 'LZ_CSV', 'guid_student', 'STG_SBAC_ASMT_OUTCOME', 'guid_student', 'clean'),
        ('1', 'LZ_CSV', 'name_asmt_location', 'STG_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'clean'),
        ('1', 'LZ_CSV', 'name_district', 'STG_SBAC_ASMT_OUTCOME', 'name_district', 'clean'),
        ('1', 'LZ_CSV', 'name_school', 'STG_SBAC_ASMT_OUTCOME', 'name_school', 'clean'),
        ('1', 'LZ_CSV', 'name_staff_first', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_first', 'clean'),
        ('1', 'LZ_CSV', 'name_staff_last', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_last', 'clean'),
        ('1', 'LZ_CSV', 'name_staff_middle', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_middle', 'clean'),
        ('1', 'LZ_CSV', 'name_state', 'STG_SBAC_ASMT_OUTCOME', 'name_state', 'clean'),
        ('1', 'LZ_CSV', 'name_student_first', 'STG_SBAC_ASMT_OUTCOME', 'name_student_first', 'clean'),
        ('1', 'LZ_CSV', 'name_student_last', 'STG_SBAC_ASMT_OUTCOME', 'name_student_last', 'clean'),
        ('1', 'LZ_CSV', 'name_student_middle', 'STG_SBAC_ASMT_OUTCOME', 'name_student_middle', 'clean'),
        ('1', 'LZ_CSV', 'score_asmt', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt', 'clean'),
        ('1', 'LZ_CSV', 'score_asmt_max', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'clean'),
        ('1', 'LZ_CSV', 'score_asmt_min', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_1', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_1_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_1_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_2', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_2_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_2_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_3_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_3_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_4', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_4_max', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'clean'),
        ('1', 'LZ_CSV', 'score_claim_4_min', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'clean'),
        ('1', 'LZ_CSV', 'score_perf_level', 'STG_SBAC_ASMT_OUTCOME', 'score_perf_level', 'clean'),
        ('1', 'LZ_CSV', 'type_school', 'STG_SBAC_ASMT_OUTCOME', 'type_school', 'schoolType'),
        ('1', 'LZ_CSV', 'type_staff', 'STG_SBAC_ASMT_OUTCOME', 'type_staff', 'staffType'),
        ('1', 'LZ_CSV', 'dmg_eth_hsp', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'yn'),
        ('1', 'LZ_CSV', 'dmg_eth_ami', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'yn'),
        ('1', 'LZ_CSV', 'dmg_eth_asn', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'yn'),
        ('1', 'LZ_CSV', 'dmg_eth_blk', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'yn'),
        ('1', 'LZ_CSV', 'dmg_eth_pcf', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'yn'),
        ('1', 'LZ_CSV', 'dmg_eth_wht', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'yn'),
        ('1', 'LZ_CSV', 'dmg_prg_iep', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'yn'),
        ('1', 'LZ_CSV', 'dmg_prg_lep', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'yn'),
        ('1', 'LZ_CSV', 'dmg_prg_504', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'yn'),
        ('1', 'LZ_CSV', 'dmg_prg_tt1', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'yn'),
        # Staging to Integration
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'batch_id', 'INT_SBAC_ASMT_OUTCOME', 'batch_id', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_asmt_location', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt_location', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'INT_SBAC_ASMT_OUTCOME', 'name_asmt_location', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'grade_asmt', 'INT_SBAC_ASMT_OUTCOME', 'grade_asmt', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_state', 'INT_SBAC_ASMT_OUTCOME', 'name_state', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'code_state', 'INT_SBAC_ASMT_OUTCOME', 'code_state', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_district', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_district', 'INT_SBAC_ASMT_OUTCOME', 'name_district', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_school', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_school', 'INT_SBAC_ASMT_OUTCOME', 'name_school', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'type_school', 'INT_SBAC_ASMT_OUTCOME', 'type_school', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_student', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_first', 'INT_SBAC_ASMT_OUTCOME', 'name_student_first', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_middle', 'INT_SBAC_ASMT_OUTCOME', 'name_student_middle', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_student_last', 'INT_SBAC_ASMT_OUTCOME', 'name_student_last', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line1', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line1', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_line2', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line2', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_city', 'INT_SBAC_ASMT_OUTCOME', 'address_student_city', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'address_student_zip', 'INT_SBAC_ASMT_OUTCOME', 'address_student_zip', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'gender_student', 'INT_SBAC_ASMT_OUTCOME', 'gender_student', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'email_student', 'INT_SBAC_ASMT_OUTCOME', 'email_student', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dob_student', 'INT_SBAC_ASMT_OUTCOME', 'dob_student', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_assessed', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_taken_day', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_taken_month', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'date_taken_year', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_min', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_max', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_perf_level', 'INT_SBAC_ASMT_OUTCOME', 'score_perf_level', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_min', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_max', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_min', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_max', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_min', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_max', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_min', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_max', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'guid_staff', 'INT_SBAC_ASMT_OUTCOME', 'guid_staff', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_first', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_first', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_middle', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_middle', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'name_staff_last', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_last', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'type_staff', 'INT_SBAC_ASMT_OUTCOME', 'type_staff', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'created_date', 'INT_SBAC_ASMT_OUTCOME', 'created_date', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_504', None),
        ('3', 'STG_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', None),
        # Integration to Target
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_asmt', 'asmt_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_asmt', 'dim_asmt', 'asmt_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'type', 'dim_asmt', 'asmt_type', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'period', 'dim_asmt', 'asmt_period', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'year', 'dim_asmt', 'asmt_period_year', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'version', 'dim_asmt', 'asmt_version', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'subject', 'dim_asmt', 'asmt_subject', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_claim_1', 'dim_asmt', 'asmt_claim_1_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_claim_2', 'dim_asmt', 'asmt_claim_2_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_claim_3', 'dim_asmt', 'asmt_claim_3_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_claim_4', 'dim_asmt', 'asmt_claim_4_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_perf_lvl_1', 'dim_asmt', 'asmt_perf_lvl_name_1', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_perf_lvl_2', 'dim_asmt', 'asmt_perf_lvl_name_2', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_perf_lvl_3', 'dim_asmt', 'asmt_perf_lvl_name_3', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_perf_lvl_4', 'dim_asmt', 'asmt_perf_lvl_name_4', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_perf_lvl_5', 'dim_asmt', 'asmt_perf_lvl_name_5', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_overall_min', 'dim_asmt', 'asmt_score_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_overall_max', 'dim_asmt', 'asmt_score_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'dim_asmt', 'asmt_claim_1_score_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'dim_asmt', 'asmt_claim_1_score_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_weight', 'dim_asmt', 'asmt_claim_1_score_weight', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'dim_asmt', 'asmt_claim_2_score_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'dim_asmt', 'asmt_claim_2_score_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_weight', 'dim_asmt', 'asmt_claim_2_score_weight', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'dim_asmt', 'asmt_claim_3_score_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'dim_asmt', 'asmt_claim_3_score_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_weight', 'dim_asmt', 'asmt_claim_3_score_weight', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'dim_asmt', 'asmt_claim_4_score_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'dim_asmt', 'asmt_claim_4_score_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_weight', 'dim_asmt', 'asmt_claim_4_score_weight', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_cut_point_1', 'dim_asmt', 'asmt_cut_point_1', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_cut_point_2', 'dim_asmt', 'asmt_cut_point_2', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_cut_point_3', 'dim_asmt', 'asmt_cut_point_3', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_cut_point_4', 'dim_asmt', 'asmt_cut_point_4', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'NULL', 'dim_asmt', 'asmt_custom_metadata', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "TO_CHAR(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_asmt', 'from_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "99991231'", 'dim_asmt', 'to_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_asmt', 'most_recent', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_inst_hier', 'inst_hier_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_state', 'dim_inst_hier', 'state_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'dim_inst_hier', 'state_code', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'dim_inst_hier', 'district_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_district', 'dim_inst_hier', 'district_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'dim_inst_hier', 'school_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_school', 'dim_inst_hier', 'school_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'type_school', 'dim_inst_hier', 'school_category', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_inst_hier', 'from_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "'99991231'", 'dim_inst_hier', 'to_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_inst_hier', 'most_recent', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'""GLOBAL_REC_SEQ""\')', 'dim_student', 'student_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', 'dim_student', 'student_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_first', 'dim_student', 'first_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_middle', 'dim_student', 'middle_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_student_last', 'dim_student', 'last_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line1', 'dim_student', 'address_1', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_line2', 'dim_student', 'address_2', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_city', 'dim_student', 'city', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'address_student_zip', 'dim_student', 'zip_code', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'gender_student', 'dim_student', 'gender', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'email_student', 'dim_student', 'email', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dob_student', 'dim_student', 'dob', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "' '", 'dim_student', 'section_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'dim_student', 'grade', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'dim_student', 'state_code', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'dim_student', 'district_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'dim_student', 'school_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP', 'yyyymmdd')", 'dim_student', 'from_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "'99991231'", 'dim_student', 'to_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_student', 'most_recent', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'dim_staff', 'staff_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_staff', 'dim_staff', 'staff_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_first', 'dim_staff', 'first_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_middle', 'dim_staff', 'middle_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_staff_last', 'dim_staff', 'last_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "' '", 'dim_staff', 'section_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'type_staff', 'dim_staff', 'hier_user_type', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'dim_staff', 'state_code', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'dim_staff', 'district_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'dim_staff', 'school_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP, 'yyyymmdd')", 'dim_staff', 'from_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "99991231'", 'dim_staff', 'to_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'dim_staff', 'most_recent', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'nextval(\'"GLOBAL_REC_SEQ"\')', 'fact_asmt_outcome', 'asmnt_outcome_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', None, 'fact_asmt_outcome', 'asmt_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_student', 'fact_asmt_outcome', 'student_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_staff', 'fact_asmt_outcome', 'teacher_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'code_state', 'fact_asmt_outcome', 'state_code', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_district', 'fact_asmt_outcome', 'district_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'guid_school', 'fact_asmt_outcome', 'school_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "' '", 'fact_asmt_outcome', 'section_guid', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', '-1', 'fact_asmt_outcome', 'inst_hier_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', None, 'fact_asmt_outcome', 'section_rec_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'fact_asmt_outcome', 'where_taken_id', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'name_asmt_location', 'fact_asmt_outcome', 'where_taken_name', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_asmt', 'fact_asmt_outcome', 'asmt_grade', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'grade_enrolled', 'fact_asmt_outcome', 'enrl_grade', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_assessed', 'fact_asmt_outcome', 'date_taken', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_day', 'fact_asmt_outcome', 'date_taken_day', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_month', 'fact_asmt_outcome', 'date_taken_month', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'date_taken_year', 'fact_asmt_outcome', 'date_taken_year', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt', 'fact_asmt_outcome', 'asmt_score', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_min', 'fact_asmt_outcome', 'asmt_score_range_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_asmt_max', 'fact_asmt_outcome', 'asmt_score_range_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_perf_level', 'fact_asmt_outcome', 'asmt_perf_lvl', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1', 'fact_asmt_outcome', 'asmt_claim_1_score', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_min', 'fact_asmt_outcome', 'asmt_claim_1_score_range_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_1_max', 'fact_asmt_outcome', 'asmt_claim_1_score_range_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2', 'fact_asmt_outcome', 'asmt_claim_2_score', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_min', 'fact_asmt_outcome', 'asmt_claim_2_score_range_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_2_max', 'fact_asmt_outcome', 'asmt_claim_2_score_range_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3', 'fact_asmt_outcome', 'asmt_claim_3_score', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_min', 'fact_asmt_outcome', 'asmt_claim_3_score_range_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_3_max', 'fact_asmt_outcome', 'asmt_claim_3_score_range_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4', 'fact_asmt_outcome', 'asmt_claim_4_score', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_min', 'fact_asmt_outcome', 'asmt_claim_4_score_range_min', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'score_claim_4_max', 'fact_asmt_outcome', 'asmt_claim_4_score_range_max', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "to_char(CURRENT_TIMESTAMP', 'yyyymmdd')", 'fact_asmt_outcome', 'asmt_create_date', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', "' '", 'fact_asmt_outcome', 'status', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'TRUE', 'fact_asmt_outcome', 'most_recent', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_hsp', 'fact_asmt_outcome', 'dmg_eth_hsp', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_ami', 'fact_asmt_outcome', 'dmg_eth_ami', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_asn', 'fact_asmt_outcome', 'dmg_eth_asn', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_blk', 'fact_asmt_outcome', 'dmg_eth_blk', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_pcf', 'fact_asmt_outcome', 'dmg_eth_pcf', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_eth_wht', 'fact_asmt_outcome', 'dmg_eth_wht', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_iep', 'fact_asmt_outcome', 'dmg_prg_iep', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_lep', 'fact_asmt_outcome', 'dmg_prg_lep', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_504', 'fact_asmt_outcome', 'dmg_prg_504', None),
        ('4', 'INT_SBAC_ASMT_OUTCOME', 'dmg_prg_tt1', 'fact_asmt_outcome', 'dmg_prg_tt1', None),
    ]
}


if __name__ == '__main__':

    from udl2 import populate_ref_tables
    from udl2_util.database_util import connect_db
    conn, db_engine = connect_db('postgresql', 'udl2', 'udl2abc1234', 'localhost', 5432, 'udl2')
    populate_ref_tables.populate_ref_column_map(ref_table_conf, db_engine, conn, 'udl2', 'REF_COLUMN_MAPPING')
