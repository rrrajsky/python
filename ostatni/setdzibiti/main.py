import openai
openai.api_key = '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'
messages = [ {"role": "system", "content":
"You are a intelligent assistant."} ]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})