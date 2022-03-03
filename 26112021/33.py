#Generate Fibonacci series of N terms
N = int(input("Enter the Nit:"))
if N == 1 or N >= 1:
    s1 = 0
    s2 = 1
    print(s1)
if N == 2 or N >= 2:
    print(s2)
if N > 2:
    N2 = N-2
    for i in range(N2):
        s3 = s1+s2
        s1 = s2
        s2 = s3
        print(s3)