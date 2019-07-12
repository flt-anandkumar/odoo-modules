# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleConfigSettings(models.TransientModel):
    _inherit = 'sale.config.settings'

    group_final_so_charge = fields.Boolean(string="Allow to enter final Sale Order charge",
                                           implied_group='bahmni_sale.group_allow_change_so_charge')
    group_default_quantity = fields.Boolean(string="Allow to enter default quantity as -1",
                                            implied_group='bahmni_sale.group_allow_change_qty')
    convert_dispensed = fields.Boolean(string="Allow to automatically convert "
                                       "quotation to sale order if drug is dispensed from local shop")
    validate_picking = fields.Boolean(string="Validate delivery when order confirmed")
    allow_negative_stock = fields.Boolean(string="Allow negative stock")
#     auto_convert_dispensed = fields.Selection([(0, "Allow to automatically convert "\
#                                        "quotation to sale order if drug is dispensed from local shop"),
#                                           (1, "Manually convert quotation to sale order")],
#                                          string="Convert Dispensed")

    @api.multi
    def set_convert_dispensed(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'convert_dispensed', self.convert_dispensed)

    @api.model
    def get_default_validate_picking(self, fields):
        value = int(self.env.ref('bahmni_sale.validate_delivery_when_order_confirmed').value)
        return {'validate_picking': bool(value)}

    @api.multi
    def set_default_validate_picking(self):
        for record in self:
            value = 1 if record.validate_picking else 0
            self.env.ref('bahmni_sale.validate_delivery_when_order_confirmed').write({'value': str(value)})

    @api.model
    def get_default_allow_negative_stock(self, fields):
        value = int(self.env.ref('bahmni_sale.allow_negative_stock').value)
        return {'validate_picking': bool(value)}

    @api.multi
    def set_default_allow_negative_stock(self):
        for record in self:
            value = 1 if record.allow_negative_stock else 0
            self.env.ref('bahmni_sale.allow_negative_stock').write({'value': str(value)})

