from openai import OpenAI   #this is just for checking that api is working or not

client = OpenAI(
    api_key="key",
)
completion = client.chat.completions.create( 
 model="gpt-5-nano", 
 messages=[ 
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"}, 
    {"role": "user", "content": "what is coding"} 
    ]
 )
print(completion.choices[0].message.content)



