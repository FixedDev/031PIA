FROM python:3.12.7
LABEL authors=["fixed27","aguilar036"]

WORKDIR /app/
RUN pip3 install django==4.2.*
RUN pip3 install mysqlclient

COPY notasproyecto notasproyecto
COPY PIANotas PIANotas
COPY templates templates
COPY manage.py manage.py
COPY start.sh start.sh

EXPOSE 8080
CMD ["sh", "start.sh"]