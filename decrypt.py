# lassoLetter('A', 3) = 'D'

# Define a function to find the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code to the letterCode variable
    letterCode = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter 'a'
    aAscii = ord('a')

    # The number of letters in the alphabet
    alphabetSize = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)

    # Convert the ASCII number to the character or letter
    decodedLetter = chr(trueLetterCode)

    # Send the decoded letter back
    return decodedLetter


# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
def lassoWord( word, shiftAmount ):

    # This variable is updated each time another letter is decoded
    decodedWord = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lassoLetter() function is invoked with each letter and the shift amount
        # The result (decoded letter) is stored in a variable called decodedLetter
        decodedLetter = lassoLetter(letter, shiftAmount)

        # The decodedLetter value is added to the end of the decodedWord value
        decodedWord = decodedWord + decodedLetter

    # The decodedWord is sent back to the line of code that invoked this function
    return decodedWord

# print(lassoLetter('Z', 3))

letterCode = ord('W'.lower())
print(letterCode)

decodedLetterCode = letterCode + 13
print(decodedLetterCode)

decodedLetter = chr(decodedLetterCode)
print(decodedLetter) 

 
#Mod operator
#To wrap around the alphabet the easy way, you need a special operator called mod, 
#which is the percent sign (%).

#The mod operator divides two numbers and returns the remainder. If you run the 
#following code in Python to set three variables by using mod:

threeTwo = 3 % 2
elevenFour = 11 % 4 
fiveTen = 5 % 10

print(threeTwo)
print(elevenFour)
print(fiveTen)




# Example 1: Letter 'a' and shift by 2
aAscii = ord('a')
alphabetSize = 26
letter = 'a'
shiftAmount = 2
print(aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize))

# Example 2: Letter 'W' and shift by 13
aAscii = ord('a')
alphabetSize = 26
letter = 'W'
shiftAmount = 13
print(aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize))


print(lassoLetter('y', 3))
print("Shifting terra by 13 gives: \n" + lassoWord('terra', 13))

print('WHY : 13 gives: ' + lassoWord('WHY', 13))
print('oskza : -18 gives: ' + lassoWord('oskza', -18))
print('ohupo : -1 gives: ' + lassoWord('ohupo', -1))
print('ED : 25 gives: ' + lassoWord('ED', 25))

print('p : -2 gives: ' + lassoWord('p', -2))
