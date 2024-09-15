
#dictonary holds the type of food I ate for each meal and the cost 
#the food is the key and the value is the cost of the meal 

cost_dict = { "eggs" :2 
            ,"banana": 2
            ,"salad": 10
            ,"steak and rice":30 }

#this is a function that calculates the meal cost , I define the function
#by using def and the name calculate_meal_cost

def calculate_meal_cost():
    cost_dict_values = sum(cost_dict.values())
    print(f"Your total cost for your meals are: ${cost_dict_values}")
    
calculate_meal_cost()



#breakfast_cost = 1.00 + 2.00

#lunch_cost = 10.00

#dinner_cost = 30.00

#print(breakfast_cost + lunch_cost + dinner_cost)