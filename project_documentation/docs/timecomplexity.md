# Time Complexity

---

The time complexity of minimax for draughts (checkers) on an 8x8 board is O(b^d), where:

- b = branching factor (average number of legal moves per position)
- d = depth of the search tree

---

### Branching factor 

Approximately 2-8 moves per position on average, though this varies significantly:

Early game: higher (around 7-10 moves)
Mid game: moderate (around 3-7 moves)
End game: lower (around 2-4 moves)
Jump sequences can temporarily reduce branches

---

### Search depth 

The search depth in this implementation is 3 due to the number of branches needed to be checked.

---