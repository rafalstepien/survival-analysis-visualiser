FROM ubuntu:latest

RUN apt update &&\
    apt -y install python3-pip &&\
    mkdir /home/survival-analysis-visualiser/
    
COPY visualiser/ /home/survival-analysis-visualiser/

WORKDIR /home/survival-analysis-visualiser/visualiser/

RUN pip3 install -r requirements.txt

WORKDIR /home/survival-analysis-visualiser/visualiser/main/

CMD ["python", "main.py"]

