#searching
#sorting

#Problem 1

#input 
user_input = [1,2,3,4,5,6,7,8,9,10]

#Q ; Checxk to see if a certain number exist in the user input arry
n = 10
# Liner Search
result = False
for e in user_input :
    if e == n :
        result = True

if result == True :
    print ('Found')
else:
    print ('Not Found')
   
# if else , for loop, print , calculation (+, -)