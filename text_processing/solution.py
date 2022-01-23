def solution(word, string):
    while word in string:
        string = string.replace(word, "")
    return string


if __name__ == "__main__":
    word = input()
    string = input()
    print(solution(word, string))