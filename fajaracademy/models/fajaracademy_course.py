from odoo import _, api, fields, models


class FajaracademyCourse(models.Model):
    _name = 'fajaracademy.course'
    _description = 'Fajaracademy Course'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    responsible_user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('fajaracademy.session', 'course_id', string='Session')