def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
x=int(input())
for _ in range(x):
    s=input().lower()
    vowels="aioue"
    Check_Vow(s,vowels)
