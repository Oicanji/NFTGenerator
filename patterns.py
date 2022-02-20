#create "rarity" to for and only non-vital things 

#if you put a "linked" one, it will link by instances files with the same name in different folders 
#"linked" = instead ... let the user or algorithm decide
#"linked" = closed ...  links the linked files with a rule within the system and the link name
#"linked" = color ... is similar to closed but the colors are not linked

#"parent" = parent to the linked files
#you must instantiate "parent" after the "linked", because it will be used to link the files
#don't complicate things, don't forget the "parent" please my friend

# The link is unnecessary if you have instantiated it so there is no need to instance twice you idiot 
#that is
#if you have already linked this pattern, do not need to link again... please 

hairinbackground = {'name': 'hair-in-background', 'linked': 'closed', 'parent':'hair-in-face'}
face = {'name': 'face'}
bushes = {'rarity': 60, 'name': 'bushes'}
skinmark = {'rarity': 10, 'name': 'skinmark'}
noise = {'name': 'noise'}
mouth = {'name': 'mouth'}
eyebrow = {'rarity': 98, 'name': 'eyebrow'}
eyes = {'name': 'eyes'}
hairinface = {'name': 'hair-in-face'}
upperhead = {'rarity': 30, 'name': 'upper-head'}
#rarity to 100% is max

#add all patterns to list
patterns = [hairinbackground, face, bushes, skinmark, noise, mouth, eyebrow, eyes, hairinface, upperhead]