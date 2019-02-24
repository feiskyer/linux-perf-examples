.PHONY: build
build:
	gcc -o app app.c
	docker build -t feisky/app:io-direct -f Dockerfile .
	gcc -o app app-cached.c
	docker build -t feisky/app:io-cached -f Dockerfile .

.PHONY: push
push:
	docker push feisky/app:io-direct
	docker push feisky/app:io-cached

.PHONY: run
run:
	docker run --privileged --name=app -itd feisky/app:io-direct

.PHONY: clean
clean:
	rm -f app
	docker rm -f app || echo "Container app already deleted."
