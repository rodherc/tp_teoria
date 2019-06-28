import sys
param = sys.argv[1]

class MTU:
	def __init__(self,fita1):
		self.fita1 = fita1		#entrada
		self.fita2 = "1"		# 1 representa o estado inicial q1
		self.fita3 = ""			# inicializa vazia

	def inicializaFita3(self): #atualiza fita3 com a palavra w
		aux = self.fita1.split("000")
		self.fita3 = aux[2]

	#faz a simulacao da MTU para a palavra de entrada
	def simulacao(self):

		palavra = self.fita3.split("0")		#pega a palavra
		entrada = self.fita1.split("000")	# divide a entrada em automato/palavra
		entrada = entrada[1].split("00")
		automato = entrada
		fitaUm = self.fita1.split("\n")  #usado so para o print
		#prints para o menu
		print("Inicio")
		print("Fita 1: " + fitaUm[0])
		print("Fita 2: " + self.fita2)
		print("Fita 3: " + self.fita3)
		print("Cabeca de leitura: 0" + "\n")

		contPosicao = [0]*len(palavra)  # lista utilizada para a heuristica
										# verificando se está em loop, verificando a quantidade de vezes
										# que a execucao possou em cada posicao da fita 
		j = 0
		contTransicao = 0    # contrador para printar a transicao atual
		while(j < len(palavra)):

			verifica = True			# booleano utilizado para verificacao de erros no decorrer das transicoes
			reconheceSimbolo = False	# booleano para reconhecer se existe transicao para o simbolo atual
			
			for i in range(len(automato)):
				
				transicao = automato[i] 		# pega cada transicao
				transicao = transicao.split("0") # divide em cada passo
				if(transicao[0] == self.fita2):	# verfica o estado
					
					if(transicao[1] == palavra[j]): # verifica o simbolo lido
						contPosicao[j] += 1

						print("---------------")
						reconheceSimbolo = True
						
						self.fita2 = transicao[2]	#atualiza com o estado atual
						contTransicao += 1			#atualiza a quantidade de transicoes
						print("transicao ", contTransicao)
						print("Fita 2: ", self.fita2)
						palavra[j] = transicao[3]	# atualiza com o novo simbolo
						self.fita3 = ""
						for i in range(len(palavra)):
							self.fita3 += palavra[i] + "0"
						print("Fita 3: " + self.fita3)
						
						if(transicao[4] == "11"): # verifica se a transicao é feita para esquerda
							if(j > 0):# primeirra posicao n pode ir pra esquerda
								j = j-2
							else:
								print("muito pra esquerda, cuidado com os seguidores de turing")
								verifica = False
								break

						break
			
			if(reconheceSimbolo == False):# nao existe transicao apra o simbolo lido
				print("palavra rejeitada")
				break
			elif(verifica == False): #se estiver fora do padrao para e rejeita
				print("teste")
				break
			else:
				if(contPosicao[j] > 1000):      #aplicacao da heuristica
												#contabilizando o numero de vezes que se repete uma
												#mesma posicao na palavra
					print("loop encontrado, parando automato")
					break
				j = j+1# atulaizacao da cabeca de leitura
				print("Cabeca de leitura: ", j, "\n")

			#else:
			#	print("ta em loop")
			#	break

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

					#verifica se existe algum simbolo diferente de 0 ou 1 no automato
					for k in range(len(transicao)):
						for j in range(len(transicao[k])):
							if(transicao[k][j] != "1"):  
								print("numero fora do padrao no automato: " + transicao[k][j])
								verifica = False
								break
				#se nao houver erros encontrados verifica se a entrada comeca com B
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
					                            
					if(verifica):				#verifica se a apalavra de entrada so contem B's
						verifica = False
						for i in range(len(palavra)):
							if(palavra[i] != "111"):
								verifica = True
						if(verifica == False):
							print("palavra so contem B")

				return verifica
		else:
			print("nao tem 000 no fim")
			return False
	else:
		print("nao tem 000 no comeco")
		return False

	
def main():
	arquivo = open(param)
	linha = arquivo.read()	# leitura do arquivo
	
	if(verificaPadroes(linha)):#verifica se o padrao da entrada
		mtu = MTU(linha)
		mtu.inicializaFita3()
		mtu.simulacao()
		
if __name__ == "__main__":
	main()
