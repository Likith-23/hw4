s = str(input("ENTER A WORD..."))
def print_substrings(s):
    n = len(s) 
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])
print("ALL POSSIBLE SUBSTRINGS FOR THIS WORD ARE...", print_substrings(s))
