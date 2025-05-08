# Structure FOR
list_values = []
for i in range(5):
    num = int(input('Informe um número: '))
    list_values.append(num)
print(f'Os números são {list_values}')

# Structure WHILE
list_names = []
answer = ''
while answer != 'n':
    name = input('Informe um nome: ')
    list_names.append(name)
    answer = input('Deseja informar outro nome? [s/n]: ')

print(f'Os nomes informados foram: {name}')
