project made for two environemnt : productions and local 

for run project on production you have to make a envfile(folder) like `sample.env` and set it valid address on `docker-compose-production.yml`

for both postgres and django app 

you can change some env value like 
```
DEFAULT_AMOUNT: 100000 
MIN_RESERVATION_HOURS:1 #hours
MAX_RESERVATION_HOURS:3 #hours
RESTAURANT_OPENING_HOUR: 8 # 8 AM
RESTAURANT_CLOSING_HOUR: 23 # 11 PM

```
But if you dont set it it will take default value 



you can run project with command `docker compoe up -f docker-compose-production.yml -d --build` 

this will build project and create docker images and after that run it 

you can make 10 samle table data on database with command `python manage.py seed_table` 

!!! if you run on docker container you have to run this command 


`docker compose -f docker-compose-production.yml exec -it web  python manage.py seed_table `  !! make sure that container is up 


swagger is available on address `/api/docs` you can see apis 

first of all you have too register a new user and take access token for login 

set raw access token on Authorize section on swagger to handle its Authorization 

you can reserv new table with its api 


!!!

TIME that is showing on swagger is based on UTC , so you need to send `start_time` and `end_time` base on UTC and app will save it by  `Asia/Tehran` on db 

!!!


Given that the question does not mention dividing the number of individual between several tables, this issue has been ignored and people over 10 cannot reserve a table.



