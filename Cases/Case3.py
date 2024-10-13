import random

linhas=int(input('Número de linhas\n'))
colunas=int(input('Número de colunas\n'))
porcent=int(input('Porcentagem dos pixels ligados\n'))

numeroPixels=colunas*linhas
pixelsLigados=(porcent*numeroPixels)//100

n=1

listaPixLig=[]
while n!=pixelsLigados+1:
    linhaPixLig=random.randint(1 , linhas)
    linhaPixLig=f"{linhaPixLig:03}"

    colunaPixLig=random.randint(1, colunas)
    colunaPixLig=f"{colunaPixLig:03}"

    registro=(str(linhaPixLig)+str(colunaPixLig))
    if registro in listaPixLig:
        continue
    listaPixLig.append(registro)
    n+=1


l=1
while l!=linhas+1:
    linhaAtual=[]
    c=1
    while c!=colunas+1:
        cellAtual=f"{l:03}"+f"{c:03}"
        if cellAtual in listaPixLig:
            linhaAtual.append("1")
        else:
            linhaAtual.append("0")
            
        c+=1
    print(linhaAtual)
    l+=1


