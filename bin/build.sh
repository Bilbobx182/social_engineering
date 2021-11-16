#!/usr/bin/env bash

docker build \
  --file Dockerfile \
  --tag social_engineering:latest \
  .

docker run social_engineering:latest