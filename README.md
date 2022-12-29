# Monte Python Hall

> Run Monte Hall Problem Simulations in python.


Familiarize thyselves with the [Monte Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem), consisting of 3 doors; representing 2 goats and a car dispersed behind each door.

![Monte Hall](https://miro.medium.com/max/1400/1*_ZNfMN84NNLHYX5tfDbLzg.jpeg)

## Usage

Run 
```shell
$ python3 disprove.py
```

to see the simulated games:

    Simulated 1500 games of each-
    Real Random   w/  Switch = 65.86666666666666% win
    Real Random   w/o Switch = 34.8% win
    Initial Wrong w   Switch = 100.0% win
    Initial Wrong w/o Switch = 0.0% win


`Real Random` refers to the usage of `random.randrange` to choose the initial door selection.

`Initial Wrong` refers to the first choice being incorrect, by using a smart Random Randrange alternative.

And `Switch` refers to the user switching to the second option presented after a first door is opened.


<br/>

### Change Options

In `run_simulation()`, options
- `games_to_play`: int = the number of games to plau for each scenario.
- `doors_num`: int = the number of doors in each game.

