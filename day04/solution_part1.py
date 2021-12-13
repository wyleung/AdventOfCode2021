#!/usr/bin/env python3

import collections
from typing import List, Union, Tuple, Iterator
import sys

input_file = sys.argv[1]
input_data = open(input_file)
input_dataset = input_data.readlines()

Board = List[Union[List[str], List[str], List[str], List[str], List[str]]]
Bingo = bool
Position = Tuple[int, int]

draw_line = input_dataset[0].strip().split(",")
# print(draw_line)


def board_positions(size=5) -> Iterator[Position]:
    for row in range(0, size):
        for col in range(0, size):
            yield (row, col)


def build_board(lines) -> Board:
    board = []
    for line in lines:
        numbers = [number for number in line.strip().split(" ") if len(number)]
        board.append(numbers)
    return board


def sum_undrawn_numbers(board: Board) -> int:
    total = 0
    for position in board_positions(len(board[0])):
        row, col = position
        position_val = board[row][col]
        if position_val.startswith("d"):
            continue
        total += int(position_val)
    return total


def update_board(board, drawn_number) -> Union[Board, Bingo]:
    has_bingo = False
    # 1. try to find the drawn number on our board
    for position in board_positions(len(board[0])):
        row, col = position
        if board[row][col] == drawn_number:
            board[row][col] = "d" + drawn_number

    # 2. try to find horizontal bingo, "numbers" starting with "d" are drawn
    for row in board:
        bingo = all([x.startswith("d") for x in row])
        if bingo:
            has_bingo = True
            break
    # 3. try to find vertical bingo, "numbers" starting with "d" are drawn
    for col_pos in range(len(board[0])):
        bingo = all(
            [board[row_pos][col_pos].startswith("d") for row_pos in range(len(board))]
        )
        if bingo:
            has_bingo = True
            break

    return board, has_bingo


boards = []
for i in range(2, len(input_dataset) - 2, 6):
    # print(i, input_dataset[i : i + 5])
    boards.append(build_board(input_dataset[i : i + 5]))


for drawn_number in draw_line:
    # draw numbers from the boards
    for i, board in enumerate(boards):
        new_board, bingo = update_board(board, drawn_number)
        if bingo:
            score = sum_undrawn_numbers(new_board) * int(drawn_number)

            print(f"We have bingo on board {i} with number {drawn_number}")
            print(f"It has a score of {score}")
            break
    else:
        continue
    break
