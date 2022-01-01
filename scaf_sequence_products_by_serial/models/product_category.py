from odoo import fields, models, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    default_code = fields.Char(
        string='Referencia interna',
        required=False)

    ir_sequence_id = fields.Many2one(
        comodel_name='ir.sequence',
        string='Secuencia de series generadas',
        required=False)
