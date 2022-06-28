


def count_string(s: list, t: list):
    response = []
    for i, seq in enumerate(t):
        result = {}
        counter = [c for c in seq]
        search = [c for c in s[i]]
        for c in search:
            result[c] = counter.count(c)
            print(result)

        out = "YES" if any(result.values()) <= 4 else "NO"
        response.append(out)
    

    

if __name__ == '__main__':
    s = ['aabaab', 'aaaaabb']
    t = ['bbabbc', 'abb']
    
    count_string(s=s, t=t)
    