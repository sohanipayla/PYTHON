# Write a function count_lines() to count and display the total number of lines from the file. Consider the following lines for 

def count_lines():
    with open("friends.txt", "r") as file:
        lines = file.readlines()
        print("Total number of lines:", len(lines))

count_lines()


# SECOND-METHOD

# def count_lines():
#     with open("friends.txt", "w+") as file:
#         file.write("Friends are crazy, Friends are naughty !\n")
#         file.write("Friends are honest, Friends are best !\n")
#         file.write("Friends are like keygen, friends are like license key !\n")
#         file.write("We are nothing without friends, Life is not possible without friends !\n")
#         file.seek(0) mob=ve cursor to start before reding
#         lines = file.readlines()
#         print("Total number of lines:", len(lines))
# count_lines()