def freq (lista):
  elementos=[]
  frequencia=[] 
  for valorlido in lista:
    if valorlido not in elementos:
      elementos.append(valorlido)
      frequencia.append(1)
      print(frequencia)
    else:
      for i in range(0,len(elementos)):
        if valorlido==elementos[i]:
          frequencia[i]+=1
          break
  for j in range(0,len(elementos)):
      print (str(elementos[j])+' ocorre '+str(frequencia[j])+' vez(es)')
  
lista=["yane", "arroz", "yan", "yan", "brocolis", "arroz"]
print(freq(lista))