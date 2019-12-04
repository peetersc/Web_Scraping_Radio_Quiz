APPLICATION_NAME = "Ham Radio Quiz"
NAVIGATION = "License Classifications"

HOME = "Home"
TECHNICIAN = "Technician"
GENERAL = "General"
EXTRA = "Amateur Extra"

TECH_QUESTIONS = [line.strip() for line in open("data/tech2018Questions.txt", 'r')]
TECH_ANSWERS = [line.strip() for line in open("data/tech2018Answers.txt", 'r')]
TECH_CORRECT_ANSWERS = [line.strip() for line in open("data/tech2018CorrectAnswers.txt", 'r')]

GEN_QUESTIONS = [line.strip() for line in open("data/general2019Questions.txt", 'r')]
GEN_ANSWERS = [line.strip() for line in open("data/general2019Answers.txt", 'r')]
GEN_CORRECT_ANSWERS = [line.strip() for line in open("data/general2019CorrectAnswers.txt", 'r')]

EXTRA_QUESTIONS = [line.strip() for line in open("data/extra2016Questions.txt", 'r')]
EXTRA_ANSWERS = [line.strip() for line in open("data/extra2016Answers.txt", 'r')]
EXTRA_CORRECT_ANSWERS = [line.strip() for line in open("data/extra2016CorrectAnswers.txt", 'r')]




