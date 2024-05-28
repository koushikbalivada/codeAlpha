def chat():
  print("Chatbot: Hello! I am your chatbot.")
  print("Chatbot: Feel free to ask anything. Type 'bye' to exit.")
  while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
      print("Chatbot: I enjoyed talking with you! Bye!")
      break
    else:
      response = respond(user_input)
      print("Chatbot:", response)

def respond(user_input):
  greetings = ["hello", "hi"]
  if any(greeting in user_input for greeting in greetings):
    return "Hi, how are you?"
  elif "how are you" in user_input:
    return "I'm doing great!"
  elif "open" in user_input:
    return "Sorry, I don't have permissions for that task."
  elif "bye" in user_input:
    return "Bye! Have a good day!"
  else:
    return "Sorry, I didn't understand."

if __name__ == "__main__":
  chat()
