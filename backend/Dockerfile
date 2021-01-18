FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/backend

COPY requirements*.txt ./

RUN apt-get update && \
    apt-get install -y libpq-dev python-dev python3-psycopg2 python3-pygresql

RUN pip3 install -r requirements.txt

# # selenium 설치 코드. 용량이 900메가 후반대로 커진다.
# RUN apt-get update && \ 
#     apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget libgbm1 apt-utils
# RUN apt-get update && apt-get install -y wget
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

COPY ./ ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--setting=nonnon.configs.local"]