#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) - Since a grows at n**2 and the while loop runs at n**3 (n**3 - n**2 = n)

b)  O(nlogn) - Grows faster than O(n) with two loops, but slower than O(n**2) since j doubles on inside loop

c)  O(n) - Since recursive call runs n/2, but drop the 1/2 constant to get n

## Exercise II

1)  Start at the top floor n (e.g. 100)
2)  Perform a binary search
    if egg breaks at 1/2 * n, search 1 to (1/2n - 1) (e.g 50, binary search 1-49)
    else egg does not break, search (1/2n + 1) to n
3)  Repeat

O(logn)

More efficient method:

1) Start at floor 1
2) For i in range 1 to n, next floor is 2**i (e.g 2,4,8,etc.)
3) Continue until egg breaks (i steps)
4) Perform binary search of smaller space (2**(i-1)) to (2**(i)) (e.g 4-8)

O(2logi)
