##Variaveis globais


kx = [0] #contém o valor de k no intervalo correspondente
pos = [0] #define as fronteiras dos intervalos
nome = ["zero", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]
passos =[0.0]
ponto_medio = 0

def define_passos():
        x = int(input('Quantos passos você quer dar entre os pontos 0 e 1?'))
        if x%2 == 0 :
                print('Escolha um número impar')
                exit(1)
        step = 1/(x+1)
        for i in range(1, x+1):
                passos.append(passos[i-1] + step)
        passos.append(1.0)
        print('passos:')
        print(passos)

def define_valores():
    p=0
    q=0
    partes = int(input('Quantos valores diferentes assume o k nesse problema? '))
    for numero in range(1, partes+1):
        posicao = float(input('O '+ str(nome[numero]) +' intervalo de k é de ' + str(pos[numero - 1]) + ' até ? '))
        if posicao not in passos:
                print('Não é possível!')
                exit(1)
        pos.append(posicao)
        valor = float(input('E quanto vale k de '+ str(pos[numero - 1]) +' a ' + str(posicao) + '? '))
        for i in range(p, len(passos)):
                p = p+1
                q = q+1
                if passos[i] == posicao:
                        break
        for i in range(q):
                kx.append(valor)
        q = 0

 

#Chama função inicial que vai determinar os valores de K durante toda a execução
define_passos()
define_valores()


kx = kx[1:]
pos = passos 
print('\n\nValores de k para cada x listado abaixo: ')
print(kx)
print(pos)
print('\n')


#Define o ponto médio
ponto_medio = int(len(passos)/2)


##Inicio da resolucao do problema



tempo = 300
passos_tempo = []
for i in range(tempo):
        passos_tempo.append(i)


#definindo todos os valores no tempo = 0, é dado pela condição inicial do problema

tempo_atual = []
for k in passos:
        tempo_atual.append(int(10 + 280 * k - 380*k*(k-0.5)))
temperatura_no_tempo = []
temperatura_no_tempo.append(tempo_atual)

#Definindo agora os valores para os próximos tempos

deltaT = 0.01
deltaX = passos[1]

##Passos para descobrir as temperaturas em cada passo interno do dominio
for i in range(1, len(passos_tempo)):
        temperatura_atual = [10]
        for j in range(1, len(passos)-1):
                foguinho = 0
                if(i>1 and temperatura_no_tempo[-2][ponto_medio] > temperatura_no_tempo[-1][ponto_medio]):
                        if(temperatura_no_tempo[-1][ponto_medio] <= 55): 
                                foguinho = 200
                if(i>1 and temperatura_no_tempo[-2][ponto_medio] < temperatura_no_tempo[-1][ponto_medio]):
                        if(temperatura_no_tempo[-1][ponto_medio] >= 155): 
                                foguinho = 0
                
                gama = (deltaT*kx[j])/(deltaX*deltaX)
                temperatura_atual.append(int(gama*(temperatura_no_tempo[-1][j-1] - 2*(temperatura_no_tempo[-1][j]) + (temperatura_no_tempo[-1][j+1])) + temperatura_no_tempo[-1][j] + foguinho))
        temperatura_atual.append(100)
        temperatura_no_tempo.append(temperatura_atual)


print('fim:\n')
for i in range(0, len(temperatura_no_tempo)):
        print('\nEm t = ' + str(passos_tempo[i]) + ':')
        print(temperatura_no_tempo[i])

#temperatura_no_tempo[i][ponto_medio]  --> plota o ponto médio


