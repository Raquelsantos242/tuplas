#carregar tupla com n países via teclado

paises = ()

while True:
    pais = input('Digite o nome de um país ou "sair" para encerrar: ')
    if pais == 'sair':
        break
    else:
        paises = paises + (pais,)
        
print(paises)