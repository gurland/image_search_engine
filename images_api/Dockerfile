FROM python:3.7-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

CMD python -c "import tensorflow as tf; print(tf.constant(42) / 2 + 2)"
