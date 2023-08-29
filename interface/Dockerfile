FROM python:3.9

RUN mkdir /interface


COPY requirements.txt /interface


WORKDIR /interface

RUN pip install -r requirements.txt


COPY . /interface

# EXPOSE 8501
EXPOSE 8080

# CMD streamlit run --server.port 8501 app.py
CMD streamlit run --server.port 8080 app.py