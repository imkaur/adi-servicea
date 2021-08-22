From python:3.7

run mkdir /app 
WORKDIR /app
COPY src/B.py /app/B.py
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

EXPOSE 8080
CMD ["python","/app/B.py"]
