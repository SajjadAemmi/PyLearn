import openai
import os

# Store the API key in an environment variable
os.environ["OPENAI_API_KEY"] = "sk-FAn8arvYqLisvbUwlyGT3BlbkFJi"

# Use the API key to authenticate
openai.api_key = os.environ ["OPENAI_API_KEY"]

# Define a flag to control the loop
keep_prompting = True

while keep_prompting:
    # Get the prompt from the user
    prompt = input( 'What is your question? (Type exit if Done) ')
    if prompt == 'exit':
        keep_prompting = False
    else:
        # Generate text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200
        )

        # Print the generated text
        print(response["choices"][0]["text"])