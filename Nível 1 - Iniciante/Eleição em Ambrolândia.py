x = 1 #x = 1 e y = 1 devido que no problema, diz que cada candidato tem pelo menos um voto, ou seja, nao tera menos de 1 voto, para evitar isso setamos 1 para cada variavel
y = 1
z = 0
w = 0
i = 0
a = 0
b = 0
k = 93 
while(True):
    try: #Error handling
        n = int(input()) 
        if(n >= 0 and i <= 100000000 ): #Iteramos i vezes, ou ate que n seja menor 0, ou seja -1 ou -2...
        #Daqui pra baixo, sempre que n (o voto) entrar dentro de algum desses if's, entao incrementamos o valor em cada variavel, que no caso
        #x representa o alibaba e o y alcapone, z os votos brancos e w os votos invalidos
            if(n == 83) : 
                x += 1 
            elif(n == 93):
                y += 1
            elif(n == 0):
                z += 1
            else:
                w += 1
        else:
            if(x > y):
                k = 83
            a = ((x-1)*100)/((x-1)+(y-1)+z); #Aqui computamos o percentual de cada candidato, lembrando que como cada candidato tem  pelo menos 1 voto temos que retirar esse 1 na hora.
            b = ((y-1)*100)/((x-1)+(y-1)+z);
            print(x-1) #Aqui a mesma coisa do que o comentario assim
            print(y-1)
            print(z)
            print(w)
            print(k)
            print("%.2f"%a)
            print("%.2f"%b)
            break
        i += 1 #Incrementamos i para a condição do while nao ir pra looping infinito, assim quando i chegar a 1000000000 execucoes o laco eh interrompido com o break
    except EOFError:
        break