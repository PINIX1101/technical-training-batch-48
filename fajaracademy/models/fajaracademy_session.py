from odoo import _, api, fields, models


class FajaracademySession(models.Model):
    _name = 'fajaracademy.session'
    _description = 'Fajaracademy Session'

    name = fields.Char('Name')
    start_date = fields.Date('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number of Seats')