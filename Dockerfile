FROM python:3

LABEL maintainer="Sergio Polanco"


# ENV PYTHONUNBUFFERED 1
# ENV FRONTEND_django-app_HOST=$FRONTEND_django-app_HOST
# ENV DB_django-app_HOST=$DB_django-app_HOST
# ENV DB_django-app_PORT=$DB_django-app_PORT
# ENV DB_django-app_USERNAME=$DB_django-app_USERNAME
# ENV DB_django-app_PASSWORD=$DB_django-app_PASSWORD
# ENV DB_django-app_NAME=$DB_django-app_NAME
# ENV django-app_SECRET_KEY=$django-app_SECRET_KEY
# ENV EMAIL_HOST=$EMAIL_HOST
# ENV EMAIL_HOST_USER=$EMAIL_HOST_USER
# ENV EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD
# ENV EMAIL_PORT=$EMAIL_PORT

RUN mkdir /code

WORKDIR /code
COPY . /code/
COPY docker-entrypoint.sh /usr/local/bin/

RUN pip install -r requirements.txt
RUN ln -s usr/local/bin/docker-entrypoint.sh /
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
