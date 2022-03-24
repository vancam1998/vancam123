from odoo import fields, models, api


class ManagePromotion(models.Model):
    _name = 'manage.promotion'
    _description = 'Description'

    name = fields.Text('loyalty program Name: ')
    points = fields.Float('% points: ')
    active = fields.Boolean('Active: ')

