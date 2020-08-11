#-----------------------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment 05, managing a CD inventory.
# Change Log: (Who, When, What)
# Jurg Huerlimann 2020-Aug-07, Created File from CDInventory_Starter.py script.
# Jurg Huerlimann 2020-Aug-08 Changed functionality to use dictonary
# Jurg Huerlimann 2020-Aug-09 Added functionality to load existing data from file
# Jurg Huerlimann 2020-Aug-10 Added functionality to delete info from inventory
# Jurg Huerlimann 2020-Aug-11 Added functionality to save inventory to file
#-----------------------------------------------------------------------------#

# Declared variables
strChoice = ''  # User input
lstTbl = []     # list of lists to hold data
dicRow = {}     #list of data row
strFileName = 'CDInventory.txt'  # Name of data file
objFile = None  # file object

# Get user Input, display menu options
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':   # Exit the program if the user chooses so
        break
    
    if strChoice == 'l':   # load inventory from file
        lstTbl.clear()
        objFile = open(strFileName, 'r')  # open CDInventory.txt file
        for row in objFile:               # read row by row and add to dictionary
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()

        print('The inventory has been loaded, please use [i] to display it .')
        print()
#    break    

    
    elif strChoice == 'a':  # add CD info through questions and add to dictionary
        strID = input('Enter an ID: ') 
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':   # Display the current inventory from in-memory
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            
    elif strChoice == 'd': # functionality of deleting an entry
        delEntry = int(input('What line would you like to delete? PLease enter the ID number: '))
        for entry in range(len(lstTbl)):
            if lstTbl[entry]['id'] == delEntry:
                del lstTbl[entry]
                print('Your entry has been deleted from inventory.')
                print()
                break     
    
    elif strChoice == 's':  # Save the data to a text file CDInventory.txt 
        objFile = open(strFileName, 'w')  # using w rewrites the content of the file
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','                
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

