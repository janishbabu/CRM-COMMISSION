from odoo import models, fields


class CrmCommissions(models.Model):
    _name = "crm.commission"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    from_date = fields.Datetime()
    to_date = fields.Datetime()
    commission_type = fields.Selection(string='Commission Type',
                                       selection=[('product wise',
                                                   'Product wise'),
                                                  ('revenue wise',
                                                   'Revenue wise')],
                                       copy=False, default='product wise',
                                       required=True)
    type = fields.Selection(string='Model Type',
                            selection=[('straight', 'Straight'),
                                       ('graduated', 'Graduated')],
                            copy=False, required=True,
                            default='straight')
    product_wise_ids = fields.One2many("product.wise", "product_wise_id")
    revenue_wise_ids = fields.One2many("revenue.wise", "revenue_wise_id")
    product_rate_id = fields.Many2one("sale.order.line")


class ProductWise(models.Model):
    _name = "product.wise"

    product_id = fields.Many2one("product.template", required=True)
    product_category_id = fields.Many2one(related="product_id.categ_id")
    rate_percentage = fields.Float(string="Rate Percentage (%)")
    Commission = fields.Float(string="Maximum Commission Amount")
    product_wise_id = fields.Many2one("crm.commission")
    sequence = fields.Integer(string="Sequence")


class RevenueWise(models.Model):
    _name = "revenue.wise"

    type = fields.Selection(string='Model Type',
                            selection=[('straight', 'Straight'),
                                       ('graduated', 'Graduated')],
                            copy=False)
    sequence = fields.Integer(string="Sequence", default=10)
    from_amount = fields.Float()
    to_amount = fields.Float()
    rate = fields.Float()
    revenue_wise_id = fields.Many2one("crm.commission")
