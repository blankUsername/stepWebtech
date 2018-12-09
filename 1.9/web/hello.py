def app(environ, start_response):
   d = "\n".join(environ['QUERY_STRING'].split('&'))
   start_response("200 OK", [
       ("Content-Type", "text/plain")#,
       ("Content-Length", str(len(data))
   ])
   return iter([data.encode('utf-8')])
