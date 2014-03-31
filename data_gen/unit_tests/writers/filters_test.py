"""
Unit tests for the project.sbac.writers.filters module.

@author: nestep
@date: March 20, 2014
"""

import sbac_data_generation.writers.filters as sbac_filters


def test_filter_yesno_true():
    assert sbac_filters.filter_yesno(True) == 'Yes'


def test_filter_yesno_false():
    assert sbac_filters.filter_yesno(False) == 'No'


def test_filter_yesno_none():
    assert sbac_filters.filter_yesno(None) == 'No'


def test_filter_yesnoblank_true():
    assert sbac_filters.filter_yesnoblank(True) == 'Yes'


def test_filter_yesnoblank_false_hundred_thousand():
    count_blank = 0
    for _ in range(100000):
        if sbac_filters.filter_yesnoblank(False) == '':
            count_blank += 1

    assert .07 < (count_blank / 100000) < .09


def test_filter_always_true_true():
    assert sbac_filters.filter_always_true(True)


def test_filter_always_true_false():
    assert sbac_filters.filter_always_true(False)


def test_filter_always_true_none():
    assert sbac_filters.filter_always_true(None)