# DEVICE ?= /dev/sda
# BPS_LIMIT ?= 10mb

.PHONY: build
build:
	gcc -o app app.c
	docker build -t feisky/app:iowait -f Dockerfile .
	gcc -o app app-fix1.c
	docker build -t feisky/app:iowait-fix1 -f Dockerfile .
	gcc -o app app-fix2.c
	docker build -t feisky/app:iowait-fix2 -f Dockerfile .

.PHONY: push
push:
	docker push feisky/app:iowait
	docker push feisky/app:iowait-fix1
	docker push feisky/app:iowait-fix2

.PHONY: run
run:
	docker run --privileged --name=app -itd feisky/app:iowait
	#docker run --name=app --device $(DEVICE):$(DEVICE) --device-read-bps $(DEVICE):$(BPS_LIMIT) -itd feisky/app:iowait /app -d $(DEVICE)

.PHONY: fix1
fix1:
	docker run --privileged --name=app -itd feisky/app:iowait-fix1

.PHONY: fix2
fix2:
	docker run --privileged --name=app -itd feisky/app:iowait-fix2

.PHONY: clean
clean:
	rm -f app
	docker rm -f app
