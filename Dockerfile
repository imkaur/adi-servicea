From python:3.7

run mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 5001
CMD ["python","/app/rdumResponse.py"]
