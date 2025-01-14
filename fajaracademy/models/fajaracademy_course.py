from odoo import _, api, fields, models


class FajaracademyCourse(models.Model):
    _name = 'fajaracademy.course'
    _description = 'Fajaracademy Course'

    name = fields.Char('Title',required=True)
    description = fields.Text('Description')