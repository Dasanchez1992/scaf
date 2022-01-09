from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tracking = fields.Selection(default='serial')


class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection([
        ('dymo', 'SCAF'),
    ], ondelete={'dymo': 'set default'}, default='dymo')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_ref_by_barcode_and_product(self, barcode):
        self.ensure_one()
        return self.env['stock.production.lot'].search([('product_id', '=', self.id), ('name', '=', barcode)])


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_transfer_reason_id = fields.Many2one(
        comodel_name='picking.transfer.reason',
        string='Motivo transferencia',
        required=False)
    picking_type_transfer = fields.Selection(
        string='Tipo de traslado',
        selection=[('Temporal', 'Temporal'),
                   ('Definitivo', 'Definitivo'), ],
        default='Definitivo')
        

class PickingTransferReason(models.Model):
    _name = 'picking.transfer.reason'

    name = fields.Char(
        string='Descripcion',
        required=False)
