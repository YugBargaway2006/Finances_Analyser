def amount_input(prompt):
    allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    val = input(prompt)
    if(val == ""):
        return -1
    
    n = len(val)
    for i in range(n):
        counter = 0
        for j in allowed:
            if(val[i] == j):
                break
            else:
                counter += 1
         
        if(counter == 10):
            print("\nInvalid Input :-(")
            print("Enter Again \n")
            return amount_input(prompt)
        
    return int(val)


def date_input(prompt):
    allowed = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    val = input(prompt)
    if(val == ""):
        return val
    
    if(val[2] != '/' or val[5] != '/'):
        print("\nInvalid Input :-(")
        print("Enter Again \n")
        return date_input(prompt)
    
    for i in range(8):
        counter = 0
        for j in allowed:
            if(val[i] == j):
                break
            else:
                counter += 1
        
        if(counter == 10):
            print("\nInvalid Input :-(")
            print("Enter Again \n")
            return date_input(prompt)
        
    return val


def check_input(allowed, prompt):
    val = input(prompt)
    
    # Check input
    for i in allowed:
        if(val == i):
            if(val == "y"):
                return "Y"
            elif(val == "n"):
                return "N"
            
            return val
    
    print("\nInvalid Input :-(")
    print("Enter again\n")
    return check_input(allowed, prompt)
    