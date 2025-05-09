def registration_vendor(num):
    'Cadastra vendedores'
    cont = 1
    for vendor in range(num):
        name_vendor = input(f'\nInforme o nome do vendedor {cont}: ')
        sales = float(input('\nInforme o valor das vendas: '))
        vendor = {
            'Nome do Vendedor': name_vendor,
            'Valor das Vendas': sales,
        }
        cont += 1
        list_registration.append(vendor)


def calc_total_sales_and_len_sales():
    'Calcula total de vendas e media de vendas'
    ttl = 0.0
    for vendor in list_registration:
        ttl = ttl + vendor['Valor das Vendas']
    ln = ttl / len(list_registration)
    return ttl, ln


def find_best_sales_and_vendor():
    'Buscar maior venda e maior vendedor'
    best_sales = 0.0
    best_vendor = ''
    for v in list_registration:
        if v['Valor das Vendas'] > best_sales:
            best_sales = v['Valor das Vendas']
            best_vendor = v['Nome do Vendedor']

    return best_sales, best_vendor


list_registration = []

print('\n'+24*'*'+' Bem vindo ao Terminal de Vendas da Loja '+24*'*'+'\n')
qtd = int(input('Digite quantos vendedores serão cadastrados no sistema: '))
print('\n'+89*'*')
registration_vendor(qtd)

print('\n'+89*'*'+'\n')
print('Relação dos Vendedores e suas Vendas\n')
for vendor in list_registration:
    print(vendor)
print('\n'+89*'*'+'\n')

ttl_sales, ln_sales = calc_total_sales_and_len_sales()
print(f'Total de Vendas: {ttl_sales}')
print(f'Media das Vendas: {ln_sales}')
print('\n'+89*'*'+'\n')

bst_sales, bst_vendor = find_best_sales_and_vendor()
print(f'Melhor Venda: {bst_sales}')
print(f'Melhor Vendedor: {bst_vendor}')
print('\n'+89*'*'+'\n')
