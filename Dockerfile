FROM python:3.6
COPY /index.html /
COPY /cgi-bin /
RUN python3 -m http.server --cgi
