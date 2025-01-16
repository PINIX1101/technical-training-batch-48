from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


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
    stop_date = fields.Date(compute='_compute_stop_date', string='Stop Date', store=True)
    number_of_attendees = fields.Float(compute='_compute_number_of_attendees', string='Number of Attendees', store=True)
    
    @api.depends('attendees_ids')
    def _compute_number_of_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.attendees_ids)
    
    @api.depends('start_date','duration')
    def _compute_stop_date(self):
        for rec in self:
            rec.stop_date = rec.start_date + relativedelta(days=+rec.duration)

    @api.constrains('attendees_ids','instructor_id')
    def _constrains_participants(self):
        for rec in self:
            if rec.instructor_id in rec.attendees_ids:
                raise ValidationError('Instructor cannot be Attendees')

    @api.onchange('number_of_seats','attendees_ids')
    def _onchange_seats_warning(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': 'Invalid Number for Seats',
                    'message': 'Number of Seats Cannot be Negative'
                }
            }
        
        if len(self.attendees_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': 'Overload Capacity in Session',
                    'message': 'Number of Attendees more than Number of Seats'
                }
            }
    
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