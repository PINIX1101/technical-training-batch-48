from odoo import _, api, fields, models


class FajaracademySession(models.Model):
    _name = 'fajaracademy.session'
    _description = 'Fajaracademy Session'

    name = fields.Char('Name')
    start_date = fields.Date('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number of Seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain="['|',('is_instructor','=',True),('partner_category_id','!=',False)]")
    course_id = fields.Many2one('fajaracademy.course', string='Course', required=True)
    attendees_ids = fields.Many2many('res.partner', string='Attendees')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('done', 'Done'),
    ], string='State', default='draft')

    def action_confirm(self):
        self.state = 'running'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'