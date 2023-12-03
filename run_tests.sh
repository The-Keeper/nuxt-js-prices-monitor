#/bin/bash

docker-compose -f docker-compose.tests.yml run --rm --entrypoint "python tests/datetime_test.py" fetching-service
docker-compose -f docker-compose.tests.yml run --rm --entrypoint "python tests/requests_test.py" fetching-service
docker-compose -f docker-compose.tests.yml run --rm --entrypoint "python tests/db_test.py" fetching-service