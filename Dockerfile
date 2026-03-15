FROM python:3.11

WORKDIR /usr/app/src

COPY requirements.txt ./
COPY src/tennis_analyzer ./tennis_analyzer
COPY data ./data
COPY output ./output

RUN pip install -r ./requirements.txt && \
    apt-get update && \
    apt-get install -y vim && \
    apt-get install -y tree && \
    apt-get install -y libgl1
    
CMD [ "python3", "-m", "tennis_analyzer.main"]
