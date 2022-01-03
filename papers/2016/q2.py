from collections import defaultdict


def coordinate_of_sequence(sequence):
    y = 4 - ((sequence - 1) // 5)
    x = (sequence - 1) % 5

    return x, y


def solve(position, sequence_values, steps):
    state = defaultdict(int)
    sequence_index = 0

    for _ in range(steps):
        new_state = state.copy()

        x, y = coordinate_of_sequence(position)

        new_count = state[x, y] + 1
        new_state[x, y] = new_count

        worklist = [(x, y)]

        while len(worklist) > 0:
            x, y = worklist.pop()

            if new_state[x, y] >= 4:
                new_state[x, y] -= 4
                for dx in (-1, 1):
                    new_state[x + dx, y] += 1
                    worklist.append((x + dx, y))
                for dy in (-1, 1):
                    new_state[x, y + dy] += 1
                    worklist.append((x, y + dy))

        position += sequence_values[sequence_index]

        if position > 25:
            position -= 25

        sequence_index = (sequence_index + 1) % len(sequence_values)
        state = new_state

    return state


def format_solution(solution, sep=' '):
    lines = []
    for y in range(5):
        y = 4 - y
        lines.append(
            sep.join(str(solution[x, y] if (x, y) in solution else 0) for x in range(5))
        )

    return "\n".join(lines)


position, _, steps = tuple(int(x) for x in input().split())
sequence_values = [int(x) for x in input().split()]
solution = solve(position, sequence_values, steps)
print(format_solution(solution))