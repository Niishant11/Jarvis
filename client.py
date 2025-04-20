from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)