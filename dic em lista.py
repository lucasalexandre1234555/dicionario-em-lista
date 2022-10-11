produtos = ['iphone 13', 'iphone 14', 'macbook', 'ipad', 'airpods']
vendas2021 = [910000, 0, 139072, 690000, 1450199]
vendas2022 = [1320000, 192256, 450000, 120099, 992109]
 
resumo = {}
 
for k, v in enumerate(produtos):
    resumo[v] = (vendas2021[k], vendas2022[k])
 
print(resumo)
 
resumo_produtos = []
resumo_vendas_2021 = []
resumo_vendas_2022 = []
 
for i in resumo:
    resumo_produtos.append(i)
    resumo_vendas_2021.append(resumo[i][0])
    resumo_vendas_2022.append(resumo[i][1])
 
print('')
print(resumo_produtos)
print(resumo_vendas_2021)
print(resumo_vendas_2022)
