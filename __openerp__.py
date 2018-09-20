{
    'name': 'odoo_report',
    'version':'1.0',
    'category':'Extends Report',
    'summary':'',
    'description':"""...""",
    'depends':['account','product','stock','purchase','sale_service','project_timesheet','mrp_repair','thaireefer_extended','report_xlsx','sale','thai_accounting','thai_accounting_taxinvoice','thai_accounting_branch','thai_accounting_receipt'],
    'website':'http://www.thaireefer.co.th',
    'data':['report/report_reg.xml',
            'report/invoice_trf_report120_id.xml',
            'report/quotation_trf_report101_id.xml',
            'report/taxinvoice_trf_report102_id.xml',
            'report/invoice_group_report_103_id.xml',
            'report/wht53_report_104_id.xml',
            'report/wht3_report_105_id.xml',
            'report/equipment_report_106_id.xml',
            'report/documentation_report_107_id.xml',
            'report/purchase_report_108_id.xml',
            'report/invoice_trf_std_report_111_id.xml',
            'report/receipt_voucher_112_id.xml',
            'report/bill_report_113_id.xml',
            'report/receipt_customer_new_114_id.xml',
            'report/receipt_customer_new_type_115_id.xml',
            'report/purchase_report_trf_116_id.xml',
            'report/suppliercreditnote_report_117_id.xml',
            'report/paymentvoucher_report_118_id.xml',
            'report/vendorvoucher_report_119_id.xml',
            'report/invoice_mahachai_report_121_id.xml',
            'report/generalvoucher_report_122_id.xml',
            'report/quotation_std_report123_id.xml',
            'report/invoice_one_report124_id.xml',
            'report/taxinvoice_group_report125_id.xml',
            'report/invoice_STD_report126_id.xml',
            'report/quotations127_report_id.xml',
            'report/invoice_leam_repoet_128_id.xml',
            'report/tax_invoice_USD_report_129_id.xml',
            'report/billing_STD_report_130_id.xml',
            'report/invoice_trf_report133_id.xml',
            'report/receipt_customer_trfempty_134_id.xml',
            'report/invoice_trf_thaiunion135.xml',
            'report/receipt_customer_new_136_id.xml',
            'report/deliveryorder_139_id.xml',
            'report/invoice_wht_140_id.xml',
            'report/billing_wht_141_id.xml',
            ],
    'auto_install':False,
    'application':True
}
