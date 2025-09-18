#Task 2:
def remove_special_characters(text):
    result = ""
    for ch in text:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch == " ":
            result += ch
    return result

user_text = input("Enter a string: ")
cleaned_text = remove_special_characters(user_text)

print("Cleaned string:", cleaned_text)

#Task 3
user_text = input("Enter a string: ")
char_list = list(user_text)

n = len(char_list)
for i in range(n):
    for j in range(0, n-i-1):
        if ord(char_list[j]) > ord(char_list[j+1]):
            char_list[j], char_list[j+1] = char_list[j+1], char_list[j]

sorted_text = ascii(char_list)
print("Sorted string by ASCII using Bubble Sort:", sorted_text)

#Task 1:
def card_check(num):
    last = int(num[-1])
    
    vals = [int(i) for i in num[:-1]]
    
    # double even index and adjust if > 9
    for j in range(len(vals)):
        if j % 2 == 0:
            vals[j] *= 2
            if vals[j] > 9:
                vals[j] -= 9
    
    # sum + last digit
    total = sum(vals) + last
    
    # check valid or not
    if total % 10 == 0:
        return "Valid"
    else:
        return "Invalid"

print(card_check("4532015112830366"))

