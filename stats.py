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