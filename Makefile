.PHONY: all syntax test seed-qa rule-qa build report dict-qa qa compare clean

PYTHON ?= python3
BASELINE ?= ../KasbahKeys/KasbahKeys.txt

all: qa

syntax:
	$(PYTHON) -m py_compile scripts/build.py scripts/compare.py scripts/qa.py scripts/report.py scripts/rule_qa.py scripts/seed_qa.py

test:
	$(PYTHON) -m unittest discover -s tests

seed-qa:
	$(PYTHON) scripts/seed_qa.py

rule-qa:
	$(PYTHON) scripts/rule_qa.py

build:
	$(PYTHON) scripts/build.py

report:
	$(PYTHON) scripts/report.py

dict-qa:
	$(PYTHON) scripts/qa.py

qa: syntax test seed-qa rule-qa build report dict-qa
	git diff --exit-code

compare:
	$(PYTHON) scripts/compare.py dist/s4r0ut-standard.txt $(BASELINE)

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

