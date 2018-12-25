numb=45673
Numbs=[]
i=0
while i < len(str(numb)):
    Numbs.append(int((str(numb))[i]))
    i=i+1
Maxnumb = max(Numbs)
print("Максимальное число -",Maxnumb)
