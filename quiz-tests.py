# this is a comment that won't be interpreted as a command

# use a variable named year to "remember" the value 1984
year = 1984

# print a message to see what year it is
print( f"The year is {year}..." )

year = year + 36
print( f"The year is {year}...\n" )

year = 1984

# if we're in 1984
if year == 1984:
    print( "I left you a message on your answering machine!\n" )
# if we're in 2020
if year == 2020:
    print( "I left you a voicemail!\n" )

# ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n" )

# print out which activity they chose
print( f"You chose {activity}.\n")    

# if they chose reading a book
if activity == "A":
    print( "Nice choice!\n" )
elif activity == 'B':
    print( "Let's Party!!!\n")
else:
    print( 'Not an option.\n' )

