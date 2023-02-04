def concatenate(*args, **kwargs):
    text_from_the_args = ''.join(args)

    for k in kwargs.keys():
        if k in text_from_the_args:
            text_from_the_args = text_from_the_args.replace(k, kwargs[k])

    return text_from_the_args


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))