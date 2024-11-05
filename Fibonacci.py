class Vijay:
    def __init__(self,n):
        self.n=n
    def fibonacci(self):
        a=0
        b=1
        if self.n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,self.n):
                c=a+b
                a=b
                b=c
                print(c)
def main():
    n=int(input("Enter the number n : "))
    vijays=Vijay(n)
    vijays.fibonacci()

if __name__ == "__main__":
    main()
