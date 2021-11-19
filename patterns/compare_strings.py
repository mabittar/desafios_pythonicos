import difflib

a = "3290100010000002"
b = "3290100010000000"
diff_list = [li for li in difflib.ndiff(a, b) if li[0] != ' ']
print(diff_list)