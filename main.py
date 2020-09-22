# Reading an excel file
import csv

# max coins in each game
max_DictatorGame = 100
max_BanditGame = 100
max_CommonsDillemaGame = 40
max_PublicGoodDillemaGame = 40

# expected behavior (by Nash Equilibrium)
expectedDictatorGame = 50
# In Bandit Game We look on the complementary
expectedBanditGame = 50

# save the real behavior
pleaseWork = 0
count_particpents = 0
regressionTwo = 0
regressionMulti = 0
nash = 0

# sum errors
error_reg_two = 0
error_reg_multi = 0
error_desison = 0
error_nash = 0

# Decision table results
with open(r"decision.table.predicted.csv", newline='') as csvfile:
    reader_result = csv.DictReader(csvfile)
    for row_result in reader_result:
        error_desison = error_desison + abs((float(row_result['actual'])) - (float(row_result['predicted'])))
        if abs((float(row_result['actual'])) - (float(row_result['predicted']))) <= 20:
            pleaseWork = pleaseWork + 1

# Read the file row by row
with open(r"exp2.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        count_particpents = count_particpents + 1
        if count_particpents < 230:
            # Dictator Game
            real_behavior_Dictator = row['DG.CHOICE']

            # Bandit Game
            real_behavior_Bandit = row['BG.CHOICE.R']

            # Commons Dillema Game Game
            real_behavior_commons_dillema_game = row['CDG.CHOICE.R']
    
            # Public Good Dillema Game
            real_behavior_public_good_dillema_game = row['PGDG.CHOICE']

            # Deviation from Nash - it's mean that he will took the same behavior
            if abs(int(real_behavior_Bandit) - int(real_behavior_Dictator)) < 20:
                nash = nash + 1
            error_nash = error_nash + abs(int(real_behavior_Bandit) - int(real_behavior_Dictator))

            # Linear Regression Model with all the games
            regDG = 0.5297 * float(real_behavior_public_good_dillema_game) + 0.3358 * float(real_behavior_Bandit) + 10.5767
            # check how much
            if abs(regDG - int(real_behavior_Dictator)) < 20:
                regressionTwo = regressionTwo + 1
            error_reg_multi = error_reg_multi + abs(regDG - int(real_behavior_Dictator))

            # Linear Regression Model with only bandit game
            regDG = 0.4085 * float(real_behavior_Bandit) + 20.994
            if abs(regDG - int(real_behavior_Dictator)) < 20:
                regressionMulti = regressionMulti + 1
            error_reg_two = error_reg_two + abs(regDG - int(real_behavior_Dictator))

print("Result of deviation from Nash Model with all the games: ")
print("Number of participants that the model predict good in range of -+20 is " + str(nash))
print("Number of participants that the model predict bad in range of -+20 is " + str(229 - nash))
print("Error sum is " + str(error_nash))

print("Result Linear Regression Model with all the games: ")
print("Number of participants that the model predict good in range of -+20 is " + str(regressionMulti))
print("Number of participants that the model predict bad in range of -+20 is " + str(229 - regressionMulti))
print("Error sum is " + str(error_reg_multi))

print("Result Linear Regression Model with only bandit game: ")
print("Number of participants that the model predict good in range of -+20 is " + str(regressionTwo))
print("Number of participants that the model predict bad in range of -+20 is " + str(229 - regressionTwo))
print("Error sum is " + str(error_reg_two))


print("Decision table results: ")
print("Number of participants that the model predict good in range of -+20 is " + str(pleaseWork))
print("Number of participants that the model predict bad in range of -+20 is " + str(229 - pleaseWork))
print("Error sum is " + str(error_desison))
