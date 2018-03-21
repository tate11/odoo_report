{
    'name': 'odoo_report',
    'version':'1.0',
    'category':'Extends Report',
    'summary':'',
    'description':"""...""",
    'depends':['account','product','stock','purchase','sale_service','project_timesheet','mrp_repair','thaireefer_extended','report_xlsx','sale','thai_accounting','thai_accounting_taxinvoice'],
    'website':'http://www.thaireefer.co.th',
    'data':['report/report_reg.xml',
            'report/invoice_trf_report100_id.xml',
            'report/quotation_trf_report101_id.xml',
            'report/taxinvoice_trf_report102_id.xml'],
    'auto_install':False,
    'application':True
}