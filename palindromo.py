
def potencia(ini,poten): #sin usar un ciclo
    if ini <= poten:
        potenciado=2**ini
        print('El número 2 elevado a: '+str(ini)+ ' es: ',potenciado)
        potencia(ini+1,poten)
    else:
        print('FIN')


def palindromo(palabra):
    palabra= palabra.replace(' ','')
    palabra=palabra.lower()
    invertida=palabra[::-1]
    if invertida==palabra:
        return True
    else:
        return False



def run():
    palabra =input('Ingrese una palabra')
    es_palindromo = palindromo(palabra)
    if es_palindromo==True:
        print('Es palindromo')
    else:
        print('No es palindromo')



if __name__=='__main__': #punto de entra en un programa de python
    potencias=int(input('Ingrese hasta la potencia que desea'))
    potencia(0,potencias)
