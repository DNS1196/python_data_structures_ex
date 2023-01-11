def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq_count(str(num1)) == freq_count(str(num2))

def freq_count(thing):
    counts = {}
    for x in thing:
        counts[x] = counts.get(x, 0) + 1 
    return counts