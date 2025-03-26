import random  # Importing the random module to shuffle the questions

def quiz():
    # List of dictionary objects, each containing a question, multiple-choice options, and the correct answer
    questions = [
        {"question": "What is the output of print(2 * 3)?", "options": ["5", "6", "23", "None"], "answer": "6"},
        {"question": "Which data type is used to store a sequence of characters?", "options": ["int", "float", "str", "bool"], "answer": "str"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["def", "func", "define", "lambda"], "answer": "def"},
        {"question": "What will be the output of print(5 // 2)?", "options": ["2.5", "2", "3", "None"], "answer": "2"},
        {"question": "Which of the following is a valid variable name in Python?", "options": ["2var", "_var", "var-name", "None"], "answer": "_var"}
    ]
    
    random.shuffle(questions)  # Shuffle the order of questions for randomness
    score = 0  # Variable to keep track of the user's score
    
    for q in questions:
        print(q["question"])  # Display the question
        
        # Display the available answer choices
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        
        # Get the user's input and convert it to an integer index
        answer = input("Enter the number of your answer: ")
        
        # Check if the selected answer is correct
        if q["options"][int(answer) - 1] == q["answer"]:
            print("Correct!\n")
            score += 1  # Increment score if the answer is correct
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    # Display the final score after all questions are answered
    print(f"Your final score is {score}/{len(questions)}")

# This ensures that the quiz function runs only when the script is executed directly
if __name__ == "__main__":
    quiz()


