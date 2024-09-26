

time_put_turkey_in_oven = int(input("What time should we put the turkey in the oven?: ")) #8pm
time_in_oven = int(input("How long do you want the turkey to cook for?: ")) #14 hrs
change_military_to_standard = int(time_put_turkey_in_oven + time_in_oven - 12)
time_take_turkey_out = 10

def turkey_time():
        if (time_put_turkey_in_oven == 8):
                print("Put turkey in oven.")
        elif(change_military_to_standard < time_take_turkey_out):
                print("Turkey is not ready yet")
                
        while(change_military_to_standard == time_take_turkey_out):
                print('Take turkey out')
                break
        
turkey_time()