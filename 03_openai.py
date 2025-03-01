import openai
import os

# Store your API key securely in an environment variable
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your new API key

# Initialize OpenAI client securely
client = openai.OpenAI()

command='''
Copied Text: [2:02 PM, 2/10/2025] 💫: CN week 3 assignment Answers:-
1. A
2. B
3. D
4. C
5. B
6. B
7. A
8. A
9. C
10. D
[2:40 PM, 2/10/2025] 💫: 10 ka C
[11:54 PM, 2/10/2025] 💫: hy
[11:54 PM, 2/10/2025] 💫: kal py ja raha hai presentation hai bhaii
[6:17 AM, 2/11/2025] Kushagra 3B1: Umeed toh nahi hai
'''
# Make a request
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Person name Jay who speaks hindi , gujarati as well as english . He is from India and is a coder. You analyzed chat history and respond like jay "},
        {"role": "user", "content": command}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)