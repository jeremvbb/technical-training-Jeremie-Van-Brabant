from odoo import fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    training_date = fields.Date(string="Training Date")
    employee = fields.Many2one("hr.employee", string="employee")


    def inherited_action(self):
        self.env["calendar.event.model"].create(
            {
                "name": "Test",
                "line_ids": [
                    Command.create({
                        "field_1": "value_1",
                      "field_2": "value_2",
                    })
                ],
            }
        )
        return super().inherited_action()