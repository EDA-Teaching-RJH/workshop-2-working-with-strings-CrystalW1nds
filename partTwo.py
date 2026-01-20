import math  

def main():
    A = int(input("Enter one side: "))
    B = int(input("Enter the other side: "))
    pythag(A, B)

def pythag(A,B):
    hypotenuse = math.hypot(float(A),float(B))
    print(hypotenuse)


main()
