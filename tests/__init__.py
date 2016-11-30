from random import randint, choice
import string


def random_string(length=randint(4, 10),
                  chars=string.ascii_uppercase + string.digits):
    """
    Generates a random text string containing ascii characters and/or numbers.
    :param length:
    :param chars:
    :return:
    """
    return ''.join(choice(chars) for _ in range(length))


def random_number(min_number=125, max_number=99999999):
    """
    Wrapper for randint with default arguments, so it can be used inside loops
    for generating lists or dicts.
    :param min_number:
    :param max_number:
    :return:
    """
    return randint(min_number, max_number)


def random_list(length=randint(4, 10), data_types=str):
    """
    Generate a random list of any data type.
    :param length:
    :param data_types:
    :return:
    """
    generated_list = []
    if isinstance(data_types, str):
        append_value = random_string
    else:
        append_value = random_number

    for i in range(0, length):
        generated_list.append(append_value())

    return generated_list


def random_dict(length=randint(3, 8)):
    """
    Generate a dictionary with random keys and values.
    :param length:
    :return:
    """
    generated_dict = {}
    for i in range(0, length):
        generated_dict[random_string()] = random_string()
    return generated_dict


data_dict = {
    'str': random_string(),
    'int': random_number(),
    'list': random_list(),
    'dict': random_dict(),
}
