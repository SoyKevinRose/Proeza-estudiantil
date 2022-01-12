def conversor(tipo_moneda,dolar):
    pesos=float(input('¿Cuántos '+ tipo_moneda +' tiene'))
    total=dolar/pesos
    total=round(total,2)
    print('Usted tiene:',total,' dolar(es)')

menu=""""
Bienvenido al sistema de conversión a dolares.

////////////////////////////////////////// 

Diseñado por: Proeza estudiantil S.A

~---~---~---~---~---~---~---~---~---~---~

 seleccione una de la siguientes opciones:
 1. Pesos Colombianos
 2. Pesos Mexicanos
 3. Pesos Chilenos

 ~---~---~---~---~---~---~---~---~---~---~
"""
opcion=input(menu)
if opcion=='1':
    conversor('pesos Colombianos',4080)
elif opcion=='2':
    conversor('pesos Mexicano',20)
elif opcion=='3':
    conversor('pesos Chilenos',837)
else:
    print('ingrese una opción válida')


    
    

