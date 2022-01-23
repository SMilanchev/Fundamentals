def get_digits(string):
    return "".join([c for c in string if c.isdigit()])


def get_punctuation(string):
    return "".join([m for m in string if not m.isalnum()])


def get_alpha_characters(string):
    return "".join([m for m in string if m.isalpha()])


def solution(string):
    print(get_digits(string))
    print(get_alpha_characters(string))
    print(get_punctuation(string))


if __name__ == "__main__":
    solution(input())