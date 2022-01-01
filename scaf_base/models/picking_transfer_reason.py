from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_transfer_reason_id = fields.Many2one(
        comodel_name='picking.transfer.reason',
        string='Motivo transferencia',
        required=False)


class PickingTransferReason(models.Model):
    _name = 'picking.transfer.reason'

    name = fields.Char(
        string='Descripcion',
        required=False)
