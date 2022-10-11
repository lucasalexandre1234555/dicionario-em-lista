# Transformar listas em dicionário e
# depois transformar dicionário em listas
# Solução do Luis Miguel

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
 
resumo = {}
 
for k, v in enumerate(produtos):
    resumo[v] = (vendas2019[k], vendas2020[k])
 
print(resumo)
 
resumo_produtos = []
resumo_vendas_2019 = []
resumo_vendas_2020 = []
 
for i in resumo:
    resumo_produtos.append(i)
    resumo_vendas_2019.append(resumo[i][0])
    resumo_vendas_2020.append(resumo[i][1])
 
print('')
print(resumo_produtos)
print(resumo_vendas_2019)
print(resumo_vendas_2020)
