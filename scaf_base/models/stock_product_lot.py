from odoo import fields, models, api


class StockState(models.Model):
    _name = 'stock.state'

    name = fields.Char()

    _sql_constraints = [('name_uniq', 'unique (name)', 'No se pueden repetir estados')]


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'
    
    state_id = fields.Many2one(
        comodel_name='stock.state',
        string='Estado del equipo',
        required=False)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    state_id = fields.Many2one(
        comodel_name='stock.state',
        string='Estado del equipo',
        related='lot_id.state_id',
        readonly=False)
