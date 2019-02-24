.PHONY: build
build:
	gcc -o app app.c -pthread
	docker build -t feisky/app:mem-leak -f Dockerfile .
	gcc -o app app-fix.c -pthread
	docker build -t feisky/app:mem-leak-fix -f Dockerfile .

.PHONY: push
push:
	docker push feisky/app:mem-leak
	docker push feisky/app:mem-leak-fix

.PHONY: run
run:
	docker run --name=app -itd feisky/app:mem-leak

.PHONY: clean
clean:
	rm -f app
	docker rm -f app || echo "Container app already deleted."
