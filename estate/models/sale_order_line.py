from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    training_date = fields.Date(string="Training Date")
    employee = fields.Char(related="employee_id.display_name", string="Employee", readonly=True, store=True)