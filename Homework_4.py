# ------------------------------ UNIQUE EMAIL ADDRESSES ------------------------------

def unique_emails(list_of_emails):
    final_uniques = set()
    for i in list_of_emails:
        first_part, domain = i.split('@')
        before_plus = first_part.split('+')[0]
        before_dot, *after_dot = before_plus.split('.')
        email = ''.join([before_dot, *after_dot, '@', domain])
        final_uniques.add(email)
    return final_uniques


input_emails = input()
list_of_emails = input_emails.split()
# list_of_emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(len(unique_emails(list_of_emails)))

# -------------------------------------UAM---------------------------------------------

def users_distinct(logs):
    users_dict = {}
    for el in logs:
        user_id, minute = el
        if user_id not in users_dict:
            users_dict[user_id] = set()
        users_dict[user_id].add(minute)
    return users_dict


def count_of_UAM(dictionary, num):
    answers = [0] * num
    for key, values in dictionary.items():
        answers[len(values)-1] += 1
    return answers


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k = 5

dictionary = users_distinct(logs)
print(count_of_UAM(dictionary, k))

# ------------------------------------FIND AND REPLACE PATTERN --------------------------------------


def convert_string(string):
    arr = {}
    for i, n in enumerate(string):
        if n not in arr:
            arr[n] = []
        arr[n].append(i)
    return list(arr.values())

def find_replace_pattern(list_strings, pattern):
    final_list = []
    for i in list_strings:
        if convert_string(i) == convert_string(pattern):
            final_list.append(i)
    return final_list

ls = ["abc","deq","mee","aqq","dkd","ccc"]
print('Here is the list ---> ', ls)
pattern = input('Write the pattern: ')
print(find_replace_pattern(ls, pattern))



# --------------------------------JEWELS AND STONES--------------------------------


def counts(jewels, stones):
    count = 0
    for i in stones:
        if i in jewels:
            count += 1
    return count

jewels = input('Jewels: ')
stones = input('Stones: ')
print(counts(jewels, stones))


# -------------------------BEAUTIFUL BINARY STRING ------------------------------
def beautify(pat):
    min_pat = '010'
    count = 0
    while min_pat in pat:
        indice = pat.index(min_pat)
        ls_pat = list(pat)
        if ls_pat[indice-1] == '1':
            ls_pat[indice] = '1'
        elif ls_pat[indice+3] == '1':
            ls_pat[indice+2] = '1'
        else:
            ls_pat[indice+1] = '0'
        count += 1
        pat = ''.join(ls_pat)
    return pat, count

pat = (input('Write the pattern: '))
print(beautify(pat))

#-----------------------------------STRING POWER---------------------------------

def find_repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]
        if substring * (len(string) // len(substring)) + (substring[:len(string) % len(substring)]) == string:
            return substring
    return string

def substract(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def string_power(string, power):
    rep = find_repeats(string)
    if power < 0:
        repet = (power * -1) - 1
        for i in range(0, repet):
            string = substract(string, rep)
            if string == "":
                return "undefined"
    elif power >= 0:
        string = string * power
    return string

string = 'abcabcabc'
k = -2
print(string_power(string, k))

