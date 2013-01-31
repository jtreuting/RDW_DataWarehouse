from pyramid.response import Response
from pyramid.view import view_config
from smarter.services.comparepopulations import generateComparePopulationsReport, generateComparePopulationsReportAlchemy
from smarter.services.compare_populations import generateComparePopulationsJSON
from sqlalchemy.exc import DBAPIError
from smarter.controllers import compare_population_criteria
from smarter.controllers import get_compare_population
import json
import urllib.request
from smarter.utils.indiv_student_helper import IndivStudentHelper
from database import importer
import os
from database.connector import DBConnector, IDbUtil
from edschema.ed_metadata import generate_ed_metadata
from zope import component


@view_config(route_name='comparing_populations', renderer='templates/comparing_populations.pt')
def compPop_view(request):
    example_json = """\
{"scope_groups": [{"school_group": {"code": 625, "name": "ALSchoolGroup1"}, "school_group_type": {"code": "Districts", "name": "Districts"}, "school": null, "teacher": null, "grade_groups": [{"bar_groups": [{"student": null, "teacher": {"code": 2077, "name": "COPELAND, JOHN"}, "school_group": {"code": 625, "name": "ALSchoolGroup1"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 63, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 65, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 66, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 59, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 61, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 6405, "name": "School258"}, "grade": null}], "grade": null}]}, {"school_group": {"code": 634, "name": "ALSchoolGroup10"}, "school_group_type": {"code": "Districts", "name": "Districts"}, "school": null, "teacher": null, "grade_groups": [{"bar_groups": [{"student": null, "teacher": {"code": 2334, "name": "SHARP, CRYSTAL"}, "school_group": {"code": 634, "name": "ALSchoolGroup10"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 75, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 48, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 45, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 61, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 6419, "name": "School1464"}, "grade": null}], "grade": null}]}, {"school_group": {"code": 724, "name": "ALSchoolGroup100"}, "school_group_type": {"code": "Districts", "name": "Districts"}, "school": null, "teacher": null, "grade_groups": [{"bar_groups": [{"student": null, "teacher": {"code": 3231, "name": "BROWN, BEULAH"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 75, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 83, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 66, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 64, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 64, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 57, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7732, "name": "School1568"}, "grade": null}, {"student": null, "teacher": {"code": 3066, "name": "CAMPBELL, KAY"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 74, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 40, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 51, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 62, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 63, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 44, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7731, "name": "School604"}, "grade": null}, {"student": null, "teacher": {"code": 2035, "name": "CANNON, JAMES"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 28, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 51, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 28, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 45, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 25, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 92, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7726, "name": "School200"}, "grade": null}, {"student": null, "teacher": {"code": 2063, "name": "DRAKE, JOHN"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 57, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 34, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 61, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 38, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 35, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 45, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7727, "name": "School326"}, "grade": null}, {"student": null, "teacher": {"code": 2860, "name": "GREER, STEPHANIE"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 57, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 94, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 48, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 42, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 27, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 88, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7738, "name": "School389"}, "grade": null}, {"student": null, "teacher": {"code": 1894, "name": "HERNANDEZ, JAMES"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 73, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 61, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 51, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 71, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 36, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 77, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7737, "name": "School1358"}, "grade": null}, {"student": null, "teacher": {"code": 15, "name": "HORN, EDWIN"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 89, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 42, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 66, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 81, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 76, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7742, "name": "School679"}, "grade": null}, {"student": null, "teacher": {"code": 2994, "name": "JOHNSTON, SHARON"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 43, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 77, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 20, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 54, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 78, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 40, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7729, "name": "School1473"}, "grade": null}, {"student": null, "teacher": {"code": 282, "name": "MANNING, VIRGIL"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 62, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 62, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 64, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 60, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7725, "name": "School901"}, "grade": null}, {"student": null, "teacher": {"code": 1038, "name": "NICHOLSON, GREGORY"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 58, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 58, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 49, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 79, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 59, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 78, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7741, "name": "School1517"}, "grade": null}, {"student": null, "teacher": {"code": 789, "name": "OLIVER, DENNIS"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 46, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 64, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 53, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 53, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 47, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 77, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7730, "name": "School725"}, "grade": null}, {"student": null, "teacher": {"code": 3096, "name": "PETERSON, NORMA"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 38, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 58, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 98, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 59, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 75, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 54, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7739, "name": "School1207"}, "grade": null}, {"student": null, "teacher": {"code": 775, "name": "QUINN, TOM"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 70, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 38, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 71, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 67, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 40, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 52, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7735, "name": "School367"}, "grade": null}, {"student": null, "teacher": {"code": 626, "name": "RAMIREZ, MARVIN"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 62, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 84, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 37, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 31, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 54, "performance_level": {"code": "2", "name": "Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 88, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7736, "name": "School1535"}, "grade": null}, {"student": null, "teacher": {"code": 2799, "name": "ROBERTS, ARLENE"}, "school_group": {"code": 724, "name": "ALSchoolGroup100"}, "bars": [{"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 88, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "EOY"}, "student_count": 1, "segments": [{"score": 84, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "MOY"}, "student_count": 1, "segments": [{"score": 61, "performance_level": {"code": "3", "name": "Above Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2012-2013"}}, {"period": {"code": null, "name": "BOY"}, "student_count": 1, "segments": [{"score": 27, "performance_level": {"code": "1", "name": "Below Benchmark"}, "student_percentage": 100, "student_count": 1}], "year": {"code": null, "name": "2013-2014"}}], "school": {"code": 7740, "name": "School1202"}, "grade": null}], "grade": null}]}]}
"""
    return {'json': example_json}


@view_config(route_name='home', renderer='templates/common.pt')
def home_view(request):
    try:
        one = 'haha'  # DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response("wrong", content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'smarter2'}


@view_config(route_name='comparepopulation', renderer='templates/compare_population_criteria.pt')
def comparepopulation_view(request):
    comparePopulationCriteria = compare_population_criteria.ComparePopulationCriteria()
    return comparePopulationCriteria.get()
    #return Response("Hello World")


@view_config(route_name='getcomparepopulation', renderer='json')
def getcomparepopulation_view(request):
    getComparePopulation = get_compare_population.GetComparePopulation()
    return getComparePopulation.get()


@view_config(route_name='test1', renderer='json')
def testJson(request):
    mystring = {
        "data": {
            "account": {
                "code": "1209",
                "name": "MCPS Account"
            },
            "scope_groups": {
                "school": "Abc",
                "section": "Xyz",
                "school_group": "Group",
                "grade_groups": "Grade",
                "school_group_type": "Type",
                "teacher": "Def"
            }
        },
        "parameters": {
            "selected_rows": "rows",
            "all": "all",
            "selected": "selected"
        },
        "report_id": 1
    }
    #return Response(mystring)
    return mystring


@view_config(route_name='template', renderer='json')
def my_templateview(request):
    mystring = {
        'data': {
            'account': {
                'code': '1209',
                'name': 'MCPS Account'
            },
            'scope_groups': {
                'school': 'Abc',
                'section': 'Xyz',
                'school_group': 'Group',
                'grade_groups': 'Grade',
                'school_group_type': 'Type',
                'teacher': 'Def'
            }
        },
        'parameters': {
            'selected_rows': 'rows',
            'all': 'all',
            'selected': 'selected'
        },
        'report_id': 1
    }
    #json_str = json.dumps(mystring, sort_keys=True, indent=4)
    #return Response(json.dumps(mystring))
    return mystring


@view_config(route_name='generateComparePopulations', renderer='templates/comparePopulationsResults.pt')
def compare_populations(request):
    return {"result": generateComparePopulationsReport(request.params["reportparam"])}


@view_config(route_name='inputComparePopulations', renderer='templates/comparePopulations.pt')
def input_populations(request):
    return {"comment": "Enter the report parameters"}


@view_config(route_name='generateComparePopulationsAl', renderer='templates/comparePopulationsResultsAl.pt')
def compare_populations_Al(request):
    return {"result": generateComparePopulationsReportAlchemy(request.params["reportparam"])}


@view_config(route_name='inputComparePopulationsAl', renderer='templates/comparePopulationsAl.pt')
def input_populations_Al(request):
    return {"comment": "Enter the report parameters"}


@view_config(route_name='datatojson2', renderer='json')
def compare_populations_json(request):
    print("this is datajson2")
    return Response(str(generateComparePopulationsJSON(request.params["reportparam"])))


@view_config(route_name='inputdata2', renderer='templates/comparePopulationsJson.pt')
def input_populations_json(request):
    return {"comment": "Enter the report parameters to generate json"}


@view_config(route_name='checkstatus', renderer='templates/checkstatus.pt')
def check_status(request):
    return {'result': 'Everything is working fine!'}


# Individual Student Report
@view_config(route_name='indiv_student', renderer='templates/reports/individual_student.pt')
def individual_student_report(request):

    student_id = int(request.params['student'])
    assessment_id = int(request.params['assmt'])

    params = json.dumps({"studentId": student_id})
    params = params.encode('utf-8')

    headers = {}
    headers['Content-Type'] = 'application/json'

    req = urllib.request.Request('http://127.0.0.1:6543/report/student/_query', params, headers)
    res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

    # temporary fix to keep this simple
    # we only want one of the rows returned from the service.
    res = res[0]

    return res


# Bootstrapped Individual Student Report
@view_config(route_name='indiv_student_bootstrap', renderer='templates/reports/individual_student_bootstrap.pt')
def individual_student_report_bootstrap(request):
    helper = IndivStudentHelper()

    params = helper.extract_parameters(request)
    headers = helper.create_header()
    response = helper.get_student_report(params, headers)

    return response


# Class Report
@view_config(route_name='class_report', renderer='templates/reports/class_bootstrap.pt')
def class_report(request):
    return {'class_name': 'English'}


@view_config(route_name='import', renderer='json')
def import_table(request):
    file_name = request.params['file']
    file_path = os.getcwd() + file_name # '/dim_school.csv'
    print(file_path)
    connector = DBConnector()
    importer.import_from_file(file_path, connector)
    return {'imported': True}


@view_config(route_name='create', renderer='json')
def create_tables(request):
    schema_name = request.params['schema']
    metadata = generate_ed_metadata(schema_name)
    createSchema(schema_name)
    dbUtil = component.queryUtility(IDbUtil)
    engine = dbUtil.get_engine()
    metadata.create_all(engine)
    return {'imported': True}


def createSchema(schemaName):
    dbConnect = DBConnector()
    conn = dbConnect.open_connection()
    conn.execute("commit")
    conn.execute("create schema {}".format(schemaName))
    conn.close()
