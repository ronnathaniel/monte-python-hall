
from random import randrange


class DoorGoat:
    pass


class DoorCar:
    pass


class NoRepeatRandom:
    def __init__(self):
        self.last = None

    def __call__(self, *args, **kwargs):
        r = randrange(*args)
        while r == self.last:
            r = randrange(*args)
        self.last = r
        return r


smart_randrange = NoRepeatRandom()


def simulate(
        door_num: int = 3,
        switch: bool = True,
        utilize_real_random: bool = True,
):
    doors = [DoorGoat()] * door_num
    randr = randrange if utilize_real_random else smart_randrange
    car_index = randr(0, door_num)
    first_selection_index = randr(0, door_num)
    doors[car_index] = DoorCar()

    car_chosen_first = first_selection_index == car_index
    if car_chosen_first:
        second_selection_option_index = randr(0, door_num)
        while second_selection_option_index == car_index:
            second_selection_option_index = randr(0, door_num)
    else:
        second_selection_option_index = car_index

    # uncomment for use of all doors opened:
    #
    # doors_opened_indexes = []
    # for i, door in enumerate(doors):
    #     if type(door) is DoorGoat:
    #         if (
    #                 car_chosen_first and i != second_selection_option_index
    #         ) or (
    #             not car_chosen_first and i != first_selection_index
    #         ):
    #             doors_opened_indexes.append(i)

    if switch:
        second_selection_index = second_selection_option_index
    else:
        second_selection_index = first_selection_index

    if type(doors[second_selection_index]) is DoorCar:
        return True
    return False


def run_simulation():
    games_to_play = 1_500
    doors_num = 3

    randrange_switch_pl = [
        simulate(doors_num, True, True) for _ in range(games_to_play)
    ]
    randrange_no_switch_pl = [
        simulate(doors_num, False, True) for _ in range(games_to_play)
    ]
    smart_randrange_switch_pl = [
        simulate(doors_num, True, False) for _ in range(games_to_play)
    ]
    smart_randrange_no_switch_pl = [
        simulate(doors_num, False, False) for _ in range(games_to_play)
    ]

    def sprint_win_percentage(arr):
        trues = 0
        total = len(arr)
        for item in arr:
            if item:
                trues += 1
        return trues / total * 100

    print(f'Simulated {games_to_play} games of each-')
    print(f'Real Random   w/  Switch = {sprint_win_percentage(randrange_switch_pl):,}% win')
    print(f'Real Random   w/o Switch = {sprint_win_percentage(randrange_no_switch_pl):,}% win')
    print(f'Initial Wrong w   Switch = {sprint_win_percentage(smart_randrange_switch_pl):,}% win')
    print(f'Initial Wrong w/o Switch = {sprint_win_percentage(smart_randrange_no_switch_pl):,}% win')


if __name__ == '__main__':
    run_simulation()
