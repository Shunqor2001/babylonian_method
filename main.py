num=int(input("s"))
num2=int(input("d"))

def main(S, d):
    a=(S-d**2)/2*d
    b=a+d
    x=b-(a**2)/b


    return x
print(main(num,num2))