from openai import OpenAI
import os
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
GPT_API_KEY = os.environ['GPT_API_KEY']
client = OpenAI(api_key=GPT_API_KEY)
def create_response(sex, age, request_message):
    print("text create start")
    print(f"Your content: 나는 {sex}이고 {age}이야, {request_message}, 100자 이내로 대답해줘!")
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": f"나는 {sex}이고 {age}이야, {request_message}, 100자 이내로 대답해줘!"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message.content