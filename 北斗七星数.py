print("="*28,"北斗七星数","="*28)
for a in range(1,10):
   for b in range(0,10):
      for c in range(0,10):
         for d in range(0,10):
            for e in range(0,10):
               for f in range(0,10):
                  for g in range(0,10):
                     if a**7+b**7+c**7+d**7+e**7+f**7+g**7==1000000*a+100000*b+10000*c+1000*d+100*e+10*f+g:
                        print(1000000*a+100000*b+10000*c+1000*d+100*e+10*f+g,end='  ')
            
         
                        
