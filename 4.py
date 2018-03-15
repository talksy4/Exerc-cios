frase=input("frase:")
vogais=list("aeiouAEIOU")
consoantes=list("bcdefghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVXYZ")
qv=0
qcon=0
qcaracteres=0
for i in range(len(frase)):
  #if frase[i]!=" ":
    if frase[i] in vogais:
      qv+=1
    elif frase[i]in consoantes:
      qcon=1+qcon
    else:
      qcaracteres+=1
      
print (qv)
print (qcon)
print (qcaracteres)
