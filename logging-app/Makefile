.PHONY: run
run:
	docker run -v /tmp:/tmp --name=app -itd feisky/logapp


.PHONY: build
build:
	docker build -t feisky/logapp -f Dockerfile .


.PHONY: push
push:
	docker push feisky/logapp


.PHONY: clean
clean:
	docker rm -f app || echo "Container app already deleted."
