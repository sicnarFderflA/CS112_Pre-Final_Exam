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
    check1 = True
    if start < 0:
        print("Enter a non-negative number.")
        check1 = False
        continue
    elif start == 0:
        print("Program Terminated.")
        check1 = False
        break
    elif not start.is_integer():
        print("Enter an integer number only.")
        check1 = False
        continue

    while True:
        end = float(input("Enter a number [end]: "))
        check2 = True
        if end < 0:
            print("Enter a non-negative number.")
            check2 = False
            continue
        elif end == 0:
            print("Program Terminated.")
            check2 = False
            break
        elif end <= start:
            print(f"Enter a number greater than {start}."
                  "\n")
            check2 = False
            continue
        elif not end.is_integer():
            print("Enter an integer number only.")
            check2 = False
            continue
        
        start = int(start)
        end = int(end)
        result = ""
        if start <= 2 <= end: #include 2 if its in the range
            result += "2 " # since 2 % 2 = 0 therefore the code will make 2 as not a prime number.
        if start == 1: 
            for i in range(2, end+1): # 1 is a special number so we skip it
                if i % 2 != 0: # checks if the number is uneven. p.s not all uneven numbers are prime but prime numbers except for 2 are uneven.
                    result += str(i) + " "
        else:
            for i in range(start, end+1): 
                if i % 2 != 0:
                    result += str(i) + " "

        if check1 and check2 == True:
            print(f"The Prime numbers between {start} and {end} is {result}"
                '\n')
            break
    if end == 0:
        break
