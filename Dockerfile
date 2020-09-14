FROM ubuntu:latest

RUN apt update &&\
    apt -y install python3-pip &&\
    mkdir /home/survival-analysis-visualiser/

RUN ls

COPY visualiser/ /home/survival-analysis-visualiser/

WORKDIR /home/survival-analysis-visualiser/

RUN ls

RUN pip3 install -r requirements.txt

WORKDIR /home/survival-analysis-visualiser/main/

EXPOSE 8050

CMD ["python3", "main.py"]

