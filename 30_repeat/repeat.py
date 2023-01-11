def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    rep_phrase = []
    if num == 0:
        return ''
    
    elif not isinstance(num, int):
        return 

    elif num in range(1,num +1):
        while num > 0:
            rep_phrase.append(phrase)
            num -= 1
        return ''.join(rep_phrase)

      
    
