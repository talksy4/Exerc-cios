#função que calcula o percentual
def calc_percent (v,p):
  percentual=v*p/100
  return percentual

#função que recebe o valor básico de um produto
def recebvalor (preço):
  iimport = calc_percent(preço,50)
  icircmerca = calc_percent(preço,3)
  taxaentrega = calc_percent(preço,10) + calc_percent(icircmerca,2)
  taxas = iimport + icircmerca + taxaentrega
  return taxas
  
preço=float(input("Valor básico:"))
#print (recebvalor(preço))
total=preço+recebvalor(preço)
perctaxas=(recebvalor(preço)*100)/preço
print ("valor basico: " + str(preço) +  " - taxas: " + str(recebvalor(preço)) + " - total: " + str(total)+ " percentual das taxas: " + str(perctaxas)+"%")
