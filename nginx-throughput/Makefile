.PHONY: run
run:
	docker run --name nginx --network host --privileged -itd feisky/nginx-tp
	docker run --name phpfpm --network host --privileged -itd feisky/php-fpm-tp

.PHONY: build
build:
	docker build -t feisky/nginx-tp -f Dockerfile.nginx .
	docker build -t feisky/php-fpm-tp -f Dockerfile.php-fpm .

.PHONY: push
push:
	docker push feisky/nginx-tp
	docker push feisky/php-fpm-tp

.PHONY: clean
clean:
	docker rm -f nginx phpfpm || echo "Container nginx already deleted."
