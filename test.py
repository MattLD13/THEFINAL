def main():
	
	questionDict = read_file("states.txt")

	#print the 1st in the dictionary
	print(list(questionDict.keys())[41])

def read_file(fileName):

	fo = open(fileName, "r")
	questionsFile = fo.read()
	fo.close()
	questionDict = create_dict(questionsFile)
	return questionDict

def create_dict(questions):
	questionDict = {}
	questions = questions.split("\n")
	for question in questions:
		question = question.split(":")
		questionDict[question[0]] = question[1]
	return questionDict

main()