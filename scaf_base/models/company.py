from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    admin_area_partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=False)
    image_logo_reports = fields.Binary(
        string='Imagen a mostrar en los encabezados de los reportes',
        attachment=True
    )
