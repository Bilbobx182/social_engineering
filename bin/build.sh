#!/usr/bin/env bash

docker build \
  --file Dockerfile \
  --tag social_engineering:latest \
  .

docker run -d -p 80:80 \
--mount source=/etc/letsencrypt/live/taifuwiddies.net,destination=/app\
social_engineering:latest
