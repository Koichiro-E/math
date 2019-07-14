def pri(x):
    i = 2
    while i * 2 <= x:
        #print(i)
        if x % i == 0:
            #print('{}素数ではない'.format(n))
            break
        i += 1
    else:
        print(x)

def fib(n): #N個までのフィボナッチ数をfib_listに収納する。
    fib_list = []
    a = b = c = 1
    while c <= n:
        fib_list.append(a)
        pri(a)
        fib_list.append(b)
        pri(b)
        a += b
        b += a
        c +=2
    if n % 2 != 0:
        fib_list.pop(-1)

    n -= 1
    print(fib_list)
fib(int(input('何個目までのフィボナッチ素数を探しますか？')))
