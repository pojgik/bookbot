def get_word_count(contents):
    return len(contents.split())

def count_characters(contents):
    contents = contents.lower()
    counts = {}
    for c in contents:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

def sort_chars(counts):
    sorted_counts = []
    for count in counts:
        char_count = {'char': count, 'num': counts[count]}
        sorted_counts.append(char_count)
    sorted_counts.sort(reverse=True, key=lambda x: x['num'])
    return sorted_counts