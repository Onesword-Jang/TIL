import os

# 현재 작업 디렉토리 확인
print("Current Working Directory:", os.getcwd())

# .env 파일 존재 여부 확인
if os.path.exists(".env"):
    print(".env 파일이 존재합니다.")
else:
    print(".env 파일이 존재하지 않습니다.")
