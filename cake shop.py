total_quantity_of_cake = int(input("total quantity of cake: "))
total_quantity_of_bread = int(input("total quantity of bread: "))

cost_price_of_the_cake = int(input("cost price of the cake: "))
cost_price_of_the_bread = int(input("cost price of the bread: "))


employe=2
employe_salary=2*100

total_cost_price= (total_quantity_of_cake*cost_price_of_the_cake) + (total_quantity_of_bread*cost_price_of_the_bread)
print("total cost price :",total_cost_price)

selling_price_of_cake = int(input("selling price of the cake:"))
selling_price_of_bread = int(input("selling price of the bread:"))

total_selling_price = 0

n=10 #assign the customer value

#i assign a for loop to iterate through every customer one by one
for i in range(1,n):

#using an if condition to check the quantity of cake and bread is not 0 
   # if(total_quantity_of_cake>=0 or total_quantity_of_bread>=0):

#after customer enter into the shop employee asking the customer whether the customer want cake or bread
        print("employee")
        print("do you want cake or bread:")

#let the customer to choose what he/she wants?
        choice = input("cake or bread or both:")

#if the customer wants only cake it goes through this statement
        if(choice=="cake"):
#checking the cake is available or not
            if(total_quantity_of_cake > 0):
                cake = int(input("how many cakes do you want: "))                             
                total_selling_price = total_selling_price + (cake*selling_price_of_cake)      
                total_quantity_of_cake = total_quantity_of_cake - cake                        
                print("cakes available: ",total_quantity_of_cake)                             

##if the customer wants only bread it goes through this statement
        elif(choice=="bread"):

#checking the bread is available or not
            if(total_quantity_of_bread > 0):                       
                bread = int(input("how many bread do you want: "))                             
                total_selling_price = total_selling_price + (bread*selling_price_of_bread)     
                total_quantity_of_bread = total_quantity_of_bread - bread                      
                print("bread available: ",total_quantity_of_bread)                             
                

#if some customer want both cake and bread it goes through this statement
        elif(choice=="both"):
            if(total_quantity_of_cake>0 and total_quantity_of_bread>0):                        
                cake = int(input("how many cakes do you want: "))                        
                bread = int(input("how many bread do you want: "))    
                

#calculating the total selling price of cake and bread and store it in the assigned variable
                total_selling_price = total_selling_price + (cake*selling_price_of_cake) + (bread*selling_price_of_bread)
                total_quantity_of_cake = total_quantity_of_cake - cake                                   
                total_quantity_of_bread = total_quantity_of_bread - bread                      
                print("cakes available: ",total_quantity_of_cake)                            
                print("bread available: ",total_quantity_of_bread)          

#if some customer wants other sweet items it goes through else statement
        else:
            print("item is not available")

#this else is used for stop the customer when products are sold out
else:
    print("sold out of products")
    
    
#giving salary to the employees from the selling price and print the total selling price
total_selling_price = total_selling_price - employe_salary
print("total_selling_price:",total_selling_price)

#printing the total cost price for the bakery per day
#print("total_cost_price:",total_cost_price)

selling_price= total_selling_price - total_cost_price
if(selling_price>total_cost_price):
    print("profit")

else:
    print("loss:")

        