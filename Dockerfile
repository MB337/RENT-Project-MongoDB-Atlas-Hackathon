FROM python:3.10-alpine
WORKDIR /var/www
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ ./

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:app" ]
