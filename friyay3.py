#define the function where a string passes through
def count(string):
    #create empty dictionary
    char_dict = {}
    #for loop for every character in the sting
    for letter in string:
        if letter in char_dict:
            char_dict[letter] += 1

        else:
            char_dict[letter] = 1
    print(char_dict)
# count('aabbbbcc')







#anagram exercise

def anagram(string, string2):
#sort the strings alphabetically check if theyre equal to each other
    if sorted(string) == sorted(string2):
        print(True)
    else:
        print(False)
anagram('desserts', 'stressed')


