import sys
param = sys.argv[1]

class MTU:
	def __init__(self,fita1):
		self.fita1 = fita1		#entrada
		self.fita2 = "1"			# 1 representa o estado inicial q1
		self.fita3 = ""

	def inicializaFita3(self): #palavra w
		aux = self.fita1.split("000")
		self.fita3 = aux[2]

		
	def simulacao(self):
		print("fita 3",self.fita3)
		palavra = self.fita3.split("0")
		entrada = self.fita1.split("000")
		print("aquiiiiii",entrada[1])
		entrada = entrada[1].split("00")
		automato = entrada
		print("automato",len(automato))
		print(automato)
		for j in range(len(palavra)):
			for i in range(len(automato)):
				transicao = automato[i] # pega cada transicao
				transicao = transicao.split("0") # divide em cada passo
				print("aiaiaia",self.fita2)
				print("transicao",transicao[0])
				if(transicao[0] == self.fita2):
					print("entrei")
					print("palavra", palavra[j])
					print("transicao", transicao[1])
					if(transicao[1] == palavra[j]):
						#print("entrou if",transicao[0]," ", transicao[1]," ",transicao[2]," ",transicao[3]," ",transicao[4])
						print("fita2", self.fita2)
						self.fita2 = transicao[2]
						print("fita2 depois", self.fita2)
						palavra[j] = transicao[3]
						print(palavra[j])
		
#verifica se as transicoes passadas estao no formato -> en(qi)0en(x)0en(qj)0en(y)0en(d)
def verificaTransicoes(linha):#####OBS TEM QUE ADD VERIFICAR OS 000 DO COMEÇO E DO FIM################################
	
	linha = linha.split("000")			# divide a linha em 2(automato e palavra)
	if(linha[2] == "\n"): 				# entrada n contem palavra w
		print("nao contem palavra w")
		return False
	else:
		automato =  linha[1]
		palavra = linha[2]
		automato = automato.split("00") # automato divido em transicoes
		
		verifica = True
		for i in range(len(automato)):
			transicao = automato[i]			# pega cada transicao
			transicao = transicao.split("0")# divide em cada passo
			print(transicao)
			if(len(transicao) != 5):		# uma transicao de uma  MTU tem o formato de tamanho 5 -> en(qi)0en(x)0en(qj)0en(y)0en(d)
				verifica = False
				
		return verifica
	
	

	
def main():
	arquivo = open(param)
	
	linha = arquivo.read()			# leitura do arquivo
	
	if(verificaTransicoes(linha)):	# se tem a forma R(M)w
		mtu = MTU(linha)
		mtu.inicializaFita3()
		mtu.simulacao()
	else:							# nao tem
		print("movendo para direita indefinidamente")
		
		
		
if __name__ == "__main__":
	main()
