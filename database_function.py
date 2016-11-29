import time
import sqlite3

def writeDataBase(rain):

    #Conecta com um banco de dados
    conn = sqlite3.connect('RainDataBase.db')
    
    ##Cria um cursor para trabalhar com esses dados
    c = conn.cursor()    

    ##Cria uma tabela se ela não existe ainda
    c.execute('''CREATE TABLE if not exists Chuva
             (date1 text, quantChuva real)''')     

    ##Muda o tipo da variavel argumento da função para float
    rain = float(rain)    

    ##Pega a data e o horário e aloca na variável dateID
    dateID = time.strftime("%d/%m/%Y %H:%M:%S") 

    ##Insert a new line in the table
    c.execute("INSERT INTO Chuva VALUES ('{dateID}', {rain})".format(dateID = dateID, rain=rain))

    
    conn.commit()

    
    conn.close()
