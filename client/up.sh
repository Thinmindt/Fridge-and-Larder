#!/bin/bash

get-graphql-schema http://server:5001/graphql --json > ./schema.json

vue ui --headless --port 8000 --host 0.0.0.0
# npx vue-cli-service serve --host 0.0.0.0 --port 5000
