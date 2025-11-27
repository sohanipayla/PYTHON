# Write a “pager” program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing  each time 
# to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to close the file.

def pager_program():
    file = open("Text.txt", "r")
    lines= 0
    while True:
        line = file.readline()
        if not line: #file is finish
            print("\nEnd of file reached.")
            break
        print(line, end='')
        lines += 1

        # Pause every 25 lines
        if lines % 25 == 0:
            user_input = input("\nEnter 'continue' to see next 25 lines or 'stop' to exit: ").lower()
            if user_input == "stop":
                print("Exiting pager...")
                break
    file.close()
pager_program()