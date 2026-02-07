def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count = 0
    phras = phrase.lower()
    for i in phras:
        if i == letter:
            count += 1
    return count
            
