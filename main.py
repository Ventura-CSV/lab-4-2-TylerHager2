def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    
    for x in range(5):
        x = int(input("Enter a number: "))
        total += x
        
    print ('Here is your total:',total)
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
