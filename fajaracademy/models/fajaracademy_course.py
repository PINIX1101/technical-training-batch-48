from odoo import _, api, fields, models


class FajaracademyCourse(models.Model):
    _name = 'fajaracademy.course'
    _description = 'Fajaracademy Course'
    _sql_constraints = [
        ("name_description_check", "check(name != description)", "Name cannot be same as Description"),
        ("name_unique", "unique(name)", "Name must be Unique"),
    ]

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    responsible_user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('fajaracademy.session', 'course_id', string='Session')

    def copy(self, default=None):
        default_data = dict(default or {})

        count = self.search_count([('name','=like','Copy of {}%'.format(self.name))])

        if not count:
            name = 'Copy of {}'.format(self.name)
        else:
            name = 'Copy of {} ({})'.format(self.name, count)

        default_data['name'] = name
        return super(FajaracademyCourse, self).copy(default_data)
        