# run docker
docker run --rm --name docker_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
docker run --rm --name pg_test -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres

echo "String the docker.."
sleep 25
python3 ./create_tables.py