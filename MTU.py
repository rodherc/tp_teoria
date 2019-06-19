import sys
param = sys.argv[1]

class MTU:
	def __init__(self,fita1):
		self.fita1 = fita1		#entrada
		self.fita2 = 1			# 1 representa o estado inicial q1
		self.fita3 = 0

	def inicializaFita3(self): #palavra w
		aux = self.fita1.split("000")
		fita3 = aux[2]
		print(len(fita3))
		
#verifica se as transicoes passadas estao no formato -> en(qi)0en(x)0en(qj)0en(y)0en(d)
def verificaTransicoes(linha):

	linha = linha.split("000")		# divide a linha em 2(automato e palavra)
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
	else:							# nao tem
		print("movendo para direita indefinidamente")
		
		
		
if __name__ == "__main__":
	main()
