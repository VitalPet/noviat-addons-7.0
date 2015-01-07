# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Noviat nv/sa (www.noviat.com). All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account Invoice Line Defaults',
    'version': '0.3',
    'license': 'AGPL-3',
    'author': 'Noviat',
    'category' : 'Generic Modules/Accounting',
    'description': """   
This module facilitates the encoding of Invoices lines: 

- The 'Account' field is initialised from the default invoice account fields on the partner records.
- The 'Description' field is moved to the main page of the Supplier Invoice form and the Invoice Line descriptions are initialised from the Invoice Description field.

    """,
    'depends': ['account'],
    'data': [
        'partner_view.xml',                    
        'account_invoice_view.xml',
    ],
}
