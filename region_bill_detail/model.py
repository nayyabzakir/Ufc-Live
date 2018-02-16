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
###################################################
from openerp import models, fields, api

class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.region_bill_detail.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('region_bill_detail.module_report')
        active_wizard = self.env['region.wise.detail'].search([])
        emp_list = []
        for x in active_wizard:
            emp_list.append(x.id)
        emp_list = emp_list
        emp_list_max = max(emp_list) 

        record_wizard = self.env['region.wise.detail'].search([('id','=',emp_list_max)])

        record_wizard_del = self.env['region.wise.detail'].search([('id','!=',emp_list_max)])
        record_wizard_del.unlink()
        
        records = self.env['summary.ffc'].search([('Customer','=',record_wizard.customer.id),('invoice_date','=',record_wizard.bill_date)])
        for x in records:
            if x.Customer.name == "FFC Mir Pur Mathelo":
                enteries = []
                for z in x.sum_ids2:
                    if record_wizard.region == z.region and record_wizard.types == z.types:
                        if z not in enteries:
                            enteries.append(z)

                            
        for x in records:
            if x.Customer.name == "FFC Goth Machi":
                enteries = []
                for z in x.sum_ids2:
                    if record_wizard.region == z.region and record_wizard.types == z.types:
                        if z not in enteries:
                            enteries.append(z)


        def bill():
            for x in records:
                if x.Customer.name == "FFC Mir Pur Mathelo":
                    for z in x.sum_ids:
                        if record_wizard.region.name == z.region_name:
                            return z.bill_num


            
        def namer():
            prov = ""
            for x in records:
                if x.Customer.name == "FFC Goth Machi":
                    prov = x.Customer.name
                if x.Customer.name == "FFC Mir Pur Mathelo":
                    prov = x.Customer.name
            
            return prov



        codes = []
        for x in enteries:
            if x.code not in codes:
                codes.append(x.code)
        codes.sort(key=int)

       
        sorted_records = []
        for x in codes:
            for y in enteries:
                if y.code == x:
                    sorted_records.append(y)


        number = []
        for x in range(7 - len(sorted_records)):
            number.append(x)
        counting = len(number) + 1


        if counting % 7 == 0:
            divid = counting / 7
        else:
            divid = int(counting / 7) + 1

        emp_count = []
        count = 0
        while count < divid:
            count = count + 1
            emp_count.append(count*7)
        sizer = len(emp_count)


        print sizer
        print "jjjjjjjjjjjjjjjjjjj"

        print counting
        print "kkkkkkkkkkkkkkkkkkkk"

        print emp_count
        print "kkkkkkkkkkkkkkkkkkkk"



        region = record_wizard.region.name
        customer = record_wizard.customer.name
        types = record_wizard.types
        bill_date = record_wizard.bill_date


      

        docargs = {

            'doc_ids': docids,
            'doc_model': 'summary.ffc',
            'docs': records,
            'data': data,
            'enteries': enteries,
            'namer': namer,
            'sorted_records': sorted_records,
            'number': number,
            'region': region,
            'bill': bill,
            'customer': customer,
            'types': types,
            'loop': emp_count,
            'sizer': sizer,

            }

        return report_obj.render('region_bill_detail.module_report', docargs)