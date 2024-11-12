# 5-3 대화형 챗봇
from openai import OpenAI

client = OpenAI()

system_message = {
    "role":"system", "content":"너는 환영인사를하는 인공지능이야, 영어로 말하고 한국어로 다시 말해줘"
}

messages = [system_message]

while True:
    user_input = input("사용자 전달:")
    if user_input == "exit":
        print("대답: 즐거운 대화였어요.")
        break

    messages.append({"role":"user", "content":user_input})
    completion = client.chat.completions.create(
    model = "gpt-4",
            messages = messages
    )

    reply = completion.choices[0].message.content
    print("대답: " + reply)
    messages.append({"role":"assistant","content":reply})
