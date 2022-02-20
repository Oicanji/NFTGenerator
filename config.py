import os

from cv2 import multiply

sufix_to_reference_obj = 'waifus'
sufix_project = 'WaifusCreator'
sufix_collection = 'AnimeFacesWeirdo'

#this var is used to system khow if generate a background or not
enable_background = True
#if so generate a background transparent

#Size in pixels of the draw
size_width = 86
size_height = 86

has_resize = True

#resize in porcentage
resize_width = 3.520
resize_height = 3.520

#instead porcent, this is parent variable, learn more in patterns.py
instead_percentage = 40

#use names custom or not
use_custom_names = False
#the custom name has filliar attr to be used in reference also image
#the name complete after attr special
#_$... to use in reference file
#_@... to use in reference folder
# others names can appear on any drawing, randomly

#use names desative, so system will use names similiar of children of Elon Musk

#this is system to cached images
#enabled if you full context for all images gerated
#per default is false
#but context works only in collection
context_all = False

#variable set difficulity of re use part
multiply_difficulty = 90
#recomend to use max 100
#this if use to generate a random number of 0 to 100
#and programmer less 5 after fustration tentative

#variables to use in all codes
#to clear screen, if you want
#no clear screen, if you dont want
clear = lambda: os.system('cls')