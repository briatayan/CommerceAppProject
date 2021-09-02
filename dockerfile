FROM python:3.9
ENV VIRTUAL_ENV=env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /env
WORKDIR /env

RUN pip install -r requirements.txt

COPY env/CommerceApp.py .

CMD ["python", "CommerceApp.py"]
