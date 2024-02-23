import openai
def gpt3(text, OPENAI_API_KEY):
    openai.api_key = OPENAI_API_KEY

    model = "gpt-3.5-turbo"

    query = f"질문: {text}"

    # 메시지 설정하기
    messages = [{
        "role": "system",
        "content": "너는 아이에게 동화를 읽어주고 있어. 아이의 질문에 100자 이하로 간결하게 대답해줘."
    }, {
        "role": "user",
        "content": query
    }]
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']

