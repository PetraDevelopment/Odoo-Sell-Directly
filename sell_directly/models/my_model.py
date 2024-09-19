from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError


class newSaleOrder(models.Model):
    _inherit='sale.order'


    serial = fields.Char(string='Document Number')

    _sql_constraints = [
        ('unique_serial', 'unique(serial)', 'The Serial Number Already Exist!')
    ]

    @api.constrains('serial')
    def _check_unique_serial(self):
        for order in self:
            if order.serial and self.search_count([('serial', '=', order.serial)]) > 1:
                raise ValidationError('The Serial Number Already Exist!')


    def _prepare_invoice(self):
        invoice_vals = super(newSaleOrder, self)._prepare_invoice()
        invoice_vals['ext_serial'] = self.serial
        return invoice_vals

class newPuechaseOrder(models.Model):
    _inherit='purchase.order'


    purchase_serial = fields.Char(string='Document Number')
    my_custom_button = fields.Char(string="My Custom Button", default="Custom Button")


    _sql_constraints = [
        ('unique_purchase_serial', 'unique(purchase_serial)', 'The Serial Number Already Exist!')
    ]

    @api.constrains('purchase_serial')
    def _check_unique_serial(self):
        for order in self:
            if order.purchase_serial and self.search_count([('purchase_serial', '=', order.purchase_serial)]) > 1:
                raise ValidationError('The Serial Number Already Exist!')

    def action_create_sales_quotation(self):

        sale_order_lines = []
        for line in self.order_line:
            sale_order_lines.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'product_uom_qty': line.product_qty,
                # 'uom_per_unit': line.uom_per_unit,
                # 'total':line.total
                
            }))

        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'order_line': sale_order_lines,
        })

        # sale_order.action_confirm()


        # Optionally, you can open the created sales quotation
        return {
        'name': 'Sales Quotation',
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'sale.order',
        'res_id': sale_order.id,  # Corrected parameter
        'target': 'current',
    }

    def _prepare_invoice(self):
        invoice_vals = super(newPuechaseOrder, self)._prepare_invoice()
        invoice_vals['ext_serial'] = self.purchase_serial
        return invoice_vals
        
   
class extAccountMove(models.Model):
    _inherit='account.move'

    ext_serial = fields.Char(string='Document Number')


