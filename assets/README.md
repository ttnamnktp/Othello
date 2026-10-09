# Othello AI — Heuristic Search and Monte Carlo Tree Search

A Python Othello (Reversi) game and comparative AI project investigating **heuristic-based adversarial search** and **Monte Carlo Tree Search (MCTS)**. In addition to implementing established search strategies, the project explores game-phase-aware evaluation functions and heuristic-guided MCTS.

**Course:** Introduction to Artificial Intelligence · Hanoi University of Science and Technology (HUST) · 2023–2024.

## Overview

Othello is a two-player, perfect-information board game on an 8 × 8 grid. Players alternately place black and white discs, flipping enclosed opposing discs. The winner has more discs when neither player can move. Strategic considerations include **corners, edges, disc count, and positional control** [1].

![Opening position and legal moves](assets/images/opening-position.png)

*Figure 1. Initial Othello board and legal opening moves.*

## Objectives and contributions

The project aims to:

1. Implement and compare **Greedy, Minimax, Alpha–Beta pruning, and MCTS**.
2. Evaluate traditional **Coin Parity** and **Static Weight** heuristics.
3. Propose **Hybrid Heuristic**, **Dynamic Hybrid Heuristic**, and **Dynamic Weight Matrix** evaluations that combine or adapt strategies over the course of a game.
4. Incorporate heuristic board evaluation into MCTS simulations rather than relying only on binary win/loss feedback.
5. Deliver a playable game with **Human vs. Human** and **Human vs. AI** modes and three difficulty levels.

## Search algorithms

| Algorithm | Main idea |
| --- | --- |
| **Greedy** | Choose the legal move with the highest immediate heuristic evaluation. |
| **Minimax** | Search alternating maximizing/minimizing decisions up to a fixed depth and evaluate leaf positions. |
| **Alpha–Beta pruning** | Avoid searching branches that cannot change the Minimax decision. |
| **MCTS** | Iteratively perform selection, expansion, simulation, and backpropagation [2]. |

![MCTS stages](assets/images/mcts-stages.png)

*Figure 2. The four stages of Monte Carlo Tree Search.*

### MCTS selection

MCTS uses an upper-confidence-bound-style selection score:

$$
\mathrm{UCB}_i = \frac{w_i}{n_i} + C\sqrt{\frac{\ln N}{n_i}},
$$

where $w_i$ is the accumulated reward of child $i$, $n_i$ its visit count, $N$ the parent visit count, and $C$ an exploration parameter.

![UCB selection formula](assets/images/ucb-formula.png)

*Figure 3. Upper confidence bound (UCB) selection score.*

## Heuristic evaluation

### 1. Coin Parity and Static Weight

**Coin Parity** evaluates the difference between the players' disc counts. **Static Weight** assigns positional values to board squares, emphasizing stable strategic locations such as corners and penalizing dangerous squares near them [1].

![Static positional weight matrix](assets/images/static-weight-matrix.png)

*Figure 4. Static positional weight matrix for Othello.*

### 2. Hybrid Heuristic

The team's **Hybrid Heuristic** combines disc-count and positional-weight strategies using normalized component scores and a mixing coefficient $\alpha$. Unlike a single-feature heuristic, it can balance multiple strategic objectives. Its components use the disc count (`count(player)`), weighted positional score (`weight(player)`), and a normalization factor (`max_weight`).

### 3. Dynamic Hybrid Heuristic

The **Dynamic Hybrid Heuristic** adjusts the component weight $\alpha$ with game progress. Early moves prioritize strategically important squares; late moves progressively emphasize disc count. This addresses the limitations of static evaluation functions.

### 4. Dynamic Weight Matrix

The **Dynamic Weight Matrix** varies individual board-square weights over time. It begins with strategically differentiated weights and gradually approaches a uniform matrix of ones by the final move.

### 5. Heuristic-guided MCTS

Instead of evaluating simulations solely with binary outcomes, the proposed MCTS variant uses a **heuristic-derived reward** based on board position. This allows simulation feedback to reflect positional advantage, not only the final win/loss event. This is a search-time evaluation strategy, **not a claim that a neural network or persistent RL policy is trained**.

## Experimental evaluation

The experiments below summarize the team's course-project evaluations; they are not independently reproduced benchmarks.

### Search time

| Search method | Reported runtime |
| --- | --- |
| Greedy | Approximately 0 s |
| Minimax, depth 3 | 1–2 s |
| Minimax with Alpha–Beta pruning, depth 5 | 0–2 s |
| Monte Carlo Tree Search | 1–3 s |

These are approximate observed runtimes rather than hardware-independent benchmarks. Hardware specifications and measurement variance are not documented.

### Comparing heuristics

We compare **Coin Parity** and **Static Weight** against **Hybrid Heuristic**, **Dynamic Hybrid Heuristic**, and **Dynamic Weight**, using **Minimax at depth 3**.

![Comparison against coin parity](assets/images/coin-parity-comparison.png)

*Figure 5. Win-rate comparisons against Coin Parity.*

![Comparison against static weight](assets/images/static-weight-comparison.png)

*Figure 6. Win-rate comparisons against Static Weight.*

### MCTS comparisons

The experiments compare MCTS and other search methods under **Static Weight**, **Coin Parity**, and **Dynamic Weight** evaluations. In these course-project comparisons, heuristic-guided MCTS showed improved win rates relative to the traditional MCTS baseline.

![MCTS with static weight](assets/images/mcts-static-weight.png)

*Figure 7. MCTS comparisons using Static Weight.*

![MCTS with coin parity](assets/images/mcts-coin-parity.png)

*Figure 8. MCTS comparisons using Coin Parity.*

![MCTS with dynamic weight](assets/images/mcts-dynamic-weight.png)

*Figure 9. MCTS comparisons using Dynamic Weight.*

> Experimental sample sizes, random seeds, and confidence intervals are not documented. These graphs should be interpreted as **course-project results**, not statistically validated benchmark claims.

## Application

The game provides a graphical interface, **Human vs. Human** and **Human vs. AI** modes, and **Easy / Medium / Hard** difficulty choices. The implementation uses **Python**, **Pygame** for the GUI, and **Poetry** for dependency management.

### Getting started

Install [Poetry](https://python-poetry.org/docs/#installation), then from the project root:

```bash
poetry install
poetry run python main.py
```

The source code also contains search and heuristic modules for experimentation beyond the three playable difficulty presets.

## Project organization

```text
Othello/
├── main.py
├── ai/
│   ├── heuristics/
│   ├── search_algorithms/
│   └── reinforcement_learning/
├── pyproject.toml
├── assets/
│   └── images/                   # Figures used by this README
└── README.md
```

## Future work

Potential next steps include refining the graphical interface, running larger-scale experiments to select suitable parameters, and optimizing the MCTS configuration and reward evaluation.

## Team

**Backend:** Trần Thành Nam, Vũ Việt Anh, Dư Vũ Mạnh Đức.  
**Frontend:** Trần Minh Huyền, Nguyễn Lê Quý Dương.  
**Supervisor:** Assoc. Prof. Lê Thanh Hương.

The backend team worked on game architecture, search algorithms, heuristic and MCTS improvements, evaluation, and reporting. The frontend team worked on interface design, implementation, and testing.

## References

The project draws on the following studies of heuristic evaluation and Monte Carlo search in Othello. Bibliographic details are limited to those available in the project materials.

[1] Derrac, Sannidhanam, Vaishnavi, and Muthukaruppan Annamalai. **“An Analysis of Heuristics in Othello.”** Department of Computer Science and Engineering, Paul G. Allen Center, University of Washington, Seattle, WA 98195. *(Publication year and venue not specified.)*

[2] P. Hingston and M. Masek. **“Experiments with Monte Carlo Othello.”** Edith Cowan University Research Online, 2007.
