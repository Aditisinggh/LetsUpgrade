n = 1042000

#Storing cubes of digits so that they need not be calculated again and again
pow_3={i:i**3 for i in range(1,10)}


while(n<=702648265):
    num,rev = n,0

    #Removing all 0's from the numbers, as it will not have any effect on the sum
    num = int(str(num).replace('0',''))
    
    #Calculating armstrong property 
    while(num!=0):
        rem = num%10
        rev += pow_3[rem]
        num//=10
    if(rev==n):
        print("The first armstrong number is:",n)
        break
    n+=1
