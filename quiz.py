def run_quiz():
    questions = [
        {
            "question": "What is the capital of Inda?",
            "answer": "Delhi"
        },
        {
            "question": "What is 2 + 2?",
            "answer": "4"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "Mars"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")

    for q_data in questions:
        question_text = q_data["question"]
        correct_answer = q_data["answer"].lower()  

        user_answer = input(f"\n{question_text} ").lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q_data['answer']}")

    print(f"\nQuiz completed! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    run_quiz()
