#Programa principal para coletar e mostrar os dados do servidor Arduino


#Importando as bib necessárias

import sys, time

import urllib.request

import sqlite3
#import limpa_str 
#import datetime as dt
from database_function import* 

from PySide.QtCore import *
from PySide.QtGui import * 



qt_app = QApplication(sys.argv) #Iniciando a aplicação 



class MainApp(QWidget):

	def __init__(self):


		QWidget.__init__(self)
		self.setWindowTitle('The Title') #Definindo as características da janela
		self.setMinimumSize(QSize(400,400))

		self.layout = QVBoxLayout()

		self.mensagem = QLabel('Dados', self)
		self.mensagem.setAlignment(Qt.AlignCenter) #Só para alinhar a Label no centro

		self.layout.addWidget(self.mensagem)
		self.setLayout(self.layout)

	def run(self): #Mét p criar um obj da class MyThread(), conectar o sinal definido ao Slot destino, p iniciar o process. de Thread e mais
		self.processo_paralelo = MyThread()
		self.processo_paralelo.serial.connect(self.recebeDado)
		self.processo_paralelo.start()
		self.show() # 
		qt_app.exec_() # LOOP
	
	
	@Slot(str)                             #Slot p/ receber os dados
	def recebeDado(self, text):           #Função Slot
		text = str(text)	
		self.mensagem.setText(text) #Setar o texto da Label. Nesse caso, a string recebida do Thread.

		
		
		return
	

class MyThread(QThread):


    #Iniciando um sinal com carry
	serial = Signal(str)
	
    #Pegando os dados da Url
	
	url = "http://chuva.ddns.net"



	def __init__(self):
		QThread.__init__(self)
	    	
		
	def run(self):
		
		while 1:
			
			
			#Requisição da página
			
			self.page = urllib.request.urlopen(self.url)
			self.text = self.page.read().decode('utf8') 
			self.p = self.text.find('##')  #Encontrando a quantidade de chuva
			self.i = self.p + 2 #Onde começam os números da quantidade de chuva           
			
			time.sleep(1) #Esperar 1 segundo
			
			self.chuva = self.text[self.i : (self.i + 5)] #String da quant. de chuva
			
			self.serial.emit(self.chuva) #Emitindo o sinal, carregando a string MyThread.chuva
			writeDataBase(self.chuva)
            

			



	
janela = MainApp() #Instanciando a classe MainApp que cria a janela
janela.run() 
