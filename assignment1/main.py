# Assignment 1.1
name = input("Enter your name: ")
for i in range(3):
    print(name)


# Assignment 2.1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(a + b + c)


# Assignment 2.2
a = input("Enter first string: ")
b = input("Enter second string: ")
c = input("Enter third string: ")
print(a + b + c)


# Assignment 4.1
for i in range(1, 11):
    print(7, "*", i, "=", 7 * i)

for i in range(1, 11):
    print(9, "*", i, "=", 9 * i)


# Assignment 4.2
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)


# Assignment 4.3
n = int(input("Enter a number: "))
s = 0
for i in range(1, n + 1):
    s = s + i
print(s)


# Assignment 5.1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(max(a, b, c))


# Assignment 5.2
n = int(input("Enter a number: "))
s = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        s = s + i
print(s)


# Assignment 5.3
n = int(input("Enter a number: "))
s = 0

for x in range(2, n + 1):
    f = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            f = 1
            break
    if f == 0:
        s = s + x

print(s)
# Assignment 6.1
def Add_two_nums(a,b):
          c=a+b
          return c
	
print Add_two_nums(4,9)

#Assignment 6.2
def IsPrime(a):
	for i in range (2,n//2+1):
		if n%i==0:
				return true
		
