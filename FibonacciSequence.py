def fibseq(n):
    x = 0
    y = 1
    for i in range(n/3):
            z = x+y
            x = z+y
            y = z+x
    if n == 0:
        y = 0
    print y

fibseq(input("Which digit of the Fibonacci Sequence interests you? "))
