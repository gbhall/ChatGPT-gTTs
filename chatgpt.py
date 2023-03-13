import sys
import openai

# Function that generates a ChatGPT response for a given prompt
def generate_chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion

# Function that gets the user input
def get_user_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Enter the text: ")

# Driver code
if __name__ == '__main__':
    prompt = get_user_input()
    response = generate_chatgpt_response(prompt)
    if response['choices'] and response['choices'][0]['message']:
        message = response['choices'][0]['message']['content']
        print(message)
    else:
        print('Failed to generate a response from ChatGPT API.')
        create_cute_voice("I'm having trouble connecting to the ChatGPT API.")
