# (c) 2014 The Regents of the University of California. All rights reserved,
# subject to the license below.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0. Unless required by
# applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

'''
Created on Sep 25, 2014

@author: tosako
'''
from smarter_score_batcher.utils.file_lock import FileLock
import os
import time
import json
from smarter_score_batcher.error.constants import ErrorsConstants


def generate_error_file(error_file_path, err_list):
    '''
    generate error file.
    '''
    SPIN = True
    directory = os.path.dirname(error_file_path)
    while SPIN:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        try:
            with FileLock(error_file_path) as f:
                data = f.file_object.read()
                f.file_object.truncate(0)
                f.file_object.seek(0)
                if data:
                    error_info = json.loads(data)
                else:
                    error_info = build_error_info_header()
                error_info[ErrorsConstants.TSB_ERROR].append(err_list)
                data = json.dumps(error_info)
                f.file_object.write(data)
                SPIN = False
        except BlockingIOError:
            time.sleep(0.02)


def build_error_info_header():
    '''
    error file template
    '''
    return {ErrorsConstants.CONTENT: ErrorsConstants.ERROR, ErrorsConstants.TSB_ERROR: []}


def build_err_list(err_code, err_source, err_code_text, err_source_text, err_input):
    '''
    error file body
    '''
    err_list = {}
    err_list[ErrorsConstants.ERR_CODE] = err_code
    err_list[ErrorsConstants.ERR_SOURCE] = err_source
    err_list[ErrorsConstants.ERR_CODE_TEXT] = err_code_text
    err_list[ErrorsConstants.ERR_SOURCE_TEXT] = err_source_text
    err_list[ErrorsConstants.ERR_INPUT] = err_input
    return err_list


def build_err_list_from_object(error_object):
    '''
    error file body
    '''
    err_list = {}
    err_list[ErrorsConstants.ERR_CODE] = error_object[ErrorsConstants.ERR_CODE]
    err_list[ErrorsConstants.ERR_SOURCE] = error_object[ErrorsConstants.ERR_SOURCE]
    err_list[ErrorsConstants.ERR_CODE_TEXT] = error_object[ErrorsConstants.ERR_CODE_TEXT]
    err_list[ErrorsConstants.ERR_SOURCE_TEXT] = error_object[ErrorsConstants.ERR_SOURCE_TEXT]
    err_list[ErrorsConstants.ERR_INPUT] = error_object[ErrorsConstants.ERR_INPUT]
    return err_list
