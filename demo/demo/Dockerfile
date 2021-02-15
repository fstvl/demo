FROM python:3.8
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y gcc unixodbc-dev graphviz graphviz-dev curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install msodbcsql17 -y
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
ENTRYPOINT ["python","manage.py"]
CMD ["runserver","0.0.0.0:8000"]

