# Question 1: Print First 10 natural numbers using while loop. Expected

x=0
while x<10:
    print(x)
    x+=1


# Question 2: Print the following pattern. Expected

x=1
while x<=5:
    for i in range(1,x):
        print(i,end=' ')
    print('')
    x+=1
print('')


# Question 3: Accept number from user and calculate the sum of all number between 1 and given number.

num = int(input('Enter Number: '))

sum = 0

for i in range(num+1):
    sum+=i

print(sum)
print('')

# Question 4: Print multiplication table of given number.

num2 = int(input('Enter Number: '))

for i in range(1,11):
    print(i*num2)
print('')

# Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number
# greater than 150 stop the loop iteration.

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if i%5==0 and i <=150:
        print(i)
print('')

# Question 6: Given a number count the total number of digits in a number.

num3 = 75869
numString = str(num3)

print(len(numString))
print('')

# Question 7: Print the following pattern using for loop.


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print('')
print('')

# Question 8: Reverse the following list using for loop

list = [10, 20, 30, 40, 50]

for i in range(len(list)-1,-1,-1):
    print(list[i])
print('')

# Question 9: Display a message “Done” after successful execution of for loop.

for i in range(2):
    print(i)
else:
    print("Done!")
print('')

# Question 10: Display Fibonacci series up to 10 terms.

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)

for i in range(10):
    print(F(i),end=' ')

print('')

# Question 11: Write a loop to find the factorial of any number.

num = int(input('Enter Number: '))

fac = 1

for i in range(1, num + 1):
    fac = fac * i

print(fac)
print('')

# Question 12: Python program to display all the prime numbers within a range

start = 25
end = 40

for num in range(start, end + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

