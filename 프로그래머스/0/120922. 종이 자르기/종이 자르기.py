def solution(M, N):
    return (M - 1) + (M) * (N - 1) if M > N else (N - 1) + (N) * (M - 1)