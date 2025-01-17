from odoo import _, api, fields, models


class AddSessionAttendeesWizard(models.TransientModel):
    _name = 'add.session.attendees.wizard'
    _description = 'Add Session Attendees Wizard'

    session_ids = fields.Many2many('fajaracademy.session', string='Session')
    attendees_ids = fields.Many2many('res.partner', string='Attendees')

    def confirm(self):
        for session in self.session_ids:
            session.attendees_ids |= self.attendees_ids