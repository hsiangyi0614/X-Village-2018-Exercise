#exercise2: recursive_2
def fib(n):
    if n == 0 or n == 1:
        return int(n)
    else:
        return fib(n-1) + fib(n-2)

number = int(input('Please type an integer: '))
print("1 到 ",number, "的過程")
for i in range(1,number):
    print("F(",i,") : ",fib(i))
print("結果")
print("F(",number,") : ",fib(number))