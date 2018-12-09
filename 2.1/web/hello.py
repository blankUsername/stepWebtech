def app(environ, start_response):
   d = "\n".join(environ['QUERY_STRING'].split('&'))
   d=d.encode('utf-8')
   start_response("200 OK", [
       ("Content-Type", "text/plain")#,
       #("Content-Length", str(len(d)))
   ])
   return iter([d])
