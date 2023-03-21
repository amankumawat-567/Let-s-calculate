import requests

def download_update():
    url = 'http://www.floatrates.com/daily/usd.xml'
    r = requests.get(url, allow_redirects=True)
    open('usd.xml', 'wb').write(r.content)

import os
def modulating():
    os.rename("usd.xml","currency_data.xml")
    os.replace("currency_data.xml","module/currency_data.xml")

from xml.dom import minidom
import mysql.connector
def upgrade_currencydata():
    mydoc = minidom.parse('module/currency_data.xml')
    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="1234",
          database="currencydata"
          )
    mycursor = mydb.cursor()

    pubdate = mydoc.getElementsByTagName('pubDate')

    basename = mydoc.getElementsByTagName('baseName')

    targetname = mydoc.getElementsByTagName('targetName')

    exchangerate = mydoc.getElementsByTagName('exchangeRate')
        
    inverserate = mydoc.getElementsByTagName('inverseRate')

    sql = "UPDATE data SET ExchangeRate = %s , InverseRate = %s , Updatetime = %s WHERE Target = %s "
   
    val = ("1","1",pubdate[0].firstChild.data,"U.S. Dollar")

    mycursor.execute(sql, val)
    mydb.commit()

    for r in range(0,148):
        tar = targetname[r].firstChild.data
        val = (exchangerate[r].firstChild.data,inverserate[r].firstChild.data,pubdate[r].firstChild.data,tar.replace('ʻ','1'))
        mycursor.execute(sql, val)
        mydb.commit()
         



    
