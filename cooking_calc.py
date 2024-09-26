
turkey_cooking_time = 14 

ham_cooking_time = 5

#defines a function called cooking and has two parameters which are elements that you can pick so it repeatbale for different values 
def cooking_end_time(start_time, duration):
    return ( start_time + duration) % 24

#return works because when we call the function we print it out 

print(f"Take the turkey out of the oven at {cooking_end_time(15,turkey_cooking_time)}")
print(f"Take the ham out of the oven at {cooking_end_time(13,ham_cooking_time)}")

#call the function within a print function that uses an f string to create a printed output to the console , the defined parameters are given