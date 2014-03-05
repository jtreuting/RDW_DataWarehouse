"""
Model the SBAC-specific items of a district.

@author: nestep
@date: February 22, 2014
"""

from mongoengine import StringField

from general.model.district import District


class SBACDistrict(District):
    """
    The SBAC-specific district class.
    """
    guid_sr = StringField(required=True)