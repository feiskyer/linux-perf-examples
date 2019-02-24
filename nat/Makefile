.PHONY: run
run:
	docker run --name nginx --privileged -p 8080:8080 -itd feisky/nginx:nat

.PHONY: host-network
host-network:
	docker run --name nginx-hostnet --privileged --network=host -itd feisky/nginx:80

.PHONY: build
build:
	docker build -t feisky/nginx:nat -f Dockerfile .
	docker build -t feisky/nginx:80 -f Dockerfile.80 .

.PHONY: push
push:
	docker push feisky/nginx:nat
	docker push feisky/nginx:80

.PHONY: clean
clean:
	docker rm -f nginx nginx-hostnet || echo "Containers already deleted."
