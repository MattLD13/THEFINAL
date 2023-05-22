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
	pickedQuestions = []
	choices = []
	fileExists = True
	isChoice = False

	welcome_message()
	fileName = get_initial_input()
	questionsDict = read_file(fileName)
	if(questionsDict == {}):
		print("Sorry, the file \"" + fileName + "\" does not exist.")
		fileExists = False
		questionAmt = 10

	while(questionAmt < 10):
		print("Question " + str(questionAmt + 1) + ":")

		chosenQuestion = pick_random(questionsDict, pickedQuestions, isChoice)

		pickedQuestions.append(chosenQuestion)

		print("after" + str(pickedQuestions))

		choices = pick_choices(chosenQuestion, questionsDict)

		question = create_question(chosenQuestion, choices)
		print(question)

		chosenAnswer = get_question_input()
		if(chosenAnswer == 0):
			print("Please enter a valid choice (A, B, C, or D).")
			print()
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
			return 0

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

def pick_random(questionDict, pickedQuestions, isChoice):
	isLooping = True

	while(isLooping):
		randomNumber = random.randint(0, len(questionDict) - 1)
		
		if(isChoice):
			randomChoice = list(questionDict.values())[randomNumber]

			print("Random Value: " + randomChoice)
		else:
			randomChoice = list(questionDict.keys())[randomNumber]
			print("Random Key: " + randomChoice)

		if(randomChoice not in pickedQuestions):
			isLooping = False

	print("Picked Questions: " + str(pickedQuestions))
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