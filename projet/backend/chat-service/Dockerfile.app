FROM python:3.8-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask psycopg2-binary Flask-SQLAlchemy Flask-Migrate Flask-JWT-Extended

EXPOSE 5001

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

CMD ["flask", "run"]