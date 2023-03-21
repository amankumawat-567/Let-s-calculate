from xml.dom import minidom
import pandas as pd
import mysql.connector

def convert_xml_currency():
    mydoc = minidom.parse('module/currency_data.xml')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE currencydata")
    mycursor.execute("USE currencydata")
    mycursor.execute("CREATE TABLE data(Base varchar(25),Target varchar(40),ExchangeRate varchar(25),InverseRate varchar(25), Updatetime varchar(35))")
    mycursor = mydb.cursor()

    pubdate = mydoc.getElementsByTagName('pubDate')

    basename = mydoc.getElementsByTagName('baseName')

    targetname = mydoc.getElementsByTagName('targetName')

    exchangerate = mydoc.getElementsByTagName('exchangeRate')
        
    inverserate = mydoc.getElementsByTagName('inverseRate')

    sql = "INSERT INTO data(Base,Target,ExchangeRate,InverseRate,Updatetime) VALUES (%s, %s, %s, %s, %s)"

    mycursor.execute(sql,("U.S. Dollar","U.S. Dollar","1","1",pubdate[0].firstChild.data))
    
    for r in range(0,148):
        tar = targetname[r].firstChild.data
        val = (basename[r].firstChild.data,tar.replace('ʻ','1'),exchangerate[r].firstChild.data,inverserate[r].firstChild.data,pubdate[r].firstChild.data)
        mycursor.execute(sql, val)
        mydb.commit()

def convert_csv_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE data")
    mycursor.execute("USE data")
    data_element_list = ["length","area","volume","weight","speed","energy","time","data","power","pressure"]
    for i in data_element_list:
        mycursor.execute("CREATE TABLE "+i+"(Unit varchar(50),Value varchar(50))")
    mydb.commit()
    
    sql_l = "INSERT INTO length(Unit,Value) VALUES (%s, %s)"
    sql_a = "INSERT INTO area(Unit,Value) VALUES (%s, %s)"
    sql_v = "INSERT INTO volume(Unit,Value) VALUES (%s, %s)"
    sql_m = "INSERT INTO weight(Unit,Value) VALUES (%s, %s)"
    sql_s = "INSERT INTO speed(Unit,Value) VALUES (%s, %s)"
    sql_e = "INSERT INTO energy(Unit,Value) VALUES (%s, %s)"
    sql_t = "INSERT INTO time(Unit,Value) VALUES (%s, %s)"
    sql_d = "INSERT INTO data(Unit,Value) VALUES (%s, %s)"
    sql_po = "INSERT INTO power(Unit,Value) VALUES (%s, %s)"
    sql_pr = "INSERT INTO pressure(Unit,Value) VALUES (%s, %s)"
    
    length = pd.read_csv('module/Data/length.csv')
    length = length.astype(str)
    length = length.to_records(index = False)
    length = list(length)
    mycursor.executemany(sql_l, length)

    volume = pd.read_csv('module/Data/volume.csv')
    volume = volume.astype(str)
    volume = volume.to_records(index = False)
    volume = list(volume)
    mycursor.executemany(sql_v,volume)

    area = pd.read_csv('module/Data/area.csv')
    area = area.astype(str)
    area = area.to_records(index = False)
    area = list(area)
    mycursor.executemany(sql_a,area)

    mass = pd.read_csv('module/Data/mass.csv')
    mass = mass.astype(str)
    mass = mass.to_records(index = False)
    mass = list(mass)
    mycursor.executemany(sql_m,mass)

    speed = pd.read_csv('module/Data/speed.csv')
    speed = speed.astype(str)
    speed = speed.to_records(index = False)
    speed = list(speed)
    mycursor.executemany(sql_s,speed)

    energy = pd.read_csv('module/Data/energy.csv')
    energy = energy.astype(str)
    energy = energy.to_records(index = False)
    energy = list(energy)
    mycursor.executemany(sql_e,energy)

    time = pd.read_csv('module/Data/time.csv')
    time = time.astype(str)
    time = time.to_records(index = False)
    time = list(time)
    mycursor.executemany(sql_t,time)

    data = pd.read_csv('module/Data/data.csv')
    data = data.astype(str)
    data = data.to_records(index = False)
    data = list(data)
    mycursor.executemany(sql_d,data)

    power = pd.read_csv('module/Data/power.csv')
    power = power.astype(str)
    power = power.to_records(index = False)
    power = list(power)
    mycursor.executemany(sql_po,power)

    pressure = pd.read_csv('module/Data/pressure.csv')
    pressure = pressure.astype(str)
    pressure = pressure.to_records(index = False)
    pressure = list(pressure)
    mycursor.executemany(sql_pr,pressure)

    mydb.commit()

    
