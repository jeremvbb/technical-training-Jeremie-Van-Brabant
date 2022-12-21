from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    training_date = fields.Date(string="Training Date")
    employee = fields.Char(related="Employee.display_name", string="Employee", readonly=True, store=True)