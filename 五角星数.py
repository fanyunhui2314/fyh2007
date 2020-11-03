print("="*8,"五角星数","="*8)
for a in range(1,10):
   for b in range(0,10):
      for c in range(0,10):
         for d in range(0,10):
            for e in range(0,10):
               if a**5+b**5+c**5+d**5+e**5==10000*a+1000*b+100*c+10*d+e:
                  print(10000*a+1000*b+100*c+10*d+e,"\t",end='   ')
