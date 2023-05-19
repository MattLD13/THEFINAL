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


	welcome_message()
	fileName = get_initial_input()

	while(questionAmt < 1):
		questionsDict = read_file(fileName)
		#print(questionsDict)

		chosenQuestion, pickedChoices = pick_random_question(questionsDict, pickedChoices)


		choices = pick_choices(chosenQuestion, questionsDict, pickedChoices)
		print("answer: ", sep = "")
		print(pickedChoices)
		print()
		print("choices: " , sep = "")
		print(choices)


		#question = create_question(chosenQuestion, choices)
		#print(question)

		#chosenAnswer = get_question_input()
		#print(chosenAnswer)

		#isCorrect = check_answer(answerNumber, chosenAnswer)
		
		#if(isCorrect):
			#print("Correct!")
			#score += 1
		#else:
		#	print("No, the correct answer is " + answer + ".")

		#print()
		questionAmt += 1
	#print("Score: " + str(score) + " / " + str(questionAmt))

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
		return questionDict
	else:
		print("Sorry, the file \'" + fileName + "\' does not exist.")

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








def pick_random_question(questionsDict, pickedChoices):
	isLooping = True
	while isLooping:
		chosenQuestion = random.choice(list(questionsDict.keys()))
		if(chosenQuestion not in pickedChoices):
			isLooping = False
			pickedChoices[chosenQuestion] = questionsDict[chosenQuestion]
	
	return chosenQuestion, pickedChoices

def pick_choices(chosenQuestion, questionsDict, pickedChoices):
	choices = {}

	choices[chosenQuestion] = questionsDict[chosenQuestion]

	for idx in range(0,3):

		chosenItem, pickedChoices = pick_random_question(questionsDict, choices)

		choices[chosenItem] = questionsDict[chosenItem]


	return choices






def create_question(chosenQuestion, choices):
	question = chosenQuestion + "\n" + "A." + choices[0] + "\nB." + choices[1] + "\nC." + choices[2] + "\nD." + choices[3]

	return question

def check_answer(answerNumber, chosenAnswer):
	isCorrect = False

	answerNumAscii = 0
	if(answerNumber == 0):
		answerNumAscii = 65
	elif(answerNumber == 1):
		answerNumAscii = 66
	elif(answerNumber == 2):
		answerNumAscii = 67
	elif(answerNumber == 3):
		answerNumAscii = 68

	if(answerNumAscii == chosenAnswer):
		isCorrect = True

	return isCorrect


main()