#Ques 4 
print("Answer 4\n")
                                              # Function that returns true if the word is found
def isWordPresent(sentence, word):
     
                                           # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
 
                                         # Comparing the current word
                                 # with the word to be searched
        if (i == word):
            return True
    return False

B = input('Enter the sentence/string -\n')
word ='name'
if word in B:
    print('\nYes\n')
    print("The word 'name' is present in the entered string.")
else:
    print('\nNo\n')
    print("The word 'name' is not present in the entered string.")


