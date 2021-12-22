selection = 'Si'

while selection == 'Si':
    number = int(input('Dame el número para la tabla de multiplicar: '))
    counter = 1
    while counter < 11:
        print(f'{number} x {counter} = {number * counter}')
        #print(number, ' x ', counter, ' = ', number * counter)
        counter += 1
    selection = input('Deseas calcular otra tabla de multiplicar? (Si/No)')
print('Adiós!')