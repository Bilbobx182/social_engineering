#!/usr/bin/env bash

docker build \
  --file Dockerfile \
  --tag social_engineering:latest \
  .

docker run -v /etc/letsencrypt/live/taifuwiddies.net:/ssl  -p 443:443 social_engineering:latest