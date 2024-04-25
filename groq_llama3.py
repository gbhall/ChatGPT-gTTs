import sys
import os
from openai import OpenAI

# Function that generates a ChatGPT response for a given prompt
def generate_chatgpt_response(prompt):
    client = OpenAI(
        base_url="https://api.groq.com/openai" + "/v1/",  # replace with your endpoint url
        api_key=os.getenv('GROQ_API_KEY')  # replace with your token
    )

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
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
    if response.choices and response.choices[0].message:
        message = response.choices[0].message.content
        print(message)
    else:
        print('Failed to generate a response from the Groq endpoint.')
        create_cute_voice("I'm having trouble connecting to the Groq endpoint.")
