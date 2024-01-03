def get_user_input(question):
    answer = input(question + " (Enter a number from 1 to 5, where 1 is strongly disagree and 5 is strongly agree): ")
    return int(answer)

def assess_personality(answers):
    total_score = sum(answers)
    
    if total_score < 10:
        return "Introverted"
    elif 10 <= total_score <= 20:
        return "Ambivert"
    else:
        return "Extroverted"

def main():
    print("Welcome to the Personality Assessment!")

    questions = [
        "I enjoy socializing with large groups of people.",
        "I prefer spending time alone rather than in social situations.",
        "I am often the life of the party.",
        "I feel comfortable in new and unfamiliar environments.",
        "I enjoy deep and meaningful conversations."
    ]

    user_answers = []

    for question in questions:
        answer = get_user_input(question)
        user_answers.append(answer)

    personality_type = assess_personality(user_answers)

    print("\nBased on your answers, your personality type is:", personality_type)

if __name__ == "__main__":
    main()