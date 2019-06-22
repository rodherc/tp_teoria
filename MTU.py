import sys
param = sys.argv[1]

class MTU:
	def __init__(self,fita1):
		self.fita1 = fita1		#entrada
		self.fita2 = "1"		# 1 representa o estado inicial q1
		self.fita3 = ""

	def inicializaFita3(self): #palavra w
		aux = self.fita1.split("000")
		self.fita3 = aux[2]

		
	def simulacao(self):

		palavra = self.fita3.split("0")
		entrada = self.fita1.split("000")
		entrada = entrada[1].split("00")
		automato = entrada

		verificaEstado = True
		verificaSimbolo = True
		for j in range(len(palavra)):

			for i in range(len(automato)):

				transicao = automato[i] # pega cada transicao
				transicao = transicao.split("0") # divide em cada passo
				if(transicao[0] == self.fita2):	# verfica o estado
					
					if(transicao[1] == palavra[j]): # verifica o simbolo lido
						
						print("fita2 antes :", self.fita2)
						self.fita2 = transicao[2]	#att com o estado atual
						print("fita 2 depois:", self.fita2)
						print("palavra lida :", palavra[j])
						palavra[j] = transicao[3]	# att com o novo simbolo
						print("palavra escrita :", palavra[j])
						if(transicao[4] == 11):
							j = j-2    ########## nao da certo , mover pra esquerda

		self.fita3 = ""
		for i in range(len(palavra)):
			self.fita3 += palavra[i] + "0"
			print("passo ", i,self.fita3)
		print("fita 3 ::::::" ,self.fita3)

#verifica se as transicoes passadas estao no formato -> en(qi)0en(x)0en(qj)0en(y)0en(d)
def verificaPadroes(linha):

	if(linha[0] == "0") and (linha[0] == linha[1] == linha[2]): 								# começa com 000
		if(linha[0] == linha[(len(linha)-2)] == linha[(len(linha)-3)] == linha[(len(linha)-4)]):# termina com 000

			linha = linha.split("000")			# divide a linha em 2(automato e palavra)
			if(linha[2] == "\n"): 				# se entrada n contem palavra w
				print("nao contem palavra w")
				return False
			else:
				automato =  linha[1]
				palavra = linha[2]
				automato = automato.split("00") 	# automato divido em transicoes
				
				#verifica padrao do
				verifica = True
				for i in range(len(automato)):
					transicao = automato[i]			# pega cada transicao
					transicao = transicao.split("0")# divide em cada passo
					print(transicao)
					if(len(transicao) != 5):		# uma transicao de uma  MTU tem o formato de tamanho 5 -> en(qi)0en(x)0en(qj)0en(y)0en(d)
						verifica = False			# se entrar n tem o formato
						break

				#verifica determinismo
				for i in range(len(automato)):
					contador = 0
					transicao = automato[i]			# pega cada transicao
					transicao = transicao.split("0")# divide em cada passo
					if(i < 0):
						for j in range(len(automato)):
							
							transAux = automato[j]
							transAux = transAux.split("0")
							if(transicao[0] == transAux[0]):
								if(transicao[1] == transAux[1]):
									contador +=1
						if(contador != 1):
							print("nao determitica")
							break



				return verifica
		else:
			print("nao tem 000 no fim")
			return False
	else:
		print("nao tem 000 no comeco")
		return False

	
def main():
	arquivo = open(param)
	
	linha = arquivo.read()			# leitura do arquivo
	
	if(verificaPadroes(linha)):	# se tem a forma R(M)w
		mtu = MTU(linha)
		mtu.inicializaFita3()
		mtu.simulacao()
	else:							# nao tem
		print("movendo para direita indefinidamente")
		
		
		
if __name__ == "__main__":
	main()
