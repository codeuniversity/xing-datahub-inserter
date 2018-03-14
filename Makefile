
proto:
	cd xing-datahub-protocol; protoc --python_out=../build protocol.proto

env:
	python3.6 -m venv env

dep:
	pip install -r requirements.txt

librdkafka-linux-install:
	apt install librdkafka-dev

librdkafka-mac-install:
	brew install librdkafka
