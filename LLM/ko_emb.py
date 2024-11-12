from sentence_transformers import Sentence_Transformer
import numpy as np

model = Sentence_Transformer('intfloat/multilingual-e5-large')

sentences = [
    "참새는 짹짹하고 웁니다.",
    "LangChain과 Faiss를 활용한 예시입니다.",
    "자연어 처리를 위한 임베딩 모델 사용법을 배워봅시다.",
    "유사한 문장을 검색하는 방법을 살펴보겠습니다.",
    "강좌를 수강하시는 수강생 여러분 감사합니다!"
]

embeddings = model.encode(sentences)

print(embeddings.shape)
print(embeddings[0])
