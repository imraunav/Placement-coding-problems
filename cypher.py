def foo(s):
    longest = 0
    running_len = 0
    subs_len = 0
    caps_flag = False
    numbers = '1234567890'
    caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for ch in s:
        if ch in numbers: # if number reset substring tracing
            caps_flag = False
            running_len = 0
            subs_len = 0
        else:
            running_len += 1
        
        if ch in caps: # if found Caps, treat as valid substring
            caps_flag = True

        if caps_flag == True: # is a valid substring
            subs_len = running_len
        longest = max(longest, subs_len)
    if longest == 0:
        return -1
    else:
        return longest

# driver code
if __name__ == "__main__":
    s = input()
    print(foo(s))




        