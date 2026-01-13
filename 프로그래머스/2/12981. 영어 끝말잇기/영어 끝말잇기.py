def solution(n, words):
    answer = [0 , 0]
    used_words = [words[0]]

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:
            if (i + 1) % n == 0:
                answer = [n, (i + 1) // n]
            else:
                answer = [(i + 1) % n, (i + 1) // n + 1]
            break
            
        if words[i] in used_words:
            if (i + 1) % n == 0:
                answer = [n, (i + 1) // n]
            else:
                answer = [(i + 1) % n, (i + 1) // n + 1]
            break
        used_words.append(words[i])

    return answer