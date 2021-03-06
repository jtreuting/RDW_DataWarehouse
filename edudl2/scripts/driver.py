# (c) 2014 Amplify Education, Inc. All rights reserved, subject to the license
# below.
#
# Education agencies that are members of the Smarter Balanced Assessment
# Consortium as of August 1, 2014 are granted a worldwide, non-exclusive, fully
# paid-up, royalty-free, perpetual license, to access, use, execute, reproduce,
# display, distribute, perform and create derivative works of the software
# included in the Reporting Platform, including the source code to such software.
# This license includes the right to grant sublicenses by such consortium members
# to third party vendors solely for the purpose of performing services on behalf
# of such consortium member educational agencies.

#!/bin/env python
from __future__ import absolute_import
import os
import shutil
import glob
import argparse
from edudl2.database.udl2_connector import initialize_all_db
from edudl2.udl2.udl2_pipeline import get_pipeline_chain
from edudl2.udl2.udl_trigger import udl_trigger
from edudl2.udl2.celery import celery, udl2_conf, udl2_flat_conf


def run_pipeline(archive_file=None, batch_guid_forced=None):
    """
    Begins the UDL Pipeline process for the file found at path archive_file

    :param archive_file: The file to be processed
    :param batch_guid_forced: this value will be used as batch_guid for the current run
    """
    if not archive_file:
        raise Exception
    get_pipeline_chain(archive_file, guid_batch=batch_guid_forced).delay()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='archive_file', help="path to the source archive file.")
    parser.add_argument('--dev', action='store_true', dest='dev_mode',
                        default=False, help="dev mode (Celery will run as eager and file is optional)")
    parser.add_argument('-g', dest='batch_guid_forced', default=None,
                        help="force the udl2 pipeline to use this batch guid")
    parser.add_argument('--loop-once', dest='loop_once', action='store_true',
                        help='Runs the udl_trigger script to watch the arrivals directory, schedule all files and exit')
    parser.add_argument('-t', dest='tenant', default='cat', help="path to the source archive file.")
    args = parser.parse_args()
    if args.dev_mode:
        # TODO: Add to ini for $PATH and eager mode when celery.py is refactored
        celery.conf.update(CELERY_ALWAYS_EAGER=True)
        os.environ['PATH'] += os.pathsep + '/usr/local/bin'
        # explicitly intialize db in dev mode
        initialize_all_db(udl2_conf, udl2_flat_conf)
        if args.archive_file is None:
            src_dir = os.path.join(os.path.dirname(__file__), '..', 'edudl2', 'tests', 'data', 'test_data_latest')
            # Find the first tar.gz.gpg file as LZ file
            file_name = glob.glob(os.path.join(src_dir, "*.tar.gz.gpg"))[0]
            # Copy file to arrivals dir of ca tenant
            dest = os.path.join(udl2_conf['zones']['arrivals'], args.tenant, os.path.basename(file_name) + '.processing')
            shutil.copy(file_name, dest)
            args.archive_file = dest

    if args.loop_once:
        # run the udl trigger to watch the arrivals directory and schedule all files and exit
        # this is to help tests call trigger script and get an handle back
        udl_trigger(udl2_flat_conf, loop_once=True)
    elif args.dev_mode or args.archive_file is not None:
        # run the pipeline for a single file
        run_pipeline(args.archive_file, batch_guid_forced=args.batch_guid_forced)
    else:
        parser.error('Please specify a valid argument')
