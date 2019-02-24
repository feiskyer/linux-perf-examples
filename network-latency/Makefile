.PHONY: run
run:
	docker run --name nginx --network=host -itd feisky/nginx:latency

.PHONY: build
build:
	docker build -t feisky/nginx:latency -f Dockerfile .

.PHONY: push
push:
	docker push feisky/nginx:latency

.PHONY: clean
clean:
	docker rm -f nginx || echo "Container nginx already deleted."
