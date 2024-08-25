FROM python:3.11

ENV HOME /opt/app

WORKDIR ${HOME} 

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
