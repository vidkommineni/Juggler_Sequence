
#Prompts the user to enter a value
num = int(input("Enter a positive integer:"))

#keeps track of the number of iterations
count = 0
#The final string to print all the numbers
sequence = ''

#Checking to see if the val is one itself
if(num == 1):
    sequence += str(num)
else:
    sequence = str(num) + ", "
    
print(f"The Juggler sequence starting at {num} is:")

#ONly runs for vals that are not 1
while num != 1:
    #Updating the number od iterations
   count += 1
   # print("INSIDE while")
   #checking to see if num is an even number
   if num % 2 == 0:
       num = int(num**(1/2))
       #adds it directly to the list of it becomes one. No comma at the end
       if(num == 1):
           sequence += str(num)
        #Since the new num is not 1, will add a comma at the end
       else:
           sequence += str(num) +', '
    #checking to see if odd
   elif num%2 != 0:
       num = int(num**(3/2))
       #will add directly w no comma at end
       if(num == 1):
           sequence += str(num)
       else:
           #comma at end bc the value of num is not 1 so more will be added.
           sequence +=str(num) + ', '
'''      
   if num == 1:
       num = int(num**(1/2))
       sequence += str(num)
   elif num == 1:
       num = int(num**(3/2))
       sequence += str(num)
   '''

print(sequence)
print(f"It took {count} iterations to reach {num}")








