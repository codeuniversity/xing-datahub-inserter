#! /usr/bin/env bash

docker-compose -f docker-compose.test.yml up -d
sleep 160

python inserter_test.py
if [ $? -eq 1 ]
then
  echo 'test failed' >&2
  docker-compose -f docker-compose.test.yml down
  exit 1
else
  echo 'test was successful'
  docker-compose -f docker-compose.test.yml down
  exit 0
fi
