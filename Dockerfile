FROM python:3.6
RUN pip install docker
WORKDIR /srv
COPY index.html .
COPY cgi-bin/* cgi-bin/
EXPOSE 8000
CMD ["python","-m","http.server","--cgi"]
