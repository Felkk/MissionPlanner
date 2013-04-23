import threading
import urllib2

def do_every(interval, worker_func, iterations = 0):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ();
  worker_func ();

  
def get_data():
  f = urllib2.urlopen( 'http://localhost:56781/mytest/' )
  print f.read( 100 )



do_every ( 0.25, get_data );