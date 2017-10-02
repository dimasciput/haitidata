SHELL := /bin/bash
PROJECT_ID := haitidata

build-geowebcache:
	@docker-compose -p $(PROJECT_ID) build geowebcache
	@docker-compose -p $(PROJECT_ID) up -d geowebcache

build-nginx:
	@cd nginx && ./build.sh

build-django:
	@cd django_haitidata && ./build.sh

build-db:
	@cd db && ./build.sh

build-geoserver:
	@cd geoserver && ./build.sh

build-all: build-db build-nginx build-django
