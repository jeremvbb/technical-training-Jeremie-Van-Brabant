from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    training_date = fields.Date(string="Training Date")
    employee = fields.Many2one("hr.employee", string="employee")

@api.model
def create(self, vals):
    res = super(CalendarEvent, self).create(vals)
    # code here to create sale order
    
    return res