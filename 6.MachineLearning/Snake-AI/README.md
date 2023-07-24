# Snake AI

[![Python application](https://github.com/SajjadAemmi/Snake-AI/actions/workflows/python-app.yml/badge.svg)](https://github.com/SajjadAemmi/Snake-AI/actions/workflows/python-app.yml)
[![Python package](https://github.com/SajjadAemmi/Snake-AI/actions/workflows/python-package.yml/badge.svg)](https://github.com/SajjadAemmi/Snake-AI/actions/workflows/python-package.yml)

Snake game with artificial intelligence written in python using pygame library and trained with pytorch.

![screenshot](assets/Screenshot.png)

# Train
Use the following command for generate eight neighborhoods csv dataset:

```
python generate_dataset_8_direction.py --count 1000000
```

Use the following command for train model:

```
python train.py --epochs 8
```


# Run
Use the following command for run game with machine learning inference:

```
python main_machine_learning.py --weights ./weights/snake.pt
```

Use the following command for run game with classic rule based AI inference:

```
python main_rule_based.py
```
