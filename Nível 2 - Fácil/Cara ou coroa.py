var=[int(x) for x in input().split()]
lista,va,lt,c,Soma,D=['C','K'],var[0],[],2,0,var[1]
def sum(lista,var,lt):
    ck=['C','K']
    if var > 1:
        h=lt[:]
        lt=[]
        for k in range(2):
            l=[]
            for i in range(len(lista)):
                x=ck[k]+lista[i]
                l.insert(0, x)
            for i in range(len(l)):
                lt.append(l[i])
    if len(lt[0]) == var:
        return lt
    return sum(lt,var,lt)
ll=sum(lista,va,lt)
def Contador(lista2,Soma,D):
    for l in lista2:
        ck,cc=l.count('K'),l.count('C')
        if abs(ck-cc) == D:
            Soma+=1
    return Soma
print(Contador(ll,Soma,D))


''' 2ª forma
def difference(array):
    counter = 0
    for l in range(len(array)):
        if abs(array[l].count("K") - array[l].count("C")) == int(D):
            counter += 1
    return counter
def sample(number):
    return ["C", "K"] if number == 1 else [i + j for i in ["C", "K"] for j in sample(number - 1)]
N, D = input().split()
print(difference(sample(int(N))))

'''