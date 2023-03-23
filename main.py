
sign = '$'
maximum = 16;

print("Enter N, the length of the horizontal diagonal of the diamond, according to the conditions below.")
print(" Condition1: ( N must be a odd. )")
print(" Condition2: ({0} < N < {1})\n".format(0,maximum))
N = int(input("N : "))
print()

if (N <= 0 or N >= maximum):
    print("Condition 1 was violated.")
elif N % 2 == 0:
    print("Condition 2 was violated.")
else:
    print("Generates diamonds..")
    print()
    for i in range(N):
        for j in range(N):
            if i + j == N // 2 or i - j == N // 2 or j - i == N // 2 or i + j == N // 2 * 3:
                print("*", end="")
            else:
                print(" ", end="")
        print()
