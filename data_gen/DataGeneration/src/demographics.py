'''
Created on Jul 1, 2013

@author: swimberly
'''

import csv
import random

from generate_names import generate_first_or_middle_name, possibly_generate_middle_name
from entities import Student


H_ID = 0
H_GROUPING = 1
H_SUBJECT = 2
H_GRADE = 3
H_DEMOGRAPHIC = 4
H_COL_NAME = 5
H_TOTAL = 6
H_PERF_1 = 7
H_PERF_2 = 8
H_PERF_3 = 9
H_PERF_4 = 10

L_GROUPING = 0
L_TOTAL = 1
L_PERF_1 = 2
L_PERF_2 = 3
L_PERF_3 = 4
L_PERF_4 = 5

ALL_DEM = 'all'


class Demographics(object):
    '''
    '''

    def __init__(self, demo_csv_file):
        self.dem_data = self._parse_file(demo_csv_file)

    ##*********************************
    ## Public Methods
    ##*********************************

    def get_demo_names(self, dem_id, subject='math', grade='3'):
        ''' return the list of demographics '''

        keys = list(self.dem_data[dem_id][subject][grade].keys())
        if 'all' in keys:
            keys.remove('all')

        return keys

    def assign_demographics(self, asmt_outcomes, students, subject, grade, dem_id, demograph_tracker):
        '''
        Take fact assessment outcomes and apply demographics to the data based on dem_dict
        @param asmt_outcomdes: the list of all the fact assessments that were created
        @param students: the list of student objects to assign demographics
        @param subject: the subject that scores are being assigned for
        @param grade: the grade that scores are being assigned for
        @param dem_id: the demographic id to use for obtaining statistics
        @param demograph_tracker: the object that is keeping track of the student demographics
        '''
        assert len(asmt_outcomes) == len(students)

        # Get the demographics corresponding to the id, subject, grade
        grade_demo = self.get_grade_demographics(dem_id, subject, grade)

        total_students = len(asmt_outcomes)

        # Convert percentages to actual values, based on number of students given
        dem_count_dict = percentages_to_values(grade_demo, total_students)

        # Assign Male and Female Gender
        self._make_male_or_female(dem_count_dict['male'], dem_count_dict['female'], asmt_outcomes, students)

        # Get ordered groupings list
        groupings = sorted({grade_demo[x][L_GROUPING] for x in grade_demo})
        # Removing all and gender
        groupings.remove(0)
        groupings.remove(1)

        # Assign other demographics
        for group in groupings:
            self._make_other_demographics(dem_count_dict, group, asmt_outcomes, students)

        # Add students to demograph tracker
        demograph_tracker.add_many(students)

        return asmt_outcomes, students

    def update_demographics(self, students, asmt_outcomes, dem_id):
        ''' update the asmt_outcomes with the proper demographics '''
        demos_to_update = self.get_demo_names(dem_id)
        if 'male' in demos_to_update:
            demos_to_update.remove('male')
        if 'female' in demos_to_update:
            demos_to_update.remove('female')

        for i in range(len(students)):
            assert students[i].student_guid == asmt_outcomes[i].student_guid

            # loop through demographics and update
            for dm in demos_to_update:
                dm_value = getattr(students[i], dm)
                setattr(asmt_outcomes[i], dm, dm_value)

        return asmt_outcomes

    def get_grade_demographics(self, dem_id, subject, grade):
        '''
        Get the demographic data that corresponds to the provided values
        Data is returned in the following format
        {name: [order, tot_percent, pl1_perc, pl2_perc, pl3_perc, pl4_perc], ... }
        {'female': ['1', '49', '8', '31', '49', '12'], ... }
        @param dem_id: The demographic id found in the data file
        @param subject: the name of the subject
        @param grade: the name of the grade
        @return: A dictionary containing list of all dem data.
        @rtype: dict
        '''
        return self.dem_data[dem_id.lower()][subject.lower()][str(grade)]

    def get_grade_demographics_total(self, dem_id, subject, grade):
        '''
        Return only the performance level percentages for the id, subject and grade
        '''
        grade_demo = self.get_grade_demographics(dem_id, subject, grade)
        total_dem = grade_demo[ALL_DEM][L_PERF_1:L_PERF_4 + 1]
        return total_dem

    def assign_scores_from_demograph(self, students, scores, subject, grade, dem_id, demograph_tracker, assessment):
        '''
        Take a list of students where most will have already been assigned demographics and assign them
        scores for the 2nd subject based on the demographics that they posses
        @param students: The list of students that need scores
        @param score: The list of generated scores
        @param subject: The subject to assign scores for
        @param grade: The students grade
        @param dem_id: The id to use for looking up demographic information
        @param demograph_tracker: the object that is keeping track of the student demographics
        @return: A list of tuples of the form (student_object, score)
        '''
        student_list = []
        score_list = []
        # Get the demographics corresponding to the id, subject, grade
        grade_demo = self.get_grade_demographics(dem_id, subject, grade)

        total_students = len(students)

        # Convert percentages to actual values, based on number of students given
        dem_count_dict = percentages_to_values(grade_demo, total_students)

        # order demographic categories by number of keys present
        keys_by_desired_count = sorted(dem_count_dict, key=lambda k: dem_count_dict[k][L_TOTAL])
        #print('keys_by_desired_count', keys_by_desired_count)

        # Remove the all key
        if 'all' in keys_by_desired_count:
            keys_by_desired_count.remove('all')

        # get dict containing scores
        score_dict = self._divide_scores_into_perf_lvls(scores, assessment)

        for key in keys_by_desired_count:
            students_to_request = dem_count_dict[key][L_TOTAL]
            #print(key, dem_count_dict)

            # Get that number of students
            for _i in range(students_to_request):
                student = demograph_tracker.pop(key)

                if student:
                    perf_level = self._determine_perf_lvl(dem_count_dict[key][L_PERF_1:])
                    score = self._pick_score_in_pl(perf_level, score_dict)
                    dem_count_dict = self._update_dem_counts(student, perf_level, dem_count_dict)
                    student_list.append(student)
                    score_list.append(score)
                else:
                    #print('No student', key, _i, students_to_request)
                    break

        return student_list, score_list

    ##*********************************
    ## Private Methods
    ##*********************************

    def _parse_file(self, file_name):
        '''
        open csv file
        '''

        dem_dict = {}

        with open(file_name) as cfile:
            reader = csv.reader(cfile)

            count = 0
            header = []
            for row in reader:
                if count == 0 and row[0]:
                    header = row
                    count += 1
                elif row[0] and row != header:
                    dem_dict = self._add_row(row, dem_dict)
                    count += 1

        return dem_dict

    def _add_row(self, row_list, dem_dict):
        '''
        Take a row from the csv file and add the data to the demographics dictionary
        '''

        dem_id = row_list[H_ID]

        id_dict = dem_dict.get(dem_id)
        if id_dict:
            subject_dict = id_dict.get(row_list[H_SUBJECT])
            if subject_dict:
                grade_dict = subject_dict.get(row_list[H_GRADE])
                if grade_dict:
                    grade_dict[row_list[H_COL_NAME].lower()] = self._construct_dem_list(row_list)
                else:
                    subject_dict[row_list[H_GRADE].lower()] = {row_list[H_COL_NAME].lower(): self._construct_dem_list(row_list)}
            else:
                id_dict[row_list[H_SUBJECT].lower()] = {row_list[H_GRADE].lower(): {row_list[H_COL_NAME].lower(): self._construct_dem_list(row_list)}}
        else:
            dem_dict[dem_id.lower()] = {row_list[H_SUBJECT].lower(): {row_list[H_GRADE].lower(): {row_list[H_COL_NAME].lower(): self._construct_dem_list(row_list)}}}

        return dem_dict

    def _construct_dem_list(self, row_list):
        '''
        Take a single row from the file and create a demographic dict object
        of the form [GROUPING, TOTAL_PERC, PL1_PERC, PL2_PERC, PL3_PERC, PL4_PERC]
        ie. [1, 20, 20, 40, 20, 20]
        '''
        ret_list = [row_list[H_GROUPING], row_list[H_TOTAL], row_list[H_PERF_1], row_list[H_PERF_2], row_list[H_PERF_3], row_list[H_PERF_4]]
        # convert to ints and return
        return [int(x) for x in ret_list]

    def _update_dem_counts(self, student, perf_lvl, dem_count_dict):
        '''
        update the demographic counts based on the just created student
        '''
        student_demo = student.getDemoOfStudent()
        for dm in student_demo:
            perf_offset = perf_lvl - 1
            # subtract 1 from the total count
            dem_count_dict[dm][L_TOTAL] -= 1
            # subtract 1 from the perf_lvl count
            dem_count_dict[dm][L_PERF_1 + perf_offset] -= 1

        return dem_count_dict

    def _divide_scores_into_perf_lvls(self, scores, assessment):
        '''
        Take a list of scores and an assessment object. Create a dict that places each score into a bucket
        where the key is the integer representing the performance level.
        '''
        sorted_scores = sorted(scores)
        score_dict = {1: [], 2: [], 3: [], 4: [], 5: []}

        # loop through sorted scores and assign to a performance level based on the assessment
        for sc in sorted_scores:
            if sc < assessment.asmt_cut_point_1:
                score_dict[1].append(sc)
            elif sc < assessment.asmt_cut_point_2:
                score_dict[2].append(sc)
            elif sc < assessment.asmt_cut_point_3:
                score_dict[3].append(sc)

            # if there is a 4th cutpoint add to pl4 and pl5
            if assessment.asmt_cut_point_4:
                if sc < assessment.asmt_cut_point_4:
                    score_dict[4].append(sc)
                else:
                    score_dict[5].append(sc)
            # otherwise add the value to pl4
            else:
                score_dict[4].append(sc)

        return score_dict

    def _pick_score_in_pl(self, perf_level, scores_dict):
        '''
        Choose a score from the list of scores based on the performance level given
        '''
        score = None

        # Get random score from PL
        if scores_dict[perf_level]:
            score = random.choice(scores_dict[perf_level])

            # remove that score from the list
            scores_dict[perf_level].remove(score)
        # if no scores are left check the next performance level
        else:
            max_tries = len(scores_dict)
            for i in range(max_tries):
                new_pl = (perf_level + i) % max_tries
                if scores_dict[new_pl]:
                    score = scores_dict[new_pl].pop(0)
                    break

        if not score:
            print(perf_level)
            print(scores_dict)
            exit()

        return score

    def _determine_perf_lvl(self, perf_lvl_counts_list):
        '''
        Determine a performance level based on the what is available
        in the given list
        '''
        available_pls = []
        for i in range(len(perf_lvl_counts_list)):
            if perf_lvl_counts_list[i] > 0:
                available_pls.append(i + 1)  # add 1 so that perf level >= 1 (not >= 0)
        return random.choice(available_pls)

    def _make_other_demographics(self, grade_count_dict, group, asmt_outcomes, students):
        '''
        '''
        group_dict = {}

        # filter all items in this group to new dictionary
        for key in grade_count_dict:
            if grade_count_dict[key][L_GROUPING] == group:
                group_dict[key] = grade_count_dict[key][:]

        # Assign students the demographics
        for i in range(len(asmt_outcomes)):
        #for outcome in asmt_outcomes:
            out_pl = asmt_outcomes[i].asmt_perf_lvl
            demographic_set = False

            # loop through available demographics
            # if the value for that perf_lvl is not 0. Give the outcome that demographic
            for demo_key in group_dict:
                pl_index = out_pl + 1  # offset perf_lvl by 1
                if group_dict[demo_key][pl_index]:
                    setattr(asmt_outcomes[i], demo_key, True)
                    setattr(students[i], demo_key, True)
                    group_dict[demo_key][pl_index] -= 1
                    demographic_set = True
                    break

            # if no demographic was set, assign demographic randomly
            # only if demographic is grouped with other demographics
            if not demographic_set and len(group_dict) > 1:
                rand_dem = random.choice(list(group_dict.keys()))
                setattr(asmt_outcomes[i], rand_dem, True)
                setattr(students[i], rand_dem, True)

        return asmt_outcomes

    def _make_male_or_female(self, male_list, female_list, asmt_outcomes, students):
        '''
        '''
        males = []
        females = []
        male_pl_counts = male_list[L_PERF_1:]
        female_pl_counts = male_list[L_PERF_1:]

        for i in range(len(students)):
            assert students[i].student_guid == asmt_outcomes[i].student_guid
            student_pl = asmt_outcomes[i].asmt_perf_lvl

            if male_pl_counts[student_pl - 1]:
                males.append(students[i])
                male_pl_counts[student_pl - 1] -= 1
            elif female_pl_counts[student_pl - 1]:
                females.append(students[i])
                female_pl_counts[student_pl - 1] -= 1
            else:
                if random.randint(0, 1):
                    males.append(students[i])
                else:
                    females.append(students[i])

        self._assign_gender(males, 'male')
        self._assign_gender(females, 'female')

        return students

    def _assign_gender(self, student_list, gender):
        '''
        '''
        for student in student_list:
            # Check to see if student already has new gender
            if not student.has_updated_gender:
                student.gender = gender
                student.first_name = generate_first_or_middle_name(gender)
                student.middle_name = possibly_generate_middle_name(gender)
                student.has_updated_gender = True


class DemographicStatus(object):
    '''
    class DemographicStatus has demographic status for students
    '''
    def __init__(self, demo_names):
        self.status_dict = self._initialize_status_dict(demo_names)

    def _initialize_status_dict(self, demo_names):
        status = {}
        for demo_name in demo_names:
            status[demo_name] = []
        return status

    def add_many(self, student_list):
        for student in student_list:
            self.add(student)

    def add(self, student_obj):
        '''
        Add one student object into the demographic status dictionary
        The given student will be added into all demographic entries that he belongs to
        '''
        if isinstance(student_obj, Student):
            # get all demo fields
            stu_demo = student_obj.getDemoOfStudent()
            for demo_name in stu_demo:
                if demo_name in self.status_dict.keys():
                    self.status_dict[demo_name].append(student_obj)

    def pop(self, demo_name):
        '''
        Remove and return one student object from the given demographic type
        This student will also be removed from all demographic types he belongs to
        '''
        removed_stu = None
        if demo_name in self.status_dict.keys():
            student_list = self.status_dict[demo_name]
            if len(student_list) > 0:
                # choose the first one
                removed_stu = student_list[0]
                # remove this student from all related demographic lists
                self._update_status_dict(removed_stu)
        else:
            print("No demographic name %s" % demo_name)
        return removed_stu

    def _update_status_dict(self, student_obj):
        stu_demo = student_obj.getDemoOfStudent()
        for demo_name in stu_demo:
            if demo_name in self.status_dict.keys():
                try:
                    self.status_dict[demo_name].remove(student_obj)
                except ValueError:
                    print("The student does not exist in demographic list %s " % demo_name)


def percentages_to_values(grade_demo_dict, total_records):
    ret_dict = {}

    for k in grade_demo_dict:
        perc_list = grade_demo_dict[k]

        # Grouping
        val_list = [perc_list[L_GROUPING]]  # place first value in list

        # Total
        total_value = int((perc_list[L_TOTAL] / 100) * total_records)
        if total_value == 0:
            total_value += 1
        val_list.append(total_value)

        # Performance Levels
        for i in range(L_PERF_1, L_PERF_4 + 1):
            pl_total = int((perc_list[i] / 100) * total_value)
            val_list.append(pl_total)

        # check that we have enough values
        diff = total_value - sum(val_list[L_PERF_1:L_PERF_4 + 1])

        # randomly add values for the differences
        for i in range(diff):
            l_index = random.randint(L_PERF_1, L_PERF_4)
            val_list[l_index] += 1

        ret_dict[k] = val_list

    return ret_dict


if __name__ == '__main__':
    import json
    dem = Demographics('/Users/swimberly/projects/edware/fixture_data_generation/DataGeneration/datafiles/demographicStats.csv')
    #print(json.dumps(dem.dem_data, indent=4))
    #print(json.dumps(dem.get_grade_demographics('typical1', 'math', '5'), indent=2))
    print(dem.get_demo_names('typical1'))