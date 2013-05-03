from __future__ import absolute_import
import udl2.celery
import udl2.W_file_loader
from celery.result import AsyncResult
from celery.utils.log import get_task_logger
import filesplitter.file_splitter as file_splitter
import time
import random


logger = get_task_logger(__name__)


@udl2.celery.celery.task(name="udl2.W_file_splitter.task")
def task(msg):
    # place holder for file_splitter
    # split_files = file_splitter_impl()
    # the input parameter for method split_file TBD
    print('message is ', msg)
    split_files = file_splitter.split_file(msg['input_file'])
    number_of_files = len(split_files)
    time.sleep(random.random() * 10)
    logger.info(task.name)
    for i in range(0, number_of_files):
        udl2.W_file_loader.task.apply_async([('part %i of %i file %s passed after ' + task.name) % (i + 1, number_of_files, split_files[i])],
                                               queue='Q_files_to_be_loaded',
                                               routing_key='udl2')
    return msg


@udl2.celery.celery.task
def error_handler(uuid):
    result = AsyncResult(uuid)
    exc = result.get(propagate=False)
    print('Task %r raised exception: %r\n%r' % (
          exc, result.traceback))


# this function will be replaced by US15440
def file_splitter_impl():
    print("Doing file splitting...")
    time.sleep(3)
    print("Four sub files are generated...")
    return ['file1', 'file2', 'file3', 'file4']
