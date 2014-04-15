'''
Created on May 9, 2013

@author: dip
'''
from smarter.reports.helpers.constants import Constants
from smarter.security.roles.base import BaseRole, verify_context
from smarter.security.context_role_map import ContextRoleMap
from smarter.security.constants import RolesConstants
from sqlalchemy.sql.expression import or_, and_
from edschema.metadata.util import get_selectable_by_table_name


@ContextRoleMap.register([RolesConstants.SRS_EXTRACTS])
class SRSExtracts(BaseRole):

    def __init__(self, connector, name):
        super().__init__(connector, name)

    @verify_context
    def get_context(self, tenant, user):
        '''
        Returns a sqlalchemy binary expression representing school_guid that user has context to
        If Context is an empty list, return None, which will return Forbidden Error
        '''
        student_reg = self.connector.get_table(Constants.STUDENT_REG)
        context = user.get_context().get_states(tenant, self.name)
        # context of none means that user has no access
        if context is None:
            return None
        else:
            return [student_reg.c.state_code.in_(context)] if context else []

    @verify_context
    def add_context(self, tenant, user, query):
        '''
        Updates a query adding context
        If Context is an empty list, return None, which will return Forbidden Error
        '''
        tables = {obj for (obj, name) in get_selectable_by_table_name(query).items() if name == Constants.STUDENT_REG}
        context = user.get_context().get_states(tenant, self.name)
        # context of none means that user has no access
        return None if context is None else query.where(and_(*[table.columns.state_code.in_(context) for table in tables]))

    def check_context(self, tenant, user, student_guids):
        '''
        Returns true if it has context to the list of student guids
        '''
        query = super().get_students(tenant, student_guids)
        query = query.where(or_(*self.get_context(tenant, user)))
        results = self.connector.get_result(query)
        return len(student_guids) == len(results)
