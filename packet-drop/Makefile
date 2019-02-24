.PHONY: run
run:
	docker run --name nginx --hostname nginx --privileged -p 80:80 -itd feisky/nginx:drop

.PHONY: build
build:
	docker build -t feisky/nginx:drop -f Dockerfile .

.PHONY: push
push:
	docker push feisky/nginx:drop

.PHONY: clean
clean:
	docker rm -f nginx || echo "Container nginx already deleted."