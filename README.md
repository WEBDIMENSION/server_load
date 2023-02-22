# Server Load

## Apache Bench

--- 

```bash
docker-compose run apachebench
ab -e /output/apace_bench.csv -n 200 -c 3  -t 15 'http://host.docker.internal:8080/'
```

### Apace Bench Params

-n : 引数にはリクエストの回数、
-c : 同時に発行するリクエストの回数
-t : Timeout (Second)


## Locust

[http://localhost:8081/](http://localhost:8089/)

## gatling

[http://localhost:8082/](http://localhost:8089/)
```bash
docker-compose up -d
docker-compose exec gatling gatling [-s TestClassName]
docker-compose exec gatling gatling -s TestClassName
```
