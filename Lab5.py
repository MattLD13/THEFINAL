# Matt Dicks
# Programming - Period 04
# Unit 6
# Quizlet CLI Basically

# Honor Code - I have neither given nor received unauthorized aid on this assignment

# Difficulties - I had many difficulties while writing this program. The issue that haunted me throughout this project was abstraction
#				 in the pick_random function. I have re-written this function 8 times at this point. I started off with a seperate 
#				 pick_question function but realized that was not the correct design. I then re-wrote it with pick_random having special
#				 cases for picking choices or questions. Eventually I settled on my current design which is abstracted and able to work for
#				 both without any changes. This was after going back to the drawing board and redoing a design specifically for the
#				 pick_random function. I had it make a key and then in pick_choices it changes it to a value but becuase it is a key
#				 it is a be to be tested easily.

#IMPORTS
import random

# Main function
def main():

	# define variables
	questionAmt = 0
	score = 0
	pickedQuestions = []
	choices = []
	fileExists = True
	questionsToPlay = 10

	# print the welcome message
	welcome_message()

	# get the file name
	fileName = get_initial_input()

	# read the file and create a dictionary
	questionsDict = read_file(fileName)

	# if the dictionary
	if(questionsDict == {}):
		
		# if the file doesn't exist, print an error message
		print("Sorry, the file \"" + fileName + "\" does not exist.")

		# set the fileExists variable to false
		fileExists = False

		# set the question value to 10 to not start the quiz
		questionAmt = 10

	# if the file has less than 10 questions change the amount of questions to play to the amount of questions in the file
	if(len(questionsDict) < 10):
		questionsToPlay = len(questionsDict)


	# while loop to only play 10 questions or the amount of questions in the file
	while(questionAmt < questionsToPlay):

		# assume that input is bad
		goodInput = False

		# pick a random question using the pick_random
		chosenQuestion = pick_random(questionsDict, pickedQuestions)

		chosenKey = list(questionsDict.keys())[list(questionsDict.values()).index(chosenQuestion)]

		# add the chosen question to the pickedQuestions list
		pickedQuestions.append(chosenQuestion)

		# pick 3 random choices and 1 correct choice using pick_choices
		choices = pick_choices(chosenQuestion, questionsDict)

		# create the question using create_question
		question = create_question(chosenKey, choices)

		# while the input is bad repeat this code
		while(goodInput == False):

			# print the question
			print(question)

			# get the user's answer using get_question_input
			chosenAnswer, goodInput = get_question_input()

			# if the input is bad, print input is invalid
			if(goodInput == False):
				print("Please enter a valid answer (A, B, C, or D).")
				print()

		# check if the answer is correct using check_answer
		isCorrect = check_answer(chosenAnswer, choices, questionsDict, chosenQuestion)
		
		# if the answer is correct, print "Correct!" and add 1 to the score
		if(isCorrect):
			print("Correct!")
			score += 1

		# if the answer is incorrect, prints the correct answer
		else:
			print("No, the correct answer is" + chosenQuestion + ".")

		#line break becuase i like formatting
		print()

		# add 1 to the questionAmt
		questionAmt += 1

	# print the score
	if(fileExists): 
		print("Score: " + str(score) + " / " + str(questionAmt))

# welcome_message function that prints the welcome message
def welcome_message():

	# print the welcome message
	print("Welcome to the Quiz Game!")
	print("This game can be used to quiz yourself on different types of facts.")
	print("You will be shown up to 10 question.   For every correct answer, you \nwill get 1 point. Good luck!")
	print()

# gets the file name from the user
def get_initial_input():

	# get the file name from the user
	fileName = input("Enter the name of the fact file: ")
	print()

	# return the file name
	return fileName

# check if the file exists and read it
def read_file(fileName):

	# if the file exists, read it and create a dictionary
	if file_exists(fileName):

		# open the file and read it
		fo = open(fileName, "r")

		# read the file into a string
		questionsFile = fo.read()

		# close the file
		fo.close()

		# create a dictionary from the string using create_dict
		questionsDict = create_dict(questionsFile)

	# if the file does not exist, create an empty dictionary
	else:
		questionsDict = {}

	# return the dictionary
	return questionsDict

# check if the file exists
def file_exists(fileName):

	# try to open the file
	try:
		open(fileName, "r")

		# if the file opens, set doesExist to True
		doesExist = True

	# if the file does not open, set doesExist to False
	except:
		doesExist = False

	# return doesExist
	return doesExist

# create a dictionary from the string
def create_dict(questions):

	# create an empty dictionary
	questionsDict = {}

	# split the string into a list of questions
	questions = questions.split("\n")

	# loop through the list of questions
	for question in questions:

		# split the question into the question and the answer
		question = question.split(":")

		# if the question is not empty, add it to the dictionary
		questionsDict[question[0]] = question[1]

	# return the dictionary
	return questionsDict

# pick a random question
def pick_random(questionsDict, pickedQuestions):
	isLooping = True

	# while loop to pick a random question
	while(isLooping):

		# pick a random number between 0 and the length of the dictionary -1
		randomNumber = random.randint(0, len(questionsDict) - 1)
		
		# change the number to a value
		randomChoice = list(questionsDict.values())[randomNumber]

		# if the random choice is not in the pickedQuestions list, set isLooping to False
		if(randomChoice not in pickedQuestions):
			isLooping = False

	# return the random choice
	return randomChoice

# pick choices for the question
def pick_choices(chosenQuestion, questionsDict):
	choices = []
	isLooping = True

	# pick 3 random choices
	while(isLooping):

		# pick a random choice using pick_random
		randomChoice = pick_random(questionsDict, choices)

		#change the output from pick_random to a value instead of a key

		# if the random choice is not the correct answer, add it to the choices list
		if(randomChoice != chosenQuestion):

			# add the random choice to the choices list
			choices.append(randomChoice)

		# if the choices list has 3 choices, stop the loop
		if(len(choices) == 3):
			isLooping = False

	# pick a random number between 0 and 3
	answerPlacement = random.randint(0, 3)

	# insert the correct answer at a random index in the choices list
	choices.insert(answerPlacement, chosenQuestion)

	# return the choices list
	return choices

# create the question
def create_question(chosenKey, choices):

	# create the question string using string concatenation
	question = chosenKey + "\n" + "A. " + choices[0] + "\n" + "B. " + choices[1] + "\n" + "C. " + choices[2] + "\n" + "D. " + choices[3]

	# return the question
	return question

# get the question and choices and return them as a ascii value
def get_question_input():
	goodInput = False
	asciiAnswer = 0

	# get input
	chosenAnswer = input("Enter Choice: ")

	# check if input is valid
	try:

		# convert input to string
		chosenAnswer = str(chosenAnswer)

		# convert input to uppercase
		fixedAnswer = chosenAnswer.upper()

		# convert input to ascii
		asciiAnswer = ord(fixedAnswer)

		# check if input is a valid choice
		if(asciiAnswer >= 65 and asciiAnswer <= 68):
			goodInput = True

	# if input is invalid, set goodInput to False
	except:
		goodInput = False

	# return the ascii value and if the input was valid
	return asciiAnswer, goodInput

# check if the answer is correct
def check_answer(chosenAnswer, choices, questionsDict, chosenQuestion):
	chrAnswer = ""

	# convert the ascii value to a character
	chrAnswer = chr(chosenAnswer)

	# convert the character to the corresponding choice
	#if it is A
	if(chrAnswer == "A"):

		# convert to choice 1
		chrAnswer = choices[0]

	# if it is B
	elif(chrAnswer == "B"):

		# convert to choice 2
		chrAnswer = choices[1]

	# if it is C
	elif(chrAnswer == "C"):

		# convert to choice 3
		chrAnswer = choices[2]

	# if it is D
	elif(chrAnswer == "D"):

		# convert to choice 4
		chrAnswer = choices[3]

	# check if the answer is correct
	if(chrAnswer == chosenQuestion):

		# if the answer is correct, set isCorrect to True
		isCorrect = True

	# if the answer is incorrect, set isCorrect to False
	else:
		isCorrect = False

	# return isCorrect
	return isCorrect

#Calling Main
main()