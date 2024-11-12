# 5-3 일회용 챗봇
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",  # 모델 이름을 올바르게 지정합니다.
    messages=[  # messages로 변경
        {"role": "system", "content": "너는 나에게 한국의 연예인인 노홍철처럼 말을 하는 인공지능이야"},
        {"role": "user", "content": "안녕하세요. 팬이에요."}
    ]
)

# 응답 내용 출력
print("대답: " + completion.choices[0].message.content)
