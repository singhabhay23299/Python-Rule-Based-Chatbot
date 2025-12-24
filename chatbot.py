def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you?"

    elif "job" in user_input:
        return "I can help you with job roles, skills, and career guidance."

    elif "python" in user_input:
        return "Python is widely used in data analysis, automation, web development, and AI."

    elif "skills" in user_input:
        return "In-demand skills include Python, SQL, Power BI, JavaScript, and React."

    elif "resume" in user_input:
        return "Focus on projects, internships, and relevant technical skills."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Best of luck for your career."

    else:
        return "Sorry, I didn't understand that. Please try again."


print("Chatbot: Hello! Type 'bye' or 'exit' to stop.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
