a = float(input('输入三角形第一条边长： '))
b = float(input('输入三角形第二条边长： '))
c = float(input('输入三角形第三条边长： '))
while a+b<=c or a+c<=b or b+c<=a:
   print('输入的边构不成三角形，请重新输入!')
   a =float(input ('输入三角形第一条边长:'))
   b =float(input ('输入三角形第二条边长:'))
   c =float(input ('输入三角形第三条边长:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("三角形面积等于%.2f"%area)
