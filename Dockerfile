FROM python:3.6
COPY /index.html /
COPY /cgi-bin /
EXPOSE 8000
CMD ["python","-m","http.server","--cgi"]
