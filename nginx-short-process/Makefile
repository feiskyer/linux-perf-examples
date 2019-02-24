.PHONY: run
run:
	docker run --name nginx -p 10000:80 -itd feisky/nginx:sp
	docker run --name phpfpm -itd --network container:nginx feisky/php-fpm:sp

.PHONY: build
build:
	docker build -t feisky/nginx:sp -f Dockerfile.nginx .
	docker build -t feisky/php-fpm:sp -f Dockerfile.php-fpm .

.PHONY: push
push:
	docker push feisky/nginx:sp
	docker push feisky/php-fpm:sp

.PHONY: clean
clean:
	docker rm -f nginx phpfpm  || echo "Container nginx already deleted."
