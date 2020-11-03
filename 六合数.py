print("="*8,"六合数","="*8)
for a in range(1,10):
   for b in range(0,10):
      for c in range(0,10):
         for d in range(0,10):
            for e in range(0,10):
               for f in range(0,10):
                  if a**6+b**6+c**6+d**6+e**6+f**6==100000*a+10000*b+1000*c+100*d+10*e+f:
                     print(100000*a+10000*b+1000*c+100*d+10*e+f,"\t",end='   ')
