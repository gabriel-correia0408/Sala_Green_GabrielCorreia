#criando função de nome soma
def soma(x,y):
    """
    soma x e y
    >>> soma(20,20)
    40

    >>> soma(-10,50)
    40

    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x,(int,float)), 'x precisa ser int ou float'
    assert  isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
