#define the function that takes two lists
    # frequency_dict = {
    #     list1 : ['1', '2', '3', '4'],
    #     list2: ['4', '3', '2', '1']
    # }
def has_same_digit_frequency(list1, list2):
    frequency_dict = {
    }
 
    for num in list1:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
        #     return True
        #     print(True)
        # else:
        #     return False
        #     print(False)
    #create an if statement that compares the two lists
    # if num in range(int(list1)) == num in range(int(list2)):
    #     return True
    # else:
    #     return False
#call the function with the two lists 
list1 = [1, 2, 3, 4, 5, 6, 4, 4]
list2 = [4, 3, 2, 1]

has_same_digit_frequency(list1, list2)


