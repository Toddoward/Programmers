def solution(score):
    sums = [sum(s) for s in score]
    ranks = {s: i + 1 for i, s in enumerate(sorted(sums, reverse=True))}
    
    sorted_sums = sorted(sums, reverse=True)
    ranks = {s: sorted_sums.index(s) + 1 for s in set(sums)} 
    
    return [ranks[s] for s in sums]