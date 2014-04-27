
deploy: build
	rsync -avz ./build/ barn-owl:/var/www/philadams.net/

build: node_modules
	node_modules/.bin/metalsmith

node_modules: package.json
	npm install

.PHONY: build
