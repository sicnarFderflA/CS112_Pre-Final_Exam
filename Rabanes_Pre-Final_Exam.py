print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM"
      "\nCreated by: Francis Alfred R. Rabanes"
      "\n"
      "\nProblem: Create python program that displays all prime numbers within a range:"
      "\n"
      "\nRULES TO CONSIDER:"
      '\n[1] If number (start) is a negative number. The program will prompt a message “Enter a non-negative number.”'
      '\n[2] If number (end) is less than number (start). The program will prompt a message “Enter a number greater than number (start).”'
      '\n[3] Lastly, if the user enter the number “0”, the program will terminate.'
      "\n"
      "\n"
      )
 
while True:
    start = float(input("Enter a number [start]: "))
    if start < 0:
        print("Enter a non-negative number.")
        continue
    elif start == 0:
        print("Program Terminated.")
        break
    elif not start.is_integer():
        print("Enter an integer number only.")
        continue
    
    while True:
        end = float(input("Enter a number [end]: "))
        if end < 0:
            print("Enter a non-negative number.")
        elif end == 0:
            print("Program Terminated.")
            break
        elif end <= start:
            print(f"Enter a number greater than {start}."
                  "\n")
            continue
        elif not end.is_integer():
            print("Enter an integer number only.")
            continue

        start = int(start)
        end = int(end)
        result = ""
        if start == 1:
            for i in range(2, end+1):
                if i % 2 != 0:
                    result += str(i) + " "
        else:
            for i in range(start, end+1):
                if i % 2 != 0:
                    result += str(i) + " "


        print(f"The Prime numbers between {start} and {end} is {result}"
              '\n')
        break
    if end == 0:
        break
