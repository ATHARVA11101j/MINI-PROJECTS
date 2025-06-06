import openai

openai.api_key = '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'

def chat():
    print("Welcome to the ChatGPT CLI Bot! Type 'exit' to quit.")
    messages = []

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

messages.append({"role":"user","content":user_input}) 

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
            )
    reply = response['choices'][0]['message']['content']
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat()