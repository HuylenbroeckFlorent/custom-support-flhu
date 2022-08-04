# -*- coding: utf-8 -*-

from odoo import models, fields

import logging

_logger = logging.getLogger(__name__)

class MessageLeadTracker(models.Model):
    _name = "mail.message"
    _inherit = ["mail.message"]

    def track(self, text, vals, record):
        _logger.info("\n\nFLHU message_lead_tracker triggered : %s \n\nValues %s\n\nCreated %s : %s\n\n",
                        text, vals, self, record,
                        stack_info=True)

    def create(self, value_list):
        created = super(MessageLeadTracker, self).create(value_list)

        if value_list[0]['subtype_id'] == 2 and value_list[0]['model']:
            if value_list[0]['model'] == 'crm.lead':
                self.track('New mail.message on crm.lead (id='+str(value_list[0]['res_id'])+")", value_list, created)

        return created
