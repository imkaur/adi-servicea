From python:3.7

run mkdir /app 
WORKDIR /app
COPY src/rdumResponse.py /app/rdumResponse.py
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

EXPOSE 5001
CMD ["python","/app/rdumResponse.py"]
