
def earliest_ancestor(ancestors, starting_node):
    parents = {}

    for parent, child in ancestors:
        if child not in parents:
            parents[child] = [parent]
        else:
            parents[child].append(parent)

    if starting_node not in parents:
        return -1

    curr_ancestors = parents[starting_node]
    print(parents)

    while True:
        new_ancestors = []
        for ancestor in curr_ancestors:
            if ancestor in parents:
                new_ancestors = new_ancestors + parents[ancestor]
            
        if len(new_ancestors) == 0:
            return curr_ancestors[0]
        else:
            curr_ancestors = new_ancestors
            

print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))