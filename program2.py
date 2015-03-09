first = 1
second = 2
limit = 4000000

fibs = [ 1 ]

while second < limit :
    tmp = second
    second = first + second
    first = tmp
    fibs.append( first )

# for fib in fibs :
#     print fib

indexs = [i for i in range(0 , len(fibs)) if fibs[i] %2 == 0 ]
even_fibs = [fibs[i] for i  in indexs]

print sum(even_fibs)
