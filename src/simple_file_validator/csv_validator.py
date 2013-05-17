from __future__ import absolute_import
"""
Stores the basic validations that can be performed on CSV source files.

Some of the basic validations include (but not limited to)
a) Checking the file is valid
b) Checking the file has data and the application has permissions to access it
"""

import os
import csv
import re

from simple_file_validator import error_codes
from udl2_util.file_util import abs_path_join


class CsvValidator():
    """
    Invoke a suite of validations for csv files.
    """


    def  __init__(self):
        """Constructor
        :param arg_udl_db: database connections
        :type arg_udl_db: udl.lib.UdlDb
        """

        self.csv_validations = [IsSourceFolderAccessible(),
                                IsSourceFileAccessible(),
                                IsFileBlank(),
                                DoesSourceFileContainHeaders(),
                                DoesSourceFileContainDuplicateHeaders(),
                                IsSourceFileCommaDelimited(),
                                DoesSourceFileHaveData(),
                                IsCsvWellFormed()]


    def execute(self, dir_path, file_name, batch_sid):
        """Run all validation tests and return error code on first failure, or
        errorcodes.STATUS_OK if all tests pass

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """

        error_list = []
        for validation in self.csv_validations:
            result = validation.execute(dir_path, file_name, batch_sid)
            if result[0] != error_codes.STATUS_OK:
                error_list.append(result)
            else:
                pass
        return error_list


class IsSourceFolderAccessible(object):
    """Job to check for accessible source folder"""
    def execute(self, dir_path, file_name, batch_sid):
        """Check if the path exists, is a directory, and we can read from it

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """

        if os.path.exists(dir_path) and os.path.isdir(dir_path) and os.access(dir_path, os.R_OK):
            return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)
        else:
            return (error_codes.SRC_FOLDER_NOT_ACCESSIBLE_SFV, dir_path, file_name, batch_sid)


class IsSourceFileAccessible(object):
    """Job to check for accessible source file"""
    def execute(self, dir_path, file_name, batch_sid):
        """Check if file exists, is readable and is not a directory

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        full_path = abs_path_join(dir_path, file_name)

        if os.path.exists(full_path) and os.access(full_path, os.R_OK) and os.path.isfile(full_path):

            return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)
        else:
            return (error_codes.SRC_FILE_NOT_ACCESSIBLE_SFV, dir_path, file_name, batch_sid)


class IsFileBlank(object):
    """Job to check for accessible blank file"""
    def execute(self, dir_path, file_name, batch_sid):
        """Check if the file is blank

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        full_path = abs_path_join(dir_path, file_name)

        if os.stat(full_path).st_size > 0:
            return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)
        else:
            return (error_codes.SRC_FILE_HAS_NO_DATA, dir_path, file_name, batch_sid)


class IsSourceFileCommaDelimited(object):
    """Job to check for comma delimited source file"""

    def execute(self, dir_path, file_name, batch_sid):
        """Execute that the file is indeed comma delimited

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """

        # get full path and open file
        full_path = abs_path_join(dir_path, file_name)
        file_to_validate = open(full_path, 'rU')

        attempt_hack = False
        sample_data = None
        # use csv.sniffer to detect the dialect, then close the file
        try:

            # h4x for http://bugs.python.org/issue10515
            # csv sniffer doesn't like lines that end in any type of quote
            # so lets detect quoted string and eol and replace them with 'FILLER'
            sample_data = file_to_validate.read(1024)
            match_results = re.findall(r'(["].*["])\s*$', sample_data, re.MULTILINE)
            for result in match_results:
                sample_data = sample_data.replace(result, 'FILLER')
            dialect = csv.Sniffer().sniff(sample_data, ',')
        except csv.Error as e:
            # if csv.sniffer thorws an exception it means we got a strange encoding.
            # In order not to interfere with encodings that DO work. Lets only apply
            # the hack when an exception is thrown
            attempt_hack = True

        if attempt_hack:
            try:
                # h4x to fix an exception that is thrown by sniffer
                # for the encoding type Western Europe (DOS/OS2-850 International) and probably others as well :)
                sample_data = sample_data.replace('\n', '\r')
                dialect = csv.Sniffer().sniff(sample_data, ',')
            except csv.Error as e:
                # if the hack fails then we'll throw the exception
                return (error_codes.SRC_FILE_WRONG_DELIMITER, dir_path, file_name, batch_sid)

        file_to_validate.close()

        # execute delimiting character
        if not dialect.delimiter is ',':
            print('Wrong delim')
            print(dialect)
            print(dialect.delimiter)
            return (error_codes.SRC_FILE_WRONG_DELIMITER, dir_path, file_name, batch_sid)

        return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)


class DoesSourceFileContainDuplicateHeaders(object):
    """Job to check for source file with duplicate headers"""
    def execute(self, dir_path, file_name, batch_sid):
        """
        Check to make sure the file does not contain duplicate headers

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        full_path = abs_path_join(dir_path, file_name)

        processed_headers = []
        headers = None

        with open(full_path, 'rU') as file_to_validate:
            # headers = file_to_validate.readline()
            reader = csv.reader(file_to_validate)

            while headers is None or len(headers) == 0:
                headers = reader.next()

        for header in headers:
            if header.lower() in processed_headers:
                return (error_codes.SRC_FILE_HAS_DUPLICATE_HEADERS, dir_path, file_name, batch_sid)
            elif len(header) > 0:
                processed_headers.append(header.lower())

        return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)


class DoesSourceFileContainHeaders(object):
    """Job to check for source file with headers"""
    def execute(self, dir_path, file_name, batch_sid):
        """Check to make sure the file contains non-empty headers

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        # get full path and read 1st 4 lines from file.
        full_path = abs_path_join(dir_path, file_name)
        first_four_lines = []
        with open(full_path, 'rU') as file_to_validate:
            for line in file_to_validate:
                line = line.strip()
                if line is not None and len(line) > 0:
                    first_four_lines.append(line)
                    if len(first_four_lines) >= 4:
                        break

        if len(first_four_lines) == 0:
            # No rows, so no header.
            return (error_codes.SRC_FILE_HAS_NO_HEADERS, dir_path, file_name, batch_sid)

        header = first_four_lines[0]
        if all([not bool(column.strip()) for column in header.split(",")]):
            # Header contains no names. Just commas and spaces.
            return (error_codes.SRC_FILE_HAS_NO_HEADERS, dir_path, file_name, batch_sid)

        # Pass first 4 lines to CSV header sniffer
        first_four_lines_str = os.linesep.join(first_four_lines)

        has_headers = csv.Sniffer().has_header(first_four_lines_str)

        if not has_headers:
            return (error_codes.SRC_FILE_HAS_NO_HEADERS, dir_path, file_name, batch_sid)
        else:
            return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)


class IsCsvWellFormed(object):
    """Job to check for well formed csv file"""

    def __init__(self):
        # Initially, lines_to_validate was defined within a configuration file, here we hard code it for now
        # TODO: define lines_to_validate in a configuration file
        self._lines_to_validate = 10 #int(CONFIG.get_config("validation_lines"))

    def set_lines_to_validate(self, lines_to_validate):
        """mutator for lines_to_validate"""
        self._lines_to_validate = lines_to_validate

    def execute(self, dir_path, file_name, batch_sid):
        """Execute to make sure that the number of headers is the same as the
        number of data-points on the first _lines_to_validate lines.

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        # get full path, open file and create reader
        full_path = abs_path_join(dir_path, file_name)
        with open(full_path, 'rU') as file_to_validate:
            file_reader = csv.reader(file_to_validate)

            # get the headers
            headers = file_reader.next()
            num_headers = len(headers)

            # check the number of data points
            while (file_reader.line_num - 1) < self._lines_to_validate:
                try:
                    line = file_reader.next()
                # execute to make sure we haven't hit the end of the file
                except StopIteration:
                    return (error_codes.SRC_FILE_HAS_NO_DATA, dir_path, file_name, batch_sid)

                # validate the number of data entries
                if len(line) != num_headers or self._empty_header_has_data(headers, line):
                    return (error_codes.SRC_FILE_HEADERS_MISMATCH_DATA,
                            dir_path, file_name, batch_sid)

        # we passed all tests
        return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)

    def _empty_header_has_data(self, headers, line):
        """
        Returns True if any header is empty but contains data in the
        same position.
        e.g.: header = '', line value = 'Bob'
        It can indicate some sort of user error where the column header
        should exist.
        """
        for i in range(len(headers)):
            if not headers[i] and line[i]:
                return True
        return False


class DoesSourceFileHaveData(object):
    """Job to check for source file with data"""

    def execute(self, dir_path, file_name, batch_sid):
        """Check if file has at least one data row, and make sure the data row
        and headers contain the same number of fields

        :param dir_path: path of the file
        :type dir_path: string
        :param file_name: name of the file
        :type file_name: string
        :param batch_sid: batch id of the file
        :type batch_sid: integer
        :return: tuple of the form: (status_code, dir_path, file_name, batch_sid)
        """
        full_path = abs_path_join(dir_path, file_name)

        try:
            # open file, reader, and get first two rows
            # if we can retrieve the 2nd row, then it exists,
            # and we can return
            file_to_validate = open(full_path, 'rU')
            file_reader = csv.reader(file_to_validate)
            file_reader.next()
            file_reader.next()
        except StopIteration:
            return (error_codes.SRC_FILE_HAS_NO_DATA, dir_path, file_name, batch_sid)

        return (error_codes.STATUS_OK, dir_path, file_name, batch_sid)
