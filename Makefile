# Запускаем Brain-games

brain-games:
	poetry run brain-games

# Собираем пакет

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
