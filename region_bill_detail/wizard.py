#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class RegionWiseDetail(models.Model):
    _name = "region.wise.detail"

    customer = fields.Many2one('res.partner',string="Customer Name")
    region = fields.Many2one('regions')
    bill_date = fields.Date(string="Bill Date")
    types = fields.Selection([('war','Warehouse'),('sal','Salepoint')],string="Types")




class regionWiseDetail(models.Model):
    _inherit = "summary.ffc"    

    @api.multi
    def create_report(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Region Wise Report',
        'res_model': 'region.wise.detail',
        'view_type': 'form',
        'view_mode': 'form',
        'target' : 'new',
        }
    
    
