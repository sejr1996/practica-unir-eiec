IMAGE_NAME := python:3.6-slim
ARGS := words.txt yes

.PHONY: all run

all: run

run: main.py
	docker run --rm \
		--volume `pwd`:/opt/app \
		--env PYTHON_PATH=/opt/app \
		-w /opt/app \
		$(IMAGE_NAME) \
		python3 main.py $(ARGS)

# Comentarios
# main.py es la entrada del programa
# La regla run depende de main.py