from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    commission = fields.Float()

    @api.onchange('price_unit', 'product_uom_qty')
    def commissions(self):
        crm_commission = self.order_id.team_id.crm_commission
        if crm_commission.from_date <= self.order_id.date_order \
                <= crm_commission.to_date:
            for product_wise in crm_commission.product_wise_ids:
                if crm_commission.commission_type == 'product wise':
                    if product_wise.product_id == self.product_template_id:
                        self.commission = self.price_subtotal \
                                          * product_wise.rate_percentage / 100
                        if self.commission > product_wise.Commission:
                            self.commission = product_wise.Commission
                else:
                    if crm_commission.type == 'straight':
                        for revenue_wise in crm_commission.revenue_wise_ids:
                            if revenue_wise.from_amount <= self.price_subtotal \
                                    <= revenue_wise.to_amount:
                                self.commission = self.price_subtotal \
                                                  * revenue_wise.rate / 100
                    else:
                        cal_commission = 0
                        for revenue_wise in crm_commission.revenue_wise_ids:
                            if self.price_subtotal > revenue_wise.to_amount:
                                cal_commission = revenue_wise.to_amount \
                                                 * revenue_wise.rate / 100
                                self.price_subtotal = \
                                    (self.price_subtotal -
                                     revenue_wise.to_amount)
                            else:
                                cal_commission += self.price_subtotal * \
                                                  revenue_wise.rate / 100
                                self.commission = cal_commission
                                return
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    total_commission = fields.Float(compute="_compute_amounts",
                                    string="Total Commission")

    @api.depends('order_line.commission')
    def _compute_amounts(self):
        for order in self:
            order.total_commission = sum(order.order_line.mapped('commission'))
