# app/Dockerfile

# 如果有新增套件
# docker build --no-cache -t streamlit-maps:0.2 .

# 如果只是更新程式碼
# docker build -t streamlit-maps:0.2 .
# 
# docker run -p 8502:8502 --rm --name stream-maps -v .\:/app/workspace streamlit-maps:0.2 bash

FROM python:3.11-slim

WORKDIR /app

EXPOSE 8502

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# 將您的程式碼複製到容器內
COPY . .

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8502", "--server.address=0.0.0.0"]