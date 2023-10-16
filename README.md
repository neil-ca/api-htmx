# Services in k3s
Updating the mongo config in `mongod.conf`


Requests to test the services
```sh
curl -X POST http://mp3converter.com/login -u neil@gmail.com:secret

curl -X POST -F 'file=@./test.mp4' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5laWxAZ21haWwuY29tIiwiZXhwIjoxNjk2MTExNzY0LCJpYXQiOjE2OTYwMjUzNjQsImFkbWluIjp0cnVlfQ.oOpTJhC_jgqL87TCaWUdwFDDGksLjHRsWsX7XLzwLrU' http://mp3converter.com/upload
```
