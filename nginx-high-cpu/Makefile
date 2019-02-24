.PHONY: run
run:
	docker run --name nginx -p 10000:80 -itd feisky/nginx:cpu
	docker run --name phpfpm -itd --network container:nginx feisky/php-fpm:cpu

.PHONY: build
build:
	docker build -t feisky/nginx:cpu -f Dockerfile.nginx .
	docker build -t feisky/php-fpm:cpu -f Dockerfile.php-fpm .

.PHONY: push
push:
	docker push feisky/nginx:cpu
	docker push feisky/php-fpm:cpu

.PHONY: clean
clean:
	docker rm -f nginx phpfpm || echo "Container nginx already deleted."
