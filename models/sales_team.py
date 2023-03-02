from odoo import models, fields


class SalesTeam(models.Model):
    _inherit = "crm.team"

    crm_commission = fields.Many2one("crm.commission")
