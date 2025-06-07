def chess_board(n):
    """Generates a chessboard pattern of size n x n."""
    return [[0 for j in range(n)] for i in range(n)]

def is_safe(board, row, col):
    """Sprawdza czy można postawić hetmana na pozycji (row, col)"""
    n = len(board)
    
    # Sprawdź kolumnę
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Sprawdź główną przekątną
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Sprawdź anty-przekątną
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row=0):
    """Znajduje wszystkie rozwiązania N-hetmanów"""
    n = len(board)
    if row == n:
        return [board]
    
    solutions = []
    for col in range(n):
        if is_safe(board, row, col):
            new_board = [row[:] for row in board]
            new_board[row][col] = 1
            solutions.extend(solve_n_queens(new_board, row + 1))
    
    return solutions

def board_to_tuple(board):
    """Konwertuje planszę na tuple"""
    return tuple(tuple(row) for row in board)

def rotate_90(board):
    """Obrót o 90 stopni w prawo"""
    n = len(board)
    return [[board[n-1-j][i] for j in range(n)] for i in range(n)]

def flip_horizontal(board):
    """Odbicie poziome (lewo-prawo)"""
    return [row[::-1] for row in board]

def flip_vertical(board):
    """Odbicie pionowe (góra-dół)"""
    return board[::-1]

def get_all_symmetries(board):
    """Zwraca wszystkie 8 symetrycznych wersji planszy"""
    symmetries = []
    current = board
    
    # 4 obroty
    for _ in range(4):
        symmetries.append(current)
        current = rotate_90(current)
    
    # Odbicie poziome + 4 obroty
    current = flip_horizontal(board)
    for _ in range(4):
        symmetries.append(current)
        current = rotate_90(current)
    
    return symmetries

def count_unique_symmetries(board):
    """Liczy ile unikalnych symetrii ma dana plansza"""
    original = board_to_tuple(board)
    symmetries = get_all_symmetries(board)
    unique_symmetries = set()
    
    for sym in symmetries:
        unique_symmetries.add(board_to_tuple(sym))
    
    return len(unique_symmetries)

def analyze_auto_symmetries(board):
    """Analizuje jakie auto-symetrie ma dana plansza"""
    original = board_to_tuple(board)
    auto_symmetries = []
    
    # Sprawdz rozne przeksztalcenia
    if board_to_tuple(rotate_90(board)) == original:
        auto_symmetries.append("obrot o 90 stopni")
    if board_to_tuple(rotate_90(rotate_90(board))) == original:
        auto_symmetries.append("obrot o 180 stopni")
    if board_to_tuple(rotate_90(rotate_90(rotate_90(board)))) == original:
        auto_symmetries.append("obrot o 270 stopni")
    if board_to_tuple(flip_horizontal(board)) == original:
        auto_symmetries.append("odbicie poziome")
    if board_to_tuple(flip_vertical(board)) == original:
        auto_symmetries.append("odbicie pionowe")
    
    # Sprawdz odbicia przekatnych
    def flip_main_diag(board):
        n = len(board)
        return [[board[j][i] for j in range(n)] for i in range(n)]
    
    def flip_anti_diag(board):
        n = len(board)
        return [[board[n-1-j][n-1-i] for j in range(n)] for i in range(n)]
    
    if board_to_tuple(flip_main_diag(board)) == original:
        auto_symmetries.append("odbicie wzgledem glownej przekatnej")
    if board_to_tuple(flip_anti_diag(board)) == original:
        auto_symmetries.append("odbicie wzgledem anty-przekatnej")
    
    return auto_symmetries

def print_board(board):
    """Wyświetla planszę czytelnie"""
    n = len(board)
    print("  " + " ".join(str(i) for i in range(n)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join("Q" if cell == 1 else "." for cell in row))

def find_max_symmetric_solutions(max_n=10):
    """Szuka rozwiązań z maksymalnymi auto-symetriami dla różnych rozmiarów"""
    print("=== SZUKANIE ROZWIĄZAŃ Z MAKSYMALNYMI AUTO-SYMETRIAMI ===\n")
    
    for n in range(1, max_n + 1):
        print(f"Szachownica {n}x{n}:")
        solutions = solve_n_queens(chess_board(n))
        
        if not solutions:
            print("  Brak rozwiązań\n")
            continue
        
        print(f"  Łącznie rozwiązań: {len(solutions)}")
        
        # Znajdź rozwiązania z najmniejszą liczbą unikalnych symetrii
        min_symmetries = float('inf')
        most_symmetric = []
        
        for sol in solutions:
            unique_count = count_unique_symmetries(sol)
            if unique_count < min_symmetries:
                min_symmetries = unique_count
                most_symmetric = [sol]
            elif unique_count == min_symmetries:
                most_symmetric.append(sol)
        
        print(f"  Maksymalne auto-symetrie: {min_symmetries} unikalnych wersji")
        
        if min_symmetries == 1:
            print("  *** ZNALEZIONO ROZWIAZANIE Z 1 WERSJA! ***")
            sol = most_symmetric[0]
            auto_syms = analyze_auto_symmetries(sol)
            print(f"  Auto-symetrie: {', '.join(auto_syms) if auto_syms else 'brak'}")
            print("  Plansza:")
            print_board(sol)
            
            print("\n  Sprawdzenie wszystkich 8 przeksztalcen:")
            symmetries = get_all_symmetries(sol)
            original_tuple = board_to_tuple(sol)
            for i, sym in enumerate(symmetries):
                is_same = board_to_tuple(sym) == original_tuple
                names = ["oryginal", "obrot 90", "obrot 180", "obrot 270", 
                        "odbicie poziome", "odbicie poziome + 90", 
                        "odbicie poziome + 180", "odbicie poziome + 270"]
                print(f"    {names[i]}: {'identyczne' if is_same else 'rozne'}")
        
        elif min_symmetries <= 4:
            print(f"  Rozwiazanie z {min_symmetries} wersjami:")
            sol = most_symmetric[0]
            auto_syms = analyze_auto_symmetries(sol)
            print(f"  Auto-symetrie: {', '.join(auto_syms) if auto_syms else 'brak'}")
            print_board(sol)
        
        print()

# Uruchomienie analizy
find_max_symmetric_solutions(8)

# Specjalne przypadki
print("\n=== SPECJALNE PRZYPADKI ===")

# 1x1 - trywialny przypadek
print("1x1 - trywialny przypadek (1 hetman, 1 pole):")
board_1x1 = [[1]]
print_board(board_1x1)
print(f"Unikalne symetrie: {count_unique_symmetries(board_1x1)}")
auto_syms = analyze_auto_symmetries(board_1x1)
print(f"Auto-symetrie: {', '.join(auto_syms) if auto_syms else 'brak'}")

print("\n" + "="*50)
print("UWAGI:")
print("• Rozwiazania z 1 wersja sa bardzo rzadkie")
print("• Wymagaja maksymalnych auto-symetrii")
print("• Najczesciej wystepuja dla malych szachownic")
print("• Dla n>=4 wiekszosc rozwiazan ma 8 lub 4 wersje")