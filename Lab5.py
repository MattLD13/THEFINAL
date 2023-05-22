# Matt Dicks
# Programming - Period 04
# Unit 6
# Quizlet CLI Basically

#IMPORTS
import random

# Main function
def main():

	questionAmt = 0
	score = 0
	pickedChoices = {}
	choices = {}
	fileExists = True

	welcome_message()
	fileName = get_initial_input()
	questionsDict = read_file(fileName)
	if(questionsDict == {}):
		print("Sorry, the file \"" + fileName + "\" does not exist.")
		fileExists = False
		questionAmt = 10

	while(questionAmt < 10):
		print("Question " + str(questionAmt + 1) + ":")
			
		#print(questionsDict)

		chosenQuestion, pickedChoices  = pick_question(questionsDict, pickedChoices)

		choices = pick_choices(chosenQuestion, questionsDict, pickedChoices)

		question = create_question(chosenQuestion, choices)
		print(question)

		chosenAnswer = get_question_input()

		isCorrect = check_answer(chosenAnswer, choices, questionsDict, chosenQuestion)
		
		if(isCorrect):
			print("Correct!")
			score += 1
		else:
			print("No, the correct answer is " + questionsDict[chosenQuestion] + ".")

		print()
		questionAmt += 1
	if(fileExists): 
		print("Score: " + str(score) + " / " + str(questionAmt))

def welcome_message():
	print("Welcome to the Quiz Game!")
	print("This game can be used to quiz yourself on different types of facts.")
	print("You will be shown up to 10 question.   For every correct answer, you \nwill get 1 point. Good luck!")
	print()

def get_initial_input():
	fileName = input("Enter the name of the fact file: ")
	print()
	return fileName

def get_question_input():

	isLooping = True
	while isLooping:
		usrInput = input("Enter Choice: ")
		try:
			usrInput = str(usrInput)
		except:
			print("Please enter a valid choice (A, B, C, or D).")
		usrInput = usrInput.upper()
		if(usrInput == "A" or usrInput == "B" or usrInput == "C" or usrInput == "D"):
			isLooping = False
			chosenAnswer = ord(usrInput)
			return chosenAnswer
		else:
			print("Please enter a valid choice (A, B, C, or D).")

def read_file(fileName):
	if file_exists(fileName):
		fo = open(fileName, "r")
		questionsFile = fo.read()
		fo.close()
		questionDict = create_dict(questionsFile)
	else:
		questionDict = {}
	return questionDict

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

def pick_random(length):
	chosenNumber = random.randint(0, length - 1)
	return chosenNumber

def pick_question(questionDict, pickedChoices):
	isLooping = True
	while isLooping:
		chosenNumber = pick_random(len(questionDict))
		chosenQuestion = list(questionDict.keys())[chosenNumber]
		if(chosenQuestion not in pickedChoices):
			isLooping = False

	pickedChoices[chosenQuestion] = questionDict[chosenQuestion]
	return chosenQuestion, pickedChoices

def pick_choices(chosenQuestion, questionsDict, pickedChoices):
	choices = {}
	# pick 3 random choices
	for i in range(3):
		randomNum = pick_random(len(questionsDict))
		# if the random number chosen is the same as the chosen question, pick again
		while(randomNum == chosenQuestion):
			randomNum = pick_random(len(questionsDict))
		# if the choice has already been picked, pick again
		while(questionsDict[list(questionsDict.keys())[randomNum]] in choices.values()):
			randomNum = pick_random(len(questionsDict))

		# add the choice to the choices dictionary
		choices[list(questionsDict.keys())[randomNum]] = questionsDict[list(questionsDict.keys())[randomNum]]

	# add the chosen question to the choices dictionary
	choices[chosenQuestion] = questionsDict[chosenQuestion]

	# convert the dictionary to a list so it can be shuffled
	choices = list(choices.items())

	# shuffle the list
	for num in range(len(choices) - 1, 0, -1):
		randNum = random.randint(0, num)
		choices[num], choices[randNum] = choices[randNum], choices[num]

	# convert the list back to a dictionary
	choices = dict(choices)

	print(choices)
	return choices

def create_question(chosenQuestion, choices):
	
	question = chosenQuestion + "\n" + "A. " + choices[list(choices.keys())[0]] + "\n" + "B. " + choices[list(choices.keys())[1]] + "\n" + "C. " + choices[list(choices.keys())[2]] + "\n" + "D. " + choices[list(choices.keys())[3]] + "\n"

	return question

def check_answer(chosenAnswer, choices, questionsDict, chosenQuestion):
	if(chosenAnswer == ord("A")):
		chosenAnswer = list(choices.keys())[0]
	elif(chosenAnswer == ord("B")):
		chosenAnswer = list(choices.keys())[1]
	elif(chosenAnswer == ord("C")):
		chosenAnswer = list(choices.keys())[2]
	elif(chosenAnswer == ord("D")):
		chosenAnswer = list(choices.keys())[3]

	if(chosenAnswer == chosenQuestion):
		isCorrect = True
	else:
		isCorrect = False

	return isCorrect

#Calling Main
main()