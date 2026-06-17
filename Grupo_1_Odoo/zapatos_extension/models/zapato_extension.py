from odoo import models, fields, api

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'
    codigo=fields.Text(string="Codigo zapato")
    marca = fields.Char(string='Marca')
    color = fields.Char(string='Color')
    material = fields.Char(string='Material')
    descripcion = fields.Text(string='Descripción')
    stock_minimo = fields.Integer(string='Stock Mínimo', default=5)

    valor_inventario = fields.Float(
        string='Valor Inventario',
        compute='_compute_valor_inventario',
        store=True
    )

    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for record in self:
            record.valor_inventario = record.precio * record.stock
    
   
            
   
            
