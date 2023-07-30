import openai
while "q" in user:
    user = input("This is nural artificial intelligent: ")
    openai.api_key = "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"
    responce = openai.Completion.create(model = "text-davinci-003" , prompt = user , max_tokens = 2048 , stop = None , temperature = 0.5)
    print(responce.choices[0].text) 