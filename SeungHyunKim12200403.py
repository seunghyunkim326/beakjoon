A = int(input())
B = int(input())
C = int(input())
if A==B==C==60:
    print("Equilateral")
elif A+B+C==180:
    if A!=B!=C!=A:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")