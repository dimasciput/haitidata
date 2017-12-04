#!/usr/bin/env bash
IMAGE_NAME=haitidata_db
TAG_NAME=latest
docker build --no-cache -t dimasciput/${IMAGE_NAME} .
docker tag dimasciput/${IMAGE_NAME}:latest dimasciput/${IMAGE_NAME}:${TAG_NAME}
docker push dimasciput/${IMAGE_NAME}:${TAG_NAME}