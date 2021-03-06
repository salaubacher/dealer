# Dealer
![example workflow](https://github.com/salaubacher/dealer/actions/workflows/test.yml/badge.svg)
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## About
[Dealer] is a library to create, shuffle and deal a deck of poker cards one at a time.

## Installation & Usage

### Installation
[Dealer] can be installed by running 

```pip install git+https://github.com/salaubacher/dealer```

It requires Python 3.7.0+ to run.

### Usage
```python
from dealer.poker_deck import PokerDeck

mydeck = PokerDeck()
mydeck.shuffle()
for i in range(53):
    print(mydeck.deal_one_card())
```

## Contributing
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

[Dealer]:https://github.com/salaubacher/dealer
