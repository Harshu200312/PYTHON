def quiz():
    # Define the questions, options, and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Charles Dickens"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
            "answer": "A"
        }
    ]

    # Initialize the score
    score = 0

    # Loop through each question
    for q in questions:
        print(q["question"])  # Print the question
        for option in q["options"]:  # Print the options
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()  # Get the user's answer and convert to uppercase

        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!")
            score += 1  # Increase the score if the answer is correct
        else:
            print("Wrong! The correct answer is " + q["answer"])

        print()  # Print a newline for better readability

    # Print the final score
    print("Your final score is " + str(score) + " out of " + str(len(questions)) + ".")

# Call the quiz function to start the quiz
quiz()
