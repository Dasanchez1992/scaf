from odoo import fields, models, api
from odoo.exceptions import UserError


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    @api.model
    def create(self, values):
        # Agregamos series categorias a prod
        obj = super(StockProductionLot, self).create(values)
        categ_id = obj.product_id.categ_id
        # if not categ_id.ir_sequence_id:
        #     raise UserError('No hay sequencia creada para la categoria: {} del producto {}, sin la secuencia no se '
        #                     'pueden crear automaticamente las secuencias de los numeros de serie de los '
        #                     'productos'.format(
        #                         categ_id.name,
        #                         obj.product_id.name
        #                     ))
        if categ_id:
            obj.ref = "{}-{}".format(
                categ_id.default_code,
                categ_id.ir_sequence_id._next()
            )
        return obj
