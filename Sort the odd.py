def sort_array(source_array: list[int]) -> list[int]:
    eq = [x for x in source_array if x % 2 == 1]

    for k, i in enumerate(source_array):
        if i % 2 == 1:
            source_array[k] = min(eq)
            del eq[eq.index(min(eq))]

    return source_array

