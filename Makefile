.PHONY: sync kernels notebooks sanitize render check clean-rendered

sync:
	uv sync

kernels:
	uv run jupyter kernelspec list

notebooks:
	uv run python3 scripts/build-public-notebooks.py

sanitize:
	uv run python3 scripts/sanitize-notebooks.py --write notebooks

render: sanitize
	uv run bash scripts/render-notebooks.sh

check:
	uv run bash scripts/check-public-safety.sh

clean-rendered:
	rm -f docs/notebooks/*.html
