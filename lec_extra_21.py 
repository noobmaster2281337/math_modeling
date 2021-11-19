a = float(input("введите кофициент а = "))
b = float(input("введите кофициент b = "))
c = float(input("введите кофициент с = "))
 
if a != 0:
  if b == 0 and c == 0:
    print("один корень")
    print(f'x = {0}')
 
  elif  b !=0 and c != 0:
    d = b ** 2 - 4*a*c
    print(f'D= {d}')
    
    if d < 0:
      print("Нет корней")
    
    elif d == 0:
        print("один корень")
        x = -b / (2*a)
        print(f'x=, {x}')
 
    else:
        print("два корня")
        x1 = ((-b + d ** 0.5) / 2*a)
        x2 = ((-b - d ** 0.5) / 2*a)
        print(f'x1= {x1} x2= {x2}')

  elif b == 0:
    print("Неполное кв. ур")

    if -c / a < 0:
      print("Нет корней")

    else:
      print("2 Корня")
      x1 = (-c / a)
      x2 = -x1
      print("x1=", x1, "x2=", x2)

  elif c == 0:
    print("Неполное кв. ур")
    print("2 Корня")
    x1 = 0
    x2 = -b / a
    print(f'x1= {x1} x2= {x2}')
else:
  print("невозможно")