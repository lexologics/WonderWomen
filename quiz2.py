# create some variables for scoring
diana_like = 0
steve_like = 0
max_like = 0
barbara_like = 0

# update scoring variables based on the weapon choice
if activity == "A":
    diana_like = diana_like + 1
    barbara_like = barbara_like + 1
else:
    max_like = max_like + 1
    steve_like = steve_like + 1

# update scoring variables based on the job choice
if job == "A":
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
    steve_like = steve_like - 1
else:
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diana_like = diana_like - 1
    max_like = max_like + 2
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 2
    barbara_like = barbara_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    steve_like = steve_like + 2
    diana_like = diana_like + 1
else:
    max_like = max_like + 1
    barbara_like = barbara_like + 2

# update scoring variables based on the travel choice
if travel == "A":
    max_like = max_like + 2
    barbara_like = barbara_like - 1
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 1

# print the results depending on the score
if diana_like >= 6:
    print( "You're most like Wonder Woman!" )
elif steve_like >= 6:
    print( "You're most like Steve Trevor!" )
elif barbara_like >= 6:
    print( "You're most like Barbara Minerva!")
else:
    print( "You're most like Max Lord!")