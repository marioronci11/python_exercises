#Create a program that prints out letters using a specified character, in this case, the '#' character. 
#The letters to be displayed are 'C', 'O', 'D', and 'E' - to print out the word CODE as below:

hash_tag_1 = "####"

hash_tag_2 = "#"

hash_tag_3 = " #   #"

hash_tag_4 = "###"

hash_tag_5 = " #    #"

hash_tag_6 = "#####"




#prints letter c
print(f" {hash_tag_1}")
for hash in range(3):
        print(hash_tag_2)
print(f" {hash_tag_1}")


#prints letter o
print(f"  \n {hash_tag_1}")
for hash in range(3):
        print(hash_tag_3)
print(f"  {hash_tag_1}")


#prints letter d
print(f"  \n {hash_tag_4}")
print(f"{hash_tag_3}")
print(f"{hash_tag_5}")
print(f"{hash_tag_3}")
print(f" {hash_tag_4}")



#prints letter e
print(f"  \n {hash_tag_6}")
print(hash_tag_2)
print(f" {hash_tag_6}")
print(hash_tag_2)
print(f" {hash_tag_6}")



#def print_c_letter():
    #print("")
    #for hash in range(3):
        #four_line_c = "".join(hash_tag)
        #print(f"{four_line_c}", end=" ")
    #for hash in range(4):
        #print(hash_tag)
    #for hash in range(4):
        #four_line_c = "".join(hash_tag)
        #print(f"{four_line_c}", end=" ")
  
    

#print_c_letter()

 #def print_o_letter():
#     for hash in range(3):
#         print("".join(hash_tag), end = "")
#     for hash in range(4):
#         print(hash_tag)
#     for hash in range(4):
#         print("".join(hash_tag), end = "")

# def print_d_letter():
#     for hash in range(3):
#         print("".join(hash_tag), end = "")
#     for hash in range(4):
#         print(hash_tag)
#     for hash in range(4):
#         print("".join(hash_tag), end = "")

# def print_e_letter():
#     for hash in range(3):
#         print("".join(hash_tag), end = "")
#     for hash in range(4):
#         print(hash_tag)
#     for hash in range(4):
#         print("".join(hash_tag), end = "")

# print_c_letter()
# print_o_letter()
# print_d_letter()
# print_e_letter()