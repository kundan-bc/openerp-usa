# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 NovaPoint Group LLC (<http://www.novapointgroup.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import orm, osv, fields

class summary_report(orm.TransientModel):
    '''
    Wizard object to print summary report
    '''
    _name = "ship.summary_report"
    _description = "Summary Report"
    _columns = {
        'name': fields.char('Name', size=32),
        }
    
    def print_summary_report(self, cr, uid, ids, context=None):
        if not ids: return []
        return {
            'type': 'ir.actions.report.xml',
            'report_name':'summary_report_print',
            'datas': {
                'model': 'shipping.move',
                'id': ids and ids[0] or False,
                'ids': ids,
                'report_type': 'pdf'
                },
            'nodestroy': False
            }
summary_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: