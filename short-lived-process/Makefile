.PHONY: build
build:
	gcc -o app app.c
	docker build -t feisky/app:short-process -f Dockerfile .

.PHONY: push
push:
	docker push feisky/app:short-process

.PHONY: run
run:
	docker run --name=app -itd feisky/app:short-process

.PHONY: clean
clean:
	rm -f app
	docker rm -f app || echo "Container app already deleted."
