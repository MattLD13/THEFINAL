# Matt Dicks
# Programming - Period 04
# Unit 6
# Quizlet CLI Basically

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
	isChoice = False

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

	# while loop to only play 10 questions
	while(questionAmt < 10):
		goodInput = False

		# pick a random question using the pick_random
		chosenQuestion = pick_random(questionsDict, pickedQuestions, isChoice)

		# add the chosen question to the pickedQuestions list
		pickedQuestions.append(chosenQuestion)

		# pick 3 random choices and 1 correct choice using pick_choices
		choices = pick_choices(chosenQuestion, questionsDict)

		# create the question using create_question
		question = create_question(chosenQuestion, choices)

		while(goodInput == False):
			print(question)

			# get the user's answer using get_question_input
			chosenAnswer, goodInput = get_question_input()

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
			print("No, the correct answer is " + questionsDict[chosenQuestion] + ".")

		print()
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
		questionDict = create_dict(questionsFile)

	# if the file does not exist, create an empty dictionary
	else:
		questionDict = {}

	# return the dictionary
	return questionDict


# get the question and choices and return them as a ascii value
def get_question_input():
	goodInput = False

	chosenAnswer = input("Enter Choice: ")

	try:
		chosenAnswer = str(chosenAnswer)
		fixedAnswer = chosenAnswer.upper()

		asciiAnswer = ord(fixedAnswer)

		if(asciiAnswer >= 65 and asciiAnswer <= 68):
			goodInput = True
	except:
		goodInput = False

	return asciiAnswer, goodInput


def file_exists(fileName):
	try:
		open(fileName, "r")
		doesExist = True
	except:
		doesExist = False

	return doesExist

def create_dict(questions):
	questionDict = {}
	questions = questions.split("\n")
	for question in questions:
		question = question.split(":")
		questionDict[question[0]] = question[1]
	return questionDict

def pick_random(questionDict, pickedQuestions, isChoice):
	isLooping = True

	while(isLooping):
		randomNumber = random.randint(0, len(questionDict) - 1)
		
		if(isChoice):
			randomChoice = list(questionDict.values())[randomNumber]

		else:
			randomChoice = list(questionDict.keys())[randomNumber]

		if(randomChoice not in pickedQuestions):
			isLooping = False

	return randomChoice

def pick_choices(chosenQuestion, questionsDict):
	choices = []
	isLooping = True
	isChoice = True

	# pick 3 random choices
	while(isLooping):
		randomChoice = pick_random(questionsDict, choices, isChoice)
		if(randomChoice != questionsDict[chosenQuestion]):
			choices.append(randomChoice)
		if(len(choices) == 3):
			isLooping = False

	randomChoice = random.randint(0, 3)
	choices.insert(randomChoice, questionsDict[chosenQuestion])

	return choices

def create_question(chosenQuestion, choices):

	question = chosenQuestion + "\n" + "A. " + choices[0] + "\n" + "B. " + choices[1] + "\n" + "C. " + choices[2] + "\n" + "D. " + choices[3]

	return question

def check_answer(chosenAnswer, choices, questionsDict, chosenQuestion):
	usrAnswer = ""

	if(chosenAnswer == ord("A")):
		usrAnswer = choices[0]
	elif(chosenAnswer == ord("B")):
		usrAnswer = choices[1]
	elif(chosenAnswer == ord("C")):
		usrAnswer = choices[2]
	elif(chosenAnswer == ord("D")):
		usrAnswer = choices[3]

	if(usrAnswer == questionsDict[chosenQuestion]):
		isCorrect = True
	else:
		isCorrect = False

	return isCorrect

#Calling Main
main()