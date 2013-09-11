from __future__ import absolute_import
from udl2.celery import celery
from celery.utils.log import get_task_logger
from udl2.message_keys import EMAIL


logger = get_task_logger(__name__)


@celery.task(name='udl2.W_report_error_or_success.task')
def task(msg):
    '''
    Celery task to report error or success. the message expects to contain
    'email_address'
    '''
    logger.info(task.name)
    logger.info('Report Error or Success Dummy')
    assert msg[EMAIL]

    #TODO: report

    return msg
