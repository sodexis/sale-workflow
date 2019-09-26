# Copyright 2011 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# Copyright 2013 Camptocamp SA (author: Guewen Baconnier)
# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    workflow_process_id = fields.Many2one(
        comodel_name='sale.workflow.process',
        string='Sale Workflow Process'
    )

    @api.multi
    def action_cancel(self):
        for inv in self:
            if inv.workflow_process_id:
                inv.workflow_process_id = None
        return super(AccountInvoice, self).action_cancel()
