Docker:
1.  � ��������� ����� docker  run -d --network=vehicle --name=postgres_container -p 5432:5432 -e POSTGRES_DB=vehicle -e POSTGRES_USER=elvi -e POSTGRES_PASSWORD=124561 postgres:latest
2. � IDE ����� docker build . -t vehicle_app  
3. IDE ����� docker run -it --network=vehicle -p 8000:8000 -d vehicle_app
4. ��������� �� http://localhost:8000/admin/
