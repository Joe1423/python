from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Enter q at anytime to quit.\n')

while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    my_survey.store_response(response)

#answers

my_survey.show_results()