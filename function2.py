# This function is sourced from https://github.com/TheAlgorithms/Python/blob/master/strings/camel_case_to_snake_case.py
# Only chnages are made to the docstring
# Contracts are added where applicable

def camel_to_snake_case(input_str:str) -> str:
    """
    Transforms a camelCase (or PascalCase) string to snake_case

    >>> camel_to_snake_case("someRandomString")
    'some_random_string'

    >>> camel_to_snake_case("SomeRandomStr#ng")
    'some_random_str_ng'

    >>> camel_to_snake_case("123someRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case("123SomeRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    """
    '''
    
    Preconditions
    '''
    assert(isinstance(input_str,str)), "Precondition: input_str must be a string"
    assert(input_str.isascii()), "Precondition: ASCII only, because ⓐ is accepted but throws an error"
    assert(len(input_str)>0), "Precondition: The length of the input_str must be greater than zero"

    # check for invalid input type
    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    snake_str = ""

    for index, char in enumerate(input_str):
        '''
        Loop invariant
        '''
        assert(all(index + 1) <= len(snake_str) <= 2 * (index + 1) for index,char in enumerate(input_str)), "Loop Variant: snake_str should match how many characters have been processed."
        
        if char.isupper():
            snake_str += "_" + char.lower()

        # if char is lowercase but proceeded by a digit:
        elif input_str[index - 1].isdigit() and char.islower():
            snake_str += "_" + char

        # if char is a digit proceeded by a letter:
        elif input_str[index - 1].isalpha() and char.isnumeric():
            snake_str += "_" + char.lower()

        # if char is not alphanumeric:
        elif not char.isalnum():
            snake_str += "_"

        else:
            snake_str += char
        '''
        Loop invariant
        '''
        assert all(not c.isupper() for c in snake_str if c.isalpha()), "Loop Variant: All letters processed so far must be lowercase in snake_str."

    # remove leading underscore
    if snake_str[0] == "_":
        snake_str = snake_str[1:]

    '''
    Post Conditions
    '''
    assert(isinstance(snake_str,str)), "Post Condition: Return value must be a string"
    assert(len(snake_str)>0), "Post Condition: The length of return value must be greater than 0"

    return snake_str