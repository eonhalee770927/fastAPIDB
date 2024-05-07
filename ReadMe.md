## Postgres DB 실행
````
$ docker run -it --rm --name postgre-container -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres:9.6.24
````
>   username: postgres
>   password: admin
 
> https://hub.docker.com/_/postgres


## package 환경 설정
````
$ pip install -r requirements.txt
````

## Application 구동
````
$ uvicorn app.main:app --reload
````
> (.venv) PS C:\workspaces\PycharmProjects\fastAPIDB> uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\workspaces\\PycharmProjects\\fastAPIDB']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [24680] using WatchFiles
postgresql://postgres:admin@127.0.0.1:5432/postgres

## Swagger 접속
````
chrome 접속
http://127.0.0.1:8000/docs#
````
> https://fastapi.tiangolo.com/tutorial/metadata/
