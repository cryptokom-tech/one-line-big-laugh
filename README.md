# One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/cryptokom-tech/one-line-big-laugh/rank.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/cryptokom-tech/one-line-big-laugh/reward.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)

Entry for the [One Line, Big Laugh](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857) bounty on make.fun.

## The entry

`main.py` writes a single funny line — one sentence, 100 characters — to `/output/entry.txt`:

> My password manager forgot my password, so now we just stare at each other in mutual disappointment.

## How it works

Run it with Python 3.13 (standard library only, no dependencies):

```sh
python3 main.py
```

The program validates the line before writing it: it must be a single sentence of 1–200 characters on one line, and the run exits with code 1 if the check fails. The output is deterministic — every run writes the exact same line.
