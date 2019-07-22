names = ["aaron", "john", "christine", "maggie", "dopa", "faker"]

for name in names:
    if name.startswith("a"):
        print(name)

#TODO 是要更加有好的返回说明，还是在default中默认一种零值返回代表一种状况

numbers = list(range(1,100))
for number in numbers:
    #  是的， 这里不是 || 或者 &&  是 or 和and
    if (number % 3 ==0) or number % 50 ==0 :
        print(number)
    elif number % 5 ==0 and number % 7 ==0:
        print(number)

# 这里使用in 和 not in 来做判断。。。。
print(5 in numbers)
print(10000 not in numbers)

# 素数筛
def sieve_of_eratosthenes(n):#埃拉托色尼筛选法，返回少于n的素数
    primes = [True] * (n+1)#范围0到n的列表
    p = 2#这是最小的素数
    while p * p <= n:#一直筛到sqrt(n)就行了
        if primes[p]:#如果没被筛，一定是素数
            for i in range(p * 2, n + 1, p):#筛掉它的倍数即可
                primes[i] = False
        p += 1
    primes = [element for element in range(2, n) if primes[element]]#得到所有少于n的素数
    return primes
print(sieve_of_eratosthenes(100))


# 列表为空时返回false 一个以上的元素返回true
names = []
if names:
    print("not empty")
else:
    print("empty")