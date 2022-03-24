from odoo import fields, models, api


class CustomerManagement(models.Model):
    _inherit = 'res.partner'
    _description = 'customer_management'

    loyalty_point = fields.Float('points_customer')
    loyalty_level = fields.Many2one(comodel_name='partner.levels', string='Partner Liver: ')

