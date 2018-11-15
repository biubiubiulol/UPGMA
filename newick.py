

def list_to_newick(base_list):
    newick = "("
    for i in range(len(base_list) - 1):
        if isinstance(base_list[i], str):
            newick += (base_list[i] + ',')
        else:
            newick += (list_to_newick(base_list[i]) + ',')
    if isinstance(base_list[len(base_list) - 1], str):
        newick += base_list[len(base_list) - 1]
    else:
        newick += list_to_newick(base_list[len(base_list) - 1])

    newick += ")"

    return newick

if __name__ == "__main__":
    sample_list = ['B', ['A', 'C'], 'D', ['G', ['H', 'J'], 'I']]
    print(list_to_newick(sample_list))

    sample_list2 = ['B', ['A', 'C'], 'D']
    print(list_to_newick(sample_list2))
