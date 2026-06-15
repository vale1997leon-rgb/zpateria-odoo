from odoo import models, fields

class ZapatoPersonalizacion(models.Model):
    _name = 'zapato.personalizacion'
    _description = 'Personalización de Zapatos'

    name = fields.Char(string='Nombre de la Personalización', required=True)
    description = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio Adicional', required=True)
    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato Base', required=True)
    color = fields.Char(string='Color Personalizado')
    material = fields.Char(string='Material Personalizado')
    talla = fields.Char(string='Tamaño / Horma Especial')
    imagen = fields.Binary(string="Diseño de Referencia")
    calificacion = fields.Selection([
        ('0', 'Sin Calificar'),
        ('1', 'Muy Bajo'),
        ('2', 'Bajo'),
        ('3', 'Medio'),
        ('4', 'Alto'),
        ('5', 'Excelente')
    ], string="Calidad / Prioridad", default='0')