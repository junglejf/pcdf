##Variaveis globais
import matplotlib.pyplot as plt


kx = [0] #contém o valor de k no intervalo correspondente
pos = [0] #define as fronteiras dos intervalos
nome = ["zero", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]
passos =[0.0]
ponto_medio = 0

def print_text(texto):
    print(texto)

def define_passos():
        x = int(input('Quantos passos você quer dar entre os pontos 0 e 1? '))
        if x%2 == 0 :
                print('Escolha um número impar')
                exit(1)
        step = 1/(x+1)
        for i in range(1, x+1):
                passos.append(passos[i-1] + step)
        passos.append(1.0)
        #print('passos:')
        #print(passos)

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

#define os eixos a serem plotados
def eixos (matriz, parametro):
    filtro = []
    
    for pos in range (0,len(parametro)):
        if parametro[pos]:
            lista = []
            for i in range (0,len(matriz)):
                lista.append(matriz[i][pos])
            filtro.append(lista)
    
    return filtro

#gráfico
def desenha_grafico (titulo,eixoX, eixo, nome_eixoX, nome_eixoY,nome_curva,figura):
    grafico = figura
    plt.title(titulo)
    a = nome_curva[0]
    if (type (eixo[0]) is list): # se for um conjunto de valores a serem plotados
        for i in range(0,len(eixo)): # (x, y[N] ):
                plt.plot(eixoX,eixo[i], label = 'x = '+str(nome_curva[i]), linewidth = 4.0 )
    #else: # se for somente uma variÃ¡vel em y (x,y)
        #plt.plot(eixoX,eixoYadicional, label = 'Mosquito Adulto sem medida de Controle')
        #plt.plot(eixoX,eixo, label = 'Mosquito Adulto apos Campanha de Controle')
        
    plt.ylabel(nome_eixoY)
    plt.xlabel(nome_eixoX)
    #plt.show()
    return grafico 

#Chama função inicial que vai determinar os valores de K durante toda a execução
define_passos()
define_valores()


kx = kx[1:]
pos = passos 



#Define o ponto médio
ponto_medio = int(len(passos)/2)


##Inicio da resolucao do problema


#Definindo agora os valores para os próximos tempos
deltaX = passos[1]

# Varíaveis que serão modificadas
###############################################
deltaT = 0.01
temperatura_minima = 55
temperatura_maxima = 90
tempo = 140000
#############################################
print("\n \n############## Temperatura que liga o foguinho = " +str(temperatura_minima)+" graus ##################")
print("############ Temperatura que desliga o foguinho = "+str(temperatura_maxima)+" graus ################")
print("\n deltaX = "+str(deltaX))
print(" deltaT = "+str(deltaT))
print("\n k= 1 até metade da barra e k=2 na outra metade da barra \n")
############### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ###############

passos_tempo = []
for i in range(tempo):
        passos_tempo.append(i)


#definindo todos os valores no tempo = 0, é dado pela condição inicial do problema

tempo_atual = []
for k in passos:
        tempo_atual.append(10 + 280 * k - 380*k*(k-0.5))
temperatura_no_tempo = []
temperatura_no_tempo.append(tempo_atual)



##Passos para descobrir as temperaturas em cada passo interno do dominio
for i in range(1, len(passos_tempo)):
        temperatura_atual = [10]
        foguinho = 0
        if i>1:
                if(temperatura_no_tempo[-2][ponto_medio] > temperatura_no_tempo[-1][ponto_medio]):
                        if(temperatura_no_tempo[-1][ponto_medio] <= temperatura_minima): 
                                foguinho = 200
                else:
                        if(temperatura_no_tempo[-1][ponto_medio] < temperatura_maxima): 
                                foguinho = 200   
        for j in range(1, len(passos)-1):             
                gama = (deltaT*kx[j])/(deltaX*deltaX)
                temperatura_atual.append((gama*(temperatura_no_tempo[-1][j-1] - 2*(temperatura_no_tempo[-1][j]) + (temperatura_no_tempo[-1][j+1]))) + temperatura_no_tempo[-1][j] + (foguinho*deltaT))
        temperatura_atual.append(100)
        temperatura_no_tempo.append(temperatura_atual)

#print('fim:\n')
#for i in range(0, len(temperatura_no_tempo)):
        #print('\nEm t = ' + str(passos_tempo[i]) + ':')
        #print(temperatura_no_tempo[i])



#temperatura_no_tempo[i][ponto_medio]  --> plota o ponto médio
parametros = [True] * len(temperatura_no_tempo[0])
parametros[ponto_medio] = True
parametros[0] = True
parametros[-1] = True
eixoY = eixos(temperatura_no_tempo,parametros)
titulo = ('Propagação de calor em uma barra')
nome_eixoY = ('Temperatura (K)')
nome_eixoX = ('Tempo (s)')
grafico = plt.figure(figsize=(10,5))
p1 = desenha_grafico (titulo,passos_tempo, eixoY, nome_eixoX, nome_eixoY,pos,grafico)
plt.legend(loc='upper center', bbox_to_anchor = (1.1,0.5),shadow = True)


