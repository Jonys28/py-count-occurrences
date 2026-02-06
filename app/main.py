def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count = 0
    phras = phrase.lower()
    for i in range(len(phras)-1):
        if phras[i] == phras[i+1]:
            l = phras[i]
            count += 1
    return f"The letter {l} is {count} keer in phrase"
            
