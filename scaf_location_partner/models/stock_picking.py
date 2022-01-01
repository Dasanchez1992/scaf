from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_dest_id = fields.Many2one(
        comodel_name='res.partner',
        related='location_dest_id.partner_id',
        string='Custodio destinatario',
        required=False)
