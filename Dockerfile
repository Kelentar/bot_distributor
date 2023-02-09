FROM python:3.10

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir -r requirments.txt

CMD ["python", "bot.py"]