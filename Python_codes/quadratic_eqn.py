a = float(input("Enter coef a: "))
b = float(input("Enter coef b: "))
c = float(input("Enter coef c: "))

under_root = b**2 - 4*a*c


if under_root > 0:
    #Two roots case
    sqrt = under_root**0.5
    root1 = (-b +sqrt)/2*a
    root2 = (-b - sqrt)/2*a
    print("Two roots", root1,root2)
elif under_root ==0:
    #One root case
    root1 = -b/2*a
    print("One root: ", root1)
else:
    #Zero root case
    print("Zero roots")




#(x -1)(x-2) x^2 -3x +2
#a =1,b= -3, c=2

#x^2
#a =1 b = 0,c =1

#a=1, b=-2,c=1