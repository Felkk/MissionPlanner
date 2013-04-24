import threading
import time as time_
from datetime import datetime
import urllib2

def do_every(interval, worker_func, iterations = 0):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ();
  worker_func ();

  
def get_data():
  #prev_ms = int(round(time_.time() * 1000))
  #a = datetime.datetime.now()
  t_before = datetime.now()
  f = urllib2.urlopen( 'http://localhost:56781/mytest/' )
  t_after = datetime.now()
  #b = datetime.datetime.now()
  #curr_ms = int(round(time_.time() * 1000))
  #print str( int(round(time.time() * 1000)) - ms ) + ":" + f.read( 100 )
  #d_ms = curr_ms - prev_ms
  #c = b - a
  #milliseconds = (c.days * 24 * 60 * 60 + c.seconds) * 1000 + c.microseconds / 1000.0
  #print str( curr_ms ) + "," + str( prev_ms ) +"," + str( d_ms )+ ":" + f.read( 100 )
  #print str( milliseconds ) + ":" + f.read( 100 )
  t_delta = t_after - t_before
  print str( datetime.now() ) + " = "+ str( t_after.microsecond - t_before.microsecond ) + "," + str( t_delta.seconds ) + "." + str( t_delta.microseconds ) + ":" + f.read( 100 )

do_every ( 0.25, get_data );