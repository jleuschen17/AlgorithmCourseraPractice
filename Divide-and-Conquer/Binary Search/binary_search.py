# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query, final_position, checker):
    checker_position = len(keys) // 2
    checker_value = keys[checker_position]
    #print('Query:', query)
    #print('Checker Position:', checker_position)
    #print('Checker Value:', checker_value)
    #print('Final Position:', final_position)
    if query == checker_value:
        if len(keys) <= 2 and checker == 1:
            final_position += 1
        return final_position
    elif len(keys) <= 1 or len(keys) <= 2 and query > checker_value:
        return -1
    elif query > checker_value:
        keys = keys[checker_position + 1:]
        final_position += len(keys) // 2 + 1
        return binary_search(keys, query, final_position, checker)
    elif query < checker_value:
        keys = keys[:checker_position]
        if len(keys) == 2:
            checker = 1
        final_position -= len(keys) // 2 + 1
        return binary_search(keys, query, final_position, checker)



if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    final_position = len(input_keys) // 2
    checker = 0
    for q in input_queries:
        print(binary_search(input_keys, q, final_position, checker), end=' ')
