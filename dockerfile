FROM python:3.9

WORKDIR /env

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV FLASK_APP env/CommerceApp.py

COPY requirements.txt /env

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "dbCLI.py", "create"]

ENTRYPOINT python env/CommerceApp.py
