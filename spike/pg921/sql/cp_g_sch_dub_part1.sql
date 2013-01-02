select dim_student_key
, eternal_student_sid   
, year_sid
, dim_assmt_period_key
, dim_assmt_grade_key
, assmt_code
, assmt_name
, assmt_version_code
, daot_hier_level
, daot_hier_level_code
, daot_hier_level_name          
, daot_hier_level_rank
, daot.daot_hier_level_1_code 
, daot.daot_hier_level_1_name
, daot.daot_hier_level_1_abbrev     
, daot.daot_hier_level_2_code 
, daot.daot_hier_level_2_name
, daot.daot_hier_level_2_abbrev
, daot.daot_hier_level_3_code 
, daot.daot_hier_level_3_name
, daot.daot_hier_level_3_abbrev
, daot.daot_hier_level_4_code 
, daot.daot_hier_level_4_name
, daot.daot_hier_level_4_abbrev
, daot.daot_hier_level_5_code 
, daot.daot_hier_level_5_name
, daot.daot_hier_level_5_abbrev
, dim_perf_level_key
--, (case when performance_level_flag then 1 else 0 end) performance_level_flag
from edware.fact_assmt_outcome fao
join edware.dim_assmt_outcome_type daot
  on fao.dim_assmt_outcome_type_key  = daot.dim_assmt_outcome_type_key
 and daot.daot_hier_level_code    in ('2')
 and daot.assmt_code         in ('7')
 and case
       when daot.assmt_code = '706' then true
       when daot.assmt_code = '706s' then true
       else (daot.assmt_version_code in ('1'))
     end
 and  case 
        when daot.daot_hier_level = 1 then daot.daot_hier_level_1_code 
        when daot.daot_hier_level = 2 then daot.daot_hier_level_2_code 
        when daot.daot_hier_level = 3 then daot.daot_hier_level_3_code 
        when daot.daot_hier_level = 4 then daot.daot_hier_level_4_code 
        when daot.daot_hier_level = 5 then daot.daot_hier_level_5_code 
      end in ('INSTREC')
where fao.assmt_instance_rank=1 -- avoid duplicate assmt results in the same period
and fao.year_sid in ('8')
and daot.daot_measure_type_code = 'BM_AM'
limit 10
;
