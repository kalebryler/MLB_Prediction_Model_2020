########## ########## ########## ########## ########## ########## ########## ########## ########## ##########

###################
##### IMPORTS #####
###################

########## ########## ########## ########## ##########

### IMPORT / EXPORT ###
import sys
import os

### PATHS ###
path = os.path.dirname(os.path.dirname(__file__))
root_path = path.split('MLB Model')[0]

sys.path.append(root_path + '/MLB Model/Momentum Model/Code')
sys.path.append(root_path + '/MLB Model/Comparison Model/Code')
sys.path.append(root_path + '/MLB Model/Zone Model/Code')
sys.path.append(root_path + '/MLB Model/Miscellaneous')

### MODEL FILES ###
import Momentum_Update
import Comparison_Update
import Zone_Update
import Player_Database

########## ########## ########## ########## ##########

###########################
##### PLAYER DATABASE #####
###########################

########## ########## ########## ########## ##########

### UPDATE PLAYER DATABASE ###

# Player_Database.write_Player_Database()

########## ########## ########## ########## ##########

##########################
##### MOMENTUM MODEL #####
##########################

########## ########## ########## ########## ##########

### UPDATE MOMENTUM DATA ###

# Momentum_Update.update_Momentum_Model()

########## ########## ########## ########## ##########

############################
##### COMPARISON MODEL #####
############################

########## ########## ########## ########## ##########

### UPDATE MATCHUP DATA ###

Comparison_Update.update_Comparison_Model_Matchup_Data()


### UPDATE PLAYER COMPARISON DATABASES ###

# Comparison_Update.update_Comparison_Model_Player_Comparisons()

########## ########## ########## ########## ##########

##########################
##### MOMENTUM MODEL #####
##########################

########## ########## ########## ########## ##########

### UPDATE ZONE MODEL DATA ###

# Zone_Update.update_Zone_Model()

########## ########## ########## ########## ##########










########## ########## ########## ########## ########## ########## ########## ########## ########## ##########
