# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseScafSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    admin_area_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string=u'Jefe de Área',
        help='Persona que aparecera por defecto para firma en reportes',
        related="company_id.admin_area_partner_id",
        readonly=False)
    image_logo_reports = fields.Binary(
        related='company_id.image_logo_reports',
        readonly=False
    )
