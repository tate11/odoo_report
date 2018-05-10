# -*- coding: utf-8 -*-
# Copyright (C) 2016-2017  Technaureus Info Solutions(<http://technaureus.com/>).

from openerp import api, fields, models, _
from openerp.exceptions import UserError
from openerp.tools.float_utils import float_compare

TYPE2JOURNAL = {
    'out_invoice': 'sale',
    'in_invoice': 'purchase',
    'out_refund': 'sale',
    'in_refund': 'purchase',
}

# mapping invoice type to refund type
TYPE2REFUND = {
    'out_invoice': 'out_refund',        # Customer Invoice
    'in_invoice': 'in_refund',          # Vendor Bill
    'out_refund': 'out_invoice',        # Customer Refund
    'in_refund': 'in_invoice',          # Vendor Refund
}

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def get_container(self):
        invoice_line_s = {}
        i = 0

        for line in self.invoice_line_ids:
            print line.product_id.id
            product_id = line.product_id.id
            container = ''
            booking = ''
            po_no = ''
            vessel = ''
            voy = ''
            shipping_ids = ''

            if line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract':
                product_name = 'TRANSPORTATION CHARGE'
            else:
                product_name = line.product_id.name

            if line.sale_id.type == 'general' or line.sale_id.type == 'logistic':
                container = line.invoice_id.account_note

            if not container and line.sale_id.container_id:
                container = line.sale_id.container_id.name

            if line.sale_id.booking_reference:
                booking = line.sale_id.booking_reference

            if line.invoice_id.name:
                po_no = line.invoice_id.name

            if line.sale_id.vessel_id:
                vessel = line.sale_id.vessel_id.name.v_name

            if line.sale_id.voy_id:
                voy = line.sale_id.voy_id.v_name

            if line.sale_id.from_shipping_id:
                from_shipping = line.sale_id.from_shipping_id.name
                from_shipping_id = line.sale_id.from_shipping_id.id
            else:
                from_shipping = False
                from_shipping_id = False

            if line.sale_id.to_shipping_id:
                to_shipping = line.sale_id.to_shipping_id.name
                to_shipping_id = line.sale_id.to_shipping_id.id
            else:
                to_shipping = False
                to_shipping_id = False

            if line.sale_id.return_shipping_id:
                return_shipping = line.sale_id.return_shipping_id.name
                return_shipping_id = line.sale_id.return_shipping_id.id

            else:
                return_shipping = False
                return_shipping_id = False

            if line.sale_id.shipping_ids:
                for shipping in line.sale_id.shipping_ids:
                    shipping_ids = shipping_ids + shipping.name
            else:
                shipping_ids = False


            if line.sale_id.container_size:
                size = line.sale_id.container_size
            else:
                size = False

            found = False
            if i > 0:
                print "more than one"
                print i
                for x in xrange(0, i):
                    print i
                    print 'i'
                    print '1'
                    print product_id
                    print invoice_line_s[0]['product_id']

                    if product_id == invoice_line_s[x]['product_id']:
                        print '2'

                        # print "found same product"
                        if line.price_unit == invoice_line_s[x]['price_unit']:
                            print '3'
                            # print "found same product and same price"
                            if not (line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract'):
                                print '4'
                                if container != '' and (
                                                    line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract'):

                                    print '5'
                                    invoice_line_s[x]['container_no'] += ','
                                    invoice_line_s[x]['container_no'] += container

                                if booking != '' and (
                                                    line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract'):
                                    print '6'
                                    if booking != invoice_line_s[x]['booking']:
                                        print '7'

                                        invoice_line_s[x]['booking'] += ','
                                        invoice_line_s[x]['booking'] += booking

                                found = True
                                invoice_line_s[x]['quantity'] += line.quantity
                                invoice_line_s[x]['price_subtotal'] += line.price_subtotal
                                invoice_line_s[x]['uom_id'] += line.uom_id.name
                                break

                            # This is transporation only, need to check from to return
                            else:
                                # print "Test from shipping id"
                                # print from_shipping_id
                                # print to_shipping_id
                                # print return_shipping_id
                                # print invoice_line_s[x]['from_shipping_id']
                                # print invoice_line_s[x]['to_shipping_id']
                                # print invoice_line_s[x]['return_shipping_id']
                                print from_shipping_id
                                print invoice_line_s[x]['from_shipping_id']
                                print to_shipping_id
                                print invoice_line_s[x]['to_shipping_id']
                                print return_shipping_id
                                print invoice_line_s[x]['return_shipping_id']
                                print size
                                print invoice_line_s[x]['size']

                                if from_shipping_id == invoice_line_s[x]['from_shipping_id'] and to_shipping_id == invoice_line_s[x]['to_shipping_id'] and return_shipping_id == invoice_line_s[x]['return_shipping_id'] and size == invoice_line_s[x]['size']:
                                    print '8'
                                    if container != '' and (
                                                        line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract'):
                                        invoice_line_s[x]['container_no'] += ','
                                        invoice_line_s[x]['container_no'] += container

                                    if booking != '' and (
                                                        line.product_id.charge_type == 'tran_agent' or line.product_id.charge_type == 'tran_contract' or line.product_id.charge_type == 'tran_none_contract'):
                                        print '9'
                                        if booking != invoice_line_s[x]['booking']:
                                            print '10'
                                            invoice_line_s[x]['booking'] += ','
                                            invoice_line_s[x]['booking'] += booking

                                    found = True
                                    invoice_line_s[x]['quantity'] += line.quantity
                                    invoice_line_s[x]['price_subtotal'] += line.price_subtotal
                                    invoice_line_s[x]['uom_id'] += line.uom_id.name
                                    break


                if not found:
                    print "not found same product"

                    invoice_line_s[i] = {
                        'name': product_name,
                        'product_id': product_id,
                        'container_no': container,
                        'booking' : booking,
                        'po' : po_no,
                        'vessel': vessel,
                        'voy': voy,
                        'from_shipping': from_shipping,
                        'from_shipping_id': from_shipping_id,
                        'to_shipping': to_shipping,
                        'to_shipping_id': to_shipping_id,
                        'shipping_ids': shipping_ids,
                        'return_shipping': return_shipping,
                        'return_shipping_id': return_shipping_id,
                        'size': line.sale_id.container_size,
                        'type': line.sale_id.container_type.name,
                        'quantity': line.quantity,
                        'price_unit': line.price_unit,
                        'price_subtotal': line.price_subtotal,
                        'from_date': line.sale_id.container_id.last_gate_in_date,
                        'to_date': line.sale_id.container_id.last_gate_out_date,
                        'sale_order' : line.sale_id.id,
                        'invoice_line_id': line,
                        'uom_id': line.uom_id.name
                    }
                    i += 1
            # first time
            else:
                print 'first time'
                if not container:
                    container = line.sale_id.container_id.name

                invoice_line_s[i] = {
                    'name': product_name,
                    'product_id': product_id,
                    'container_no': container,
                    'booking' : booking,
                    'po' : po_no,
                    'vessel': vessel,
                    'voy': voy,
                    'from_shipping': from_shipping,
                    'from_shipping_id': from_shipping_id,
                    'to_shipping': to_shipping,
                    'to_shipping_id': to_shipping_id,
                    'shipping_ids': shipping_ids,
                    'return_shipping': return_shipping,
                    'return_shipping_id': return_shipping_id,
                    'size': line.sale_id.container_size,
                    'type': line.sale_id.container_type.name,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'price_subtotal': line.price_subtotal,
                    'from_date': line.sale_id.container_id.last_gate_in_date,
                    'to_date': line.sale_id.container_id.last_gate_out_date,
                    'sale_order' : line.sale_id.id,
                    'invoice_line_id': line,
                    'uom_id': line.uom_id.name
                }
                i += 1

        invoice_line_s = [value for key, value in invoice_line_s.items()]
        # print 'invoice_line_s'
        # print invoice_line_s
        # if invoice_line_s:
        #     for inv_line in invoice_line_s:
        #         print inv_line['price_unit']
        #         print inv_line['price_subtotal']

        return invoice_line_s
