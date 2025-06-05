from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaterialRegistry(models.Model):
    _name = 'material.registry'
    _description = 'Material Registry'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], required=True)
    buy_price = fields.Float(required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True, domain=[('supplier_rank', '>', 0)])

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Buy Price must be greater than or equal to 100.')
