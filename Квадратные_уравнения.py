
#while (True):                                                  
a = float(input("Введите значение a= "))                                  
b = float(input("Введите значение b = "))
c = float(input("Введите значение c = "))





D = b**2.0- 4.0*a*c

if D < 0.0:
    print("уравнение не имеет решений диствительних числах")
    
elif D > 0.0:
    
    if a == 0:
        print("x_1 = " + str(-c/b)
        
    if a > 0:
        x1 = (-b + D) / (2 * a)
        x2 = (-b - D) / (2 * a)
        print("x_1 = ",x1)
        print("x_2 = ",x2)
        
elif D == 0.0:
    
    if a == 0:
        print("x = 0")
        
    if a > 0:
        x = -b / (2 * a)
        print("x =",x)
    
        
