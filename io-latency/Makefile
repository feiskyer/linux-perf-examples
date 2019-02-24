.PHONY: run
run:
	docker run --name=app -p 10000:80 -itd feisky/word-pop


.PHONY: build
build:
	docker build -t feisky/word-pop -f Dockerfile .


.PHONY: push
push:
	docker push feisky/word-pop


.PHONY: clean
clean:
	docker rm -f app || echo "Container app already deleted."
