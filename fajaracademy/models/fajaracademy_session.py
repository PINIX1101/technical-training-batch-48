from odoo import _, api, fields, models


class FajaracademySession(models.Model):
    _name = 'fajaracademy.session'
    _description = 'Fajaracademy Session'

    name = fields.Char('Name')
    start_date = fields.Date('Start Date',default=fields.Date.today())
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
    active = fields.Boolean('Active', default=True)
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')
    
    @api.depends('number_of_seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.number_of_seats:
                rec.taken_seats = len(rec.attendees_ids)/rec.number_of_seats*100
            else:
                rec.taken_seats = 0

    def action_confirm(self):
        self.state = 'running'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'