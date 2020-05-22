# ConcurBooking
A low latency high scalable system designed to handle burst concurrency requests 

This project is built to handle high concurrency requests in a situation such as ticket booking for a hot sports event. The requirement of the system includes:
* Sell the tickets accurately, no oversold, no understold
* Respond to users in low latency
* Reliable under the pressure of high amount of requests

The web application is setup in django+uwsgi+postgres on a single machine
baseline:
```
uwsgi --http :8000 --module ConcurBooking.wsgi --master --processes 1 --threads 4
```
The pressure test using ab command ```ab -n 10000 -c 1000 http://localhost:8000/``` give the following results:
```
Concurrency Level:      1000
Time taken for tests:   61.315 seconds
Complete requests:      10000
Failed requests:        744
   (Connect: 0, Receive: 0, Length: 744, Exceptions: 0)
Total transferred:      152483344 bytes
HTML transferred:       151344856 bytes
Requests per second:    163.09 [#/sec] (mean)
Time per request:       6131.487 [ms] (mean)
Time per request:       6.131 [ms] (mean, across all concurrent requests)
Transfer rate:          2428.60 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    5  15.8      0      76
Processing:    86 5669 16250.7    448   61238
Waiting:        0 1286 5667.5    436   56160
Total:        150 5674 16263.8    448   61312

Percentage of the requests served within a certain time (ms)
  50%    448
  66%    475
  75%   1436
  80%   1463
  90%   3527
  95%  61238
  98%  61262
  99%  61272
 100%  61312 (longest request)
```
