from openai import OpenAI

client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create( 
 model="gpt-5-nano", 
 messages=[ 
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"}, 
    {"role": "user", "content": "what is coding"} 
    ]
 )
print(completion.choices[0].message.content)


