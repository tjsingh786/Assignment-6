#Q.1
def sphere(radius):
    area=4*3.14*radius*radius
    print(area)

radius=int(input('Enter Radius:'))
sphere(radius)

#Q.2

def perfect(num):
    sum=0
    i=1
    while i<num:
        if(num%i==0):
            sum=sum+i
        i+=1
        
    if num!=1 and sum==num:
         print (num)
         
print('The Perfect Numbers are:')
for i in range (1,1000):
    perfect(i)

#Q.3
def multiplication():
    n=int(input('Enter integer:'))
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

multiplication()
    
#Q.4
def exponent(base,exp):
    
    if(exp==1):
        return base
    else:
        return base*exponent(base,exp-1)
base=int(input("Enter base: "))
exp=int(input("Enter exponential number: "))
a=exponent(base,exp)
print(a)
