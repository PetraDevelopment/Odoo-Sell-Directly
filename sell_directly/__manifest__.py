{
    'name':'Sell Directly',
    'summary':'Special Serial Number and sell directly from purchase ',
    'depends': ['base', 'product','sale','stock','web_tour','purchase','account'],
    'category':'Sales',

    'data':[
       
            'views/sales_orderline.xml',
            'views/purchase_orderline.xml'  ,
            'views/invoice_serial.xml'   

            ],
            'website': 'www.t-petra.com',
    'author':'Petra Software',
    'company': 'Petra Software',
    'maintainer': 'Petra Software',
    'images': ['static/description/banner.png'],
        'price':15,
      'currency':'USD',  
         
        
    }