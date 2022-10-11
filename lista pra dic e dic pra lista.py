# Transformar listas em dicionário e
# depois transformar dicionário em listas
# Solução do prof. Polizello

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
    
vendas = list(zip(vendas2019, vendas2020))

vendas_produtos = dict(zip(produtos,vendas))
print(vendas_produtos)

produto_meu = list(dict.fromkeys(vendas_produtos))
print(produto_meu)

ano2019 = []
ano2020 = []
for ano19,ano20 in vendas_produtos.values():
    ano2019.append(ano19)
    ano2020.append(ano20)

print(ano2019)
print(ano2020)
