FROM python:alpine

LABEL maintainer="feiskyer@gmail.com"

RUN pip install flask

EXPOSE 80
ADD app.py /app.py

CMD ["python", "/app.py"]
