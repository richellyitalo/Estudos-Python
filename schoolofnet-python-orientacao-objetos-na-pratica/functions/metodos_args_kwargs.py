def metodo_simples(*args, **kwargs):
    print(type(args))

    print(type(kwargs))

    for p in args:
        print(p)

    for q in kwargs:
        print('%s = %s' % (q, kwargs[q]))

