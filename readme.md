docker build -t flask-mysql-app .
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=example mysql:latest
docker run -d --name flask-app -p 5000:5000 --link mysql:mysql flask-mysql-app
