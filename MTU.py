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

		
	def simulacao(self, padrao):

		palavra = self.fita3.split("0")
		entrada = self.fita1.split("000")
		entrada = entrada[1].split("00")
		automato = entrada

		contPosicao = [0]*len(palavra)

		for i in range(len(palavra)):
			contPosicao[i] = 0

		verificaEstado = True
		verificaSimbolo = True
		j = 0
		while(j < len(palavra)):
			#print("j no comeco",j)

			verifica = True

			if(padrao == False):
				print("movendo para direita indefinidamente")
				break
			else:
			
				for i in range(len(automato)):
					
					transicao = automato[i] # pega cada transicao
					transicao = transicao.split("0") # divide em cada passo
					if(transicao[0] == self.fita2):	# verfica o estado
						
						if(transicao[1] == palavra[j]): # verifica o simbolo lido
							contPosicao[j] += 1
							
							print("fita2 antes :", self.fita2)
							self.fita2 = transicao[2]	#att com o estado atual
							print("fita 2 depois:", self.fita2)
							print("palavra lida :", palavra[j])
							palavra[j] = transicao[3]	# att com o novo simbolo
							print("palavra escrita :", palavra[j])
							
							print("posicao 4", transicao[4])
							if(transicao[4] == "11"):
								if(j > 0):# primeirra posicao n pode ir pra esquerda
									j = j-2
									print("j",j)
								else:
									print("muito pra esquerda, cuidado com os seguidores de turing")
									verifica = False
									break
				if(verifica == False): #se estiver fora do padrao entra em loop
					padrao = False
					#break
				else:
					if(contPosicao[j] > 100):      #aplicacao da heuristica
						                           #contabilizando o numero de vezes que se repete uma
												   #mesma posicao na palavra
						print("loop encontrado, parando automato")
						break
					j = j+1
				#else:
				#	print("ta em loop")
				#	break

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
				palavra = palavra.split("0")
				
				#verifica padrao do automato
				verifica = True
				for i in range(len(automato)):
					transicao = automato[i]			# pega cada transicao
					transicao = transicao.split("0")# divide em cada passo
					print(transicao)
					if(len(transicao) != 5):		# uma transicao de uma  MTU tem o formato de tamanho 5 -> en(qi)0en(x)0en(qj)0en(y)0en(d)
						verifica = False			# se entrar n tem o formato
						print("fora do padrao")
						break

				#verifica determinismo
				for i in range(len(automato)):
					contador = 0
					transicao = automato[i]			# pega cada transicao
					transicao = transicao.split("0")# divide em cada passo
					if(i > 0):

						for j in range(len(automato)):
							transAux = automato[j]
							transAux = transAux.split("0")
							if(transicao[0] == transAux[0]):
								if(transicao[1] == transAux[1]):
									contador +=1
						if(contador != 1):
							print("nao deterministica")
							return False
							break

					for k in range(len(transicao)):
						for j in range(len(transicao[k])):
							print("olha o numero: " + transicao[k][j])
							if(transicao[k][j] != "1"):  #verifica se existe algum simbolo diferente de 0 ou 1 no automato
								print("numero fora do padrao no automato: " + transicao[k][j])
								verifica = False
								break

				if(verifica):
					if(palavra[0] == "111"):      #verifica se comeca com B
						for i in range(len(palavra)):
							for j in range(len(palavra[i])):
								if(palavra[i][j] != "1"):  #verifica se existe algum simbolo diferente de 0 ou 1 na palavra
									print("numero fora do padrao na palavra: " + palavra[i][j])
									verifica = False
									break
							
					else:
						print("palavra nao inicia com B")
						verifica = False
					                            
					#verificar a necessidade dessa funcao e, se caso necessario, passar para a simulacao
					#if(verifica):				#verifica se so tem B na palavra
					#	verifica = False
					#	for i in range(len(palavra)):
					#		if(palavra[i] != "111"):
					#			verifica = True

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
	
	mtu = MTU(linha)
	mtu.inicializaFita3()
	mtu.simulacao(verificaPadroes(linha))
	
		
		
		
if __name__ == "__main__":
	main()
