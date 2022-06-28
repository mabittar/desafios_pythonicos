

def count_string(s: list, t: list):
    response = []
    for i, seq in enumerate(t):
        result = [s.count(q) for q in seq.split()]
        out = "YES" if any(result) <= 4 else "NO"
        response.append(out)
    
    
    return response


if __name__ == '__main__':
    s = ['aabaab', 'aaaaabb']
    t = ['bbabbc', 'abb']

    count_string(s=s, t=t)
