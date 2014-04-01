__author__ = 'tshewchuk'

"""
This module contain functions to compile report data from trackers into a generator.
"""

from edextract.data_extract_generation.statistics_generator import generate_data_row
from edextract.trackers.category_tracker import DataCounter


def get_tracker_results(report_map, total_tracker, trackers, current_year):
    """
    Use the report map to transform the tracker data into the report data format.

    @param report_map: Hierarchical map of basic report format
    @param total_tracker: Totals tracker, from which to obtain the EdOrg totals, for percentage calculations
    @param trackers: List of trackers containing needed data to fill the report
    @param: current_year: Current academic year of the report

    @return: Report data, as a generator
    """

    # First, get all the edorg totals.
    previous_year = current_year - 1
    for key, val in report_map.items():
        total_entry_data = total_tracker.get_map_entry(val)
        previous_year_total = total_entry_data.get(previous_year, None)
        current_year_total = total_entry_data.get(current_year, None)

        for tracker in trackers:
            state_name = key.state_name
            district_name = key.district_name if key.district_name else 'ALL'
            school_name = key.school_name if key.school_name else 'ALL'
            category, value = tracker.get_category_and_value()
            if total_entry_data:
                entry_data = _get_map_entry(tracker.get_map_entry(val), current_year, previous_year)

                previous_year_count = _get_count(entry_data.get(previous_year, 0), [previous_year_total])
                current_year_count = _get_count(entry_data.get(current_year, 0), [current_year_total])
                matched_id_count = _get_count(entry_data.get(DataCounter.MATCHED_IDS, 0), [previous_year_total, current_year_total])
                row = [state_name, district_name, school_name, category, value] + generate_data_row(current_year_count, previous_year_count,
                                                                                                    current_year_total, previous_year_total,
                                                                                                    matched_id_count)
                yield row


def _get_map_entry(entry_data, current_year, previous_year):
    """
    Adjust the current entry data, based on it's existence status.

    @param entry_data: Current entry data
    @param current_year: Current academic year
    @param previous_year: Previous academic year

    @return: Adjusted current entry data
    """

    if entry_data:
        return entry_data
    else:
        return {current_year: 0, previous_year: 0, DataCounter.MATCHED_IDS: 0}


def _get_count(count, totals):
    """
    Determine the count, based on the totals.

    @param count: Count for some category
    @param totals: Totals to be tested

    @return: Adjusted count for the category (int or None)
    """

    for total in totals:
        if total is None:
            return None
    return count
