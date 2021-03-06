"""

Question 4

Develop a program to perform the following task:
1. Define a function to check whether a number is happy or not.
2. Define a function to print all happy numbers within a range
3. Define a function to print first N happy numbers
"""

#function to check whether happy or sad
def happy(n):
  for i in range(1,101):
    sum=0
    while n!=0:
        digit=n%10                 #digit-each extracted digits stored
        square=digit**2                         
        n=n//10                         
        sum=sum+square                         
    n=sum                         
  return (sum)

#function to print the happy number within range
def happynumber(l,u):               #l-lowerlimit  u-upperlimit
  count=0
  for i in range(l+1,u):
    s=happy(i)                      #invoke happy() function
    if s==1:
      print(i,end=" ")
      count=1                       #count to check whether there is happy number in the range
  print()
  if count==0:                      
    print("There is no happy numbers between this range.")

#Function to print 'n' number of happy numbers
def printnumbers(n):
   count=1                          #count- to check the number of happy numbers printed
   i=1
   while count<=n:
     total=happy(i)                 #invoke happy function
     if total==1:                   #total- condition variable
        print(i,end=" ")
        count+=1
     i=i+1
   print('') 

#function to invoke all above mentioned functions 
def main():
  print("\t HAPPY NUMBER FUNCTIONS")
  print("\tA number is Happy or Sad")
  num=int(input("Enter the number to check:"))
  if happy(num)==1:
    print("Its a Happy number.")
  else:
    print("Its a Sad number.")
  print("\tHappy numbers within a range.")
  lowerlimit=int(input("Enter the Lower limit:"))
  upperlimit=int(input("Enter the Upper limit:"))
  happynumber(lowerlimit,upperlimit)   
  print("\tFirst N happy numbers") 
  N=int(input("Enter the number of terms:"))
  printnumbers(N)                   #N-number of terms to print

main()                              #function invokation