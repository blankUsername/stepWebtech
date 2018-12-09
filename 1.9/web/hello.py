def app(environ, start_response):
   #data = b"Hello, World!\n"
   start_response("200 OK", [
       ("Content-Type", "text/plain")#,
       #("Content-Length", str(len(data))
       )
   ])
   #return iter([data])
   return [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]