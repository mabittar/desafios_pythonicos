from collections import Counter


def count_string(s: list, t: list):
    response = []
    for i, seq in enumerate(t):
        target = Counter([c for c in seq])
        search = [c for c in s[i]]
        for letter in search:
            out = "YES" if target[letter] <= 4 or target[letter] != 0 else "NO"

        response.append(out)
        
    print(response)    

if __name__ == '__main__':
    s = ['aabaab', 'aaaaabb']
    t = ['bbabbc', 'abb']
    
    count_string(s=s, t=t)
    