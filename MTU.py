import sys
param = sys.argv[1]  # pegando o argumento

#qi x = qj y d    sintaxe das transições

#a = 1  b = 11  B = 111
#R = 1  l = 11
#q0 = 1  q1 = 11 ....

def verificaTransicoes(arquivo): #verifica se as transicoes passadas estao no formato -> en(qi)0en(x)0en(qj)0en(y)0en(d)

	linha = arquivo.read()	# leitura do arquivo
	linha = linha.split("000") # divide a linha em 2(automato e palavra)
	automato =  linha[1]
	palavra = linha[2]
	automato = automato.split("00") # automato divido em transicoes
	
	verifica = True
	for i in range(len(automato)):
		transicao = automato[i]	# pega cada transicao
		transicao = transicao.split("0") # divide em cada passo
		print(transicao)
		if(len(transicao) != 5): # uma transicao de uma  MTU tem o formato de tamanho 5 -> en(qi)0en(x)0en(qj)0en(y)0en(d)
			verifica = False
			
	return verifica



#def verificaDeterminismo(arquivo): #verifica determinismo do automato

	
def main():
	arquivo = open(param)
	#~ lendoArq = True
	#~ while(lendoArq):
		#~ aux = arquivo.read(1)
		
		#~ if(aux == ""):
			#~ lendoArq = False
	
	if(verificaTransicoes(arquivo)): # se ta ok
		#verificaDeterminismo(arquivo)
		
if __name__ == "__main__":
	main()
