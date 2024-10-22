Docker:
1.  в терминале пишем docker network create vehicle. затем пишем docker  run -d --network=vehicle --name=postgres_container -p 5432:5432 -e POSTGRES_DB=vehicle -e POSTGRES_USER=elvi -e POSTGRES_PASSWORD=124561 postgres:latest
2. в IDE пишем docker build . -t vehicle_app  
3. IDE пишем docker run -it --network=vehicle -p 8000:8000 -d vehicle_app
4. переходим на http://localhost:8000/admin/
