from util import Stack


def earliest_ancestor(ancestors, starting_node):
    earliest = -1
    relatives = Stack()
    met = set()

    for pair in ancestors:
        if pair[1] == starting_node:
            if pair not in met:
                relatives.push(pair)

    while relatives.stack:
        current_pair = relatives.pop()
        earliest = current_pair[0]
        for pair in ancestors:
            if pair not in met:
                if pair[1] == earliest:
                    relatives.push(pair)
                    met.add(pair)
    return earliest
