# ConcurBooking

This project is to explore the performance impact on one possible system design to handle the burst requests of users trying to get the same item concurrently.

## Architecture
[architecture for this project](./architecture.png)

The web application is setup on the stack of django + uwsgi + redis + postgres on a single vitual box.
baseline:
```
uwsgi --http :8000 --module ConcurBooking.wsgi --master --processes 1 --threads 4
```
The pressure test using ab command ```ab -n 10000 -c 1000 http://localhost:8000/``` give the following results:
```
    webapp  baseline
50%	180   140	1.28
66%   187   147	1.27
75%   195	154	1.26
80%   199	157	1.26
90%   210	181	1.16
95%   220	209	1.05
98%   236	217	1.08
99%   239	220	1.08
100%  244   230	1.06
```
