def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')




import unittest

class NamesTestCase(unittest.TestCase): 
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        print("test1")
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        print("test2")
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')







class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    def show_question(self):
         """Show the survey question."""
         print(question)
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        if self.responses is None:
            print("No one responded yet")
        else:
            for response in self.responses:
                print('- ' + response)
####################### Don't forget to use self.responses. Otherwise NameError, responses is not defined. 


#from survey import AnonymousSurvey
# Define a question, and make a survey.

question = 'What language did you first learn to speak?'
#responses = ""
my_survey = AnonymousSurvey(question)
# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
###Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()




### Test the AnoymousSurvey
##### When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_.
### each method has to start with test_
### avoid method overloading by differnt naming
class TestAnonmyousSurvey(unittest.TestCase): 
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly.""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English')
        print("test3")
        self.assertIn('English', my_survey.responses)


    def test_store_three_responses(self):
            """Test that three individual responses are stored properly."""
            question = "What language did you first learn to speak?"
            my_survey = AnonymousSurvey(question)
            responses = ['English', 'Spanish', 'Mandarin']
            for response in responses:
                my_survey.store_response(response)
            for response in responses:
                print("test4")
                self.assertIn(response, my_survey.responses)

    
  
    def test_store_single_response_with_setup(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        print("Test5")
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses_with_setup(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            print("Test6")
            self.assertIn(response, self.my_survey.responses)




###the setUp() Method

### When you include a setUp() method in a TestCase class, 
### Python runs the setUp() method before running each method starting with test_. 
### Any objects created in the setUp() method are then available in each test method you write.


unittest.main()












