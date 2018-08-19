#!/usr/bin/env python3

import cgi
import html
import docker

form = cgi.FieldStorage()
cid = form.getfirst("cid", "")
cid = html.escape(cid)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Containers</title>
        </head>
        <body>""")

client = docker.from_env()
if cid == "":
  print("<h1>Containers:</h1>")
  containers = client.containers.list()
  for container in containers:
    print("<a href='?cid={}'>{}({})</a><br>".format(container.id,container.name,container.attrs['Config']['Image']))
else:
  container = client.containers.get(cid)
  print("<h1>Logs for {} ({}): </h1>".format(container.name,container.attrs['Config']['Image']))
  logs = container.logs(timestamps=True).decode()
  for line in logs.split("\n"):
    print("{}<br>".format(line))

print("""</body>
        </html>""")