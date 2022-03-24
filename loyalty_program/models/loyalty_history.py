from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Description'

    name = fields.Char('ma customer')
    partner_id = fields.Many2one(comodel_name='', string='partner')
    loyalty_points = fields.Float('points')
    money_spent = fields.Float('total amount in 1 order')
    loyalty_point = fields.Float('Customer accumulated points')
    date_order = fields.Datetime('order receipt time')
