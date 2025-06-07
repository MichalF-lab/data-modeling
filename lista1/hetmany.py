import random
import time
import math
def chess_board(n):
    """Generates a chessboard pattern of size n x n."""
    return [[0 for j in range(n)] for i in range(n)]


def hetman_move(board, x, y):
    n = len(board)
    moves = []

    for i in range(n):
        if i != x:
            moves.append((i, y))
        if i != y:
            moves.append((x, i)) 

    for i in range(-n, n):
        if 0 <= x + i < n and 0 <= y + i < n and (i != 0):
            moves.append((x + i, y + i))  # Main diagonal
        if 0 <= x + i < n and 0 <= y - i < n and (i != 0):
            moves.append((x + i, y - i))  # Anti-diagonal

    moves.append((x,y))
    return moves


def hetman_posible_positions(board, i,j):
    if board[i][j] == 1:
        return False
    moves = hetman_move(board, i, j)
    if any(board[x][y] == 1 for x, y in moves):
        return False
    return True


def solve(board, actual_row = 0):
    n = len(board)
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = solve(new_board, actual_row + 1)
            if result: return result


#print(solve(chess_board(8)), flush=True)


def solve_permutation(board, actual_row = 0):
    n = len(board)
    permutations = 0
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return 1
            permutations += solve_permutation(new_board, actual_row + 1)
    return permutations


#print(solve_permutation(chess_board(8)))

"""
Próba odopoweidzenia na pytanie ile pozyzji jest równoważnych

def solve_sym(board, actual_row = 0, hetman_count = 0):
    n = len(board)
    result = []
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if hetman_count + 1 == n:
                return [new_board]
            ext = solve_sym(new_board, actual_row + 1, hetman_count + 1)
            if ext:
                result.extend(ext)
    return result

full_posibilty = solve_sym(chess_board(8))
posibilty = full_posibilty[:]

tab = []
n = len(full_posibilty[0])

# Tworzymy odwrócone pionowo plansze
for board in full_posibilty:
    temp = []
    for i in reversed(range(n)):
        temp.append(board[i][:])
    tab.append(temp)

# Konwertujemy plansze na tuple dla porównania
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

set1 = set(board_to_tuple(board) for board in full_posibilty)
set2 = set(board_to_tuple(board) for board in tab)

common_count = len(set1 & set2)
print(common_count)
"""

def random_solve(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    random.shuffle(temp)
    for j in temp:
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve(new_board, actual_row + 1)
            if result: return result

# for i in range(3,22):
#     start_time = time.time()
#     a = random_solve(chess_board(i))
#     end_time = time.time()  # czas po wykonaniu operacji
#     elapsed_time = end_time - start_time 
#     print(i," ",elapsed_time, "sekundy")

#     start_time = time.time()
#     a = solve(chess_board(i))
#     end_time = time.time()  # czas po wykonaniu operacji
#     elapsed_time = end_time - start_time 
#     print(i," ",elapsed_time, "sekundy")

def bounded_gauss_random(mu=0.5, sigma=0.15):
    while True:
        x = random.gauss(mu, sigma)
        if 0 <= x < 1:
            return x

def random_solve_gauss1(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    random.shuffle(temp, random=bounded_gauss_random)
    for j in temp:
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve_gauss1(new_board, actual_row + 1)
            if result: return result


import numpy as np

def bounded_gauss_random2():
    x = np.clip(np.random.normal(0.5, 0.1), 0,  0.999999)
    return x

def random_solve_gauss2(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    for j in temp:
        random.shuffle(temp, random=bounded_gauss_random2)
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve_gauss2(new_board, actual_row + 1)
            if result: return result

from concurrent.futures import ProcessPoolExecutor, TimeoutError
import time

def solve_and_measure(solve_func, board):
    """Uruchom funkcję i zmierz czas"""
    start_time = time.time()
    solve_func(board)
    end_time = time.time()
    return end_time - start_time

import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed, TimeoutError
import multiprocessing

def solve_and_measure_safe(func, board):
    """Wrapper z obsługą błędów dla funkcji solve_and_measure"""
    try:
        return solve_and_measure(func, board)
    except Exception as e:
        print(f"Błąd w funkcji: {e}")
        return None

if __name__ == "__main__":
    # Ważne dla Windows - ustaw sposób uruchamiania procesów
    multiprocessing.set_start_method('spawn', force=True)
    
    wynik1, wynik2, wynik3 = [], [], []
    random.seed(42)
    np.random.seed(42)
    
    # Jeden ProcessPoolExecutor dla całego programu
    with ProcessPoolExecutor(max_workers=3) as executor:
        for i in range(412, 420): #103
            print(f"\nPrzetwarzanie planszy {i}...")
            board = chess_board(i)
            
            # Uruchom wszystkie 3 funkcje równolegle
            tasks = [
                (executor.submit(solve_and_measure_safe, random_solve, board), 1, "funkcja1"),
                (executor.submit(solve_and_measure_safe, random_solve_gauss1, board), 2, "funkcja2"),
                (executor.submit(solve_and_measure_safe, random_solve_gauss2, board), 3, "funkcja3")
            ]
            
            results = {1: None, 2: None, 3: None}
            completed_count = 0
            
            try:
                # Czekaj maksymalnie 20 sekund na wszystkie wyniki
                for future in as_completed([task[0] for task in tasks], timeout=20):
                    # Znajdź które zadanie się ukończyło
                    for task_future, func_num, func_name in tasks:
                        if task_future == future:
                            try:
                                elapsed = future.result()
                                if elapsed is not None:
                                    results[func_num] = elapsed
                                    print(f"{i} {func_name}: {elapsed:.2f}s")
                                else:
                                    print(f"{i} {func_name}: ERROR")
                                completed_count += 1
                                break
                            except Exception as e:
                                print(f"{i} {func_name}: EXCEPTION - {e}")
                                completed_count += 1
                                break
                                
            except TimeoutError:
                print(f"{i}: TIMEOUT po 20s - ukończono {completed_count}/3 funkcji")
                
                # Sprawdź które zadania się już ukończyły
                for task_future, func_num, func_name in tasks:
                    if task_future.done() and results[func_num] is None:
                        try:
                            elapsed = task_future.result(timeout=0.1)  # Bardzo krótki timeout
                            if elapsed is not None:
                                results[func_num] = elapsed
                                print(f"{i} {func_name}: {elapsed:.2f}s (ukończone przed timeout)")
                        except:
                            print(f"{i} {func_name}: TIMEOUT lub ERROR")
                    elif not task_future.done():
                        print(f"{i} {func_name}: TIMEOUT - nie ukończone")
            
            # Dodaj wyniki do list (tylko udane)
            if results[1] is not None:
                wynik1.append(results[1])
            if results[2] is not None:
                wynik2.append(results[2])
            if results[3] is not None:
                wynik3.append(results[3])
            
            print(f"Planszy {i} - ukończone: f1={results[1] is not None}, f2={results[2] is not None}, f3={results[3] is not None}")

    print(f"\n=== PODSUMOWANIE ===")
    print(f"Sumy czasów: {sum(wynik1):.2f}s, {sum(wynik2):.2f}s, {sum(wynik3):.2f}s")
    print(f"Liczba ukończonych: {len(wynik1)}, {len(wynik2)}, {len(wynik3)}")
    print(f"Średnie czasy: {sum(wynik1)/len(wynik1) if wynik1 else 0:.2f}s, {sum(wynik2)/len(wynik2) if wynik2 else 0:.2f}s, {sum(wynik3)/len(wynik3) if wynik3 else 0:.2f}s")