# Python3 Seed

## Overview

A boilerplate Python 3 project set up for unit tests and continuous integration.

Specifically:

* Enforces Python style rules with [YAPF](https://github.com/google/yapf)
* Performs static analysis with [pyflakes](https://github.com/megies/pyflakes) and [pylint](https://github.com/PyCQA/pylint)
* Sorts imports with [isort](https://github.com/timothycrosley/isort)

## Installation

```bash
mkdir -p ./venv && \
  virtualenv --python python3 ./venv && \
  . venv/bin/activate && \
  pip install --requirement requirements.txt && \
  pip install --requirement dev_requirements.txt && \
  ./dev-scripts/enable-git-hooks
```

## Customization

To customize this for your project:

1. _Redacted, customizations completed on 2022-02-10_
1. Rename `app/dummy.py` and `app/dummy_test.py` to the module names of your choosing.
1. Begin working.

## Run

```bash
./app/main.py
```
