FROM python:3.7

RUN mkdir /app 
WORKDIR /app
COPY src/A.py /app/A.py
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

EXPOSE 5001
CMD ["python","/app/A.py"]
