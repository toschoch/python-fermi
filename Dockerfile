FROM python:alpine as builder

# Install dependencies
RUN apk --update add build-base postgresql-dev postgresql-client python3-dev libffi libffi-dev

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip wheel \
 --wheel-dir /wheels \
 -r requirements.txt

FROM python:alpine
MAINTAINER Tobias Schoch <tobias.schoch@vtxmail.ch>

# Install dependencies
RUN apk --update add postgresql-client libffi

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install dependencies
COPY --from=builder /wheels /wheels

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app
RUN rm .env && chmod +x entrypoint.sh


ENV APP_NAME="Fermi App"
ENV APP_SETTINGS="project.server.config.ProductionConfig"
ENV FLASK_DEBUG=0

# run server
CMD ["./entrypoint.sh"]
