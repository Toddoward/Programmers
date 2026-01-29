def solution(rank, attendance):
    answer = sorted([rank[i] for i in range(len(rank)) if attendance[i]])[:3]
    return rank.index(answer[0]) * 10 ** 4 + rank.index(answer[1]) * 10 ** 2 + rank.index(answer[2])