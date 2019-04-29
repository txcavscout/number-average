# Function to import numbers until a non number is entered. Averages numbers in list and rounds.

def get_nums():
    list = []
    keep_adding = True
    while keep_adding == True:
        try:
            list_in = int(input('Enter number to add to list, enter q to quit: '))
            list.append(list_in)
        except ValueError:
            val = int(list_in)
            average = sum(list) / len(list)
            average = int(round(average, 0))
            print(f'\nYour list to average is: {list}\nThe average is: {average}\n')
            return

#start = get_nums()
