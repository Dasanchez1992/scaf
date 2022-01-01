# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockLocation(models.Model):
    _inherit = 'stock.location'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Custodio',
        required=False)

    @api.onchange('partner_id')
    def compute_name(self):
        for rec in self:
            if rec.partner_id:
                rec.name = rec.partner_id.name
