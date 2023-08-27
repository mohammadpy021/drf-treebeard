FROM python:slim


COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1 
# ENV PYTHONDONTWRITEBYTECODE 1 



RUN pip install --upgrade pip 
# RUN apt install --update --no-cache postgresql-client postgresql-dev 
# RUN apt install --update -virtual gcc musl-dev 
# RUN apt install --update  build-base  linux-headers libffi-dev libxslt-dev libxml2-dev
# RUN apt install --update --no-cache  .tmp-deps \
#     libjpeg zlib-dev jpeg-dev libxslt libxml2 
#RUN apk add ...
#...     ""./requirements" will got Error.  we dont need "./" we need "/"
RUN pip install -r /requirements/development.txt 
# COPY . /app/
RUN chmod -R +x /scripts &&\
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home user && \
    chown -R user:user /vol && \
    chmod -R 755 /vol 
ENV PATH="/scripts:/py/bin:$PATH"
USER user

CMD [ "run.sh" ]
