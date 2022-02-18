tam1=int(input())
ln=[]
lx=[]
lt=[]
if tam1!=0:
        #ln=[]
        #lx=[]
        #lt=[]
    for i in range(tam1):
        n=int(input())
        ln.append(n)
    #else:
        #print('Erro - A lista deve ter pelo menos 1 elemento.')
        #break
    tam2=int(input())
    if tam2!=0:
        for i in range(tam2):
            x=int(input())
            lx.append(x)
        for i in range(tam1):
            lt.append(ln[i])
        for i in range(tam2):
            lt.append(lx[i])
        for i in range(len(lt)):
            print(lt[i], end=' ')
    else:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
else:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
    #1 1 3 1 2 3


''' 2ª forma
tamanho1 = int(input())
lista1 = []
lista2 = []
lista3 = []

for i in range(tamanho1):
    lista1.append(int(input()))
    lista3.append(lista1[i])
tamanho2 = int(input())

for i in range(tamanho2):
    lista2.append(int(input()))
    lista3.append(lista2[i])

for i in range(len(lista3)):
    print(lista3[i])'''




