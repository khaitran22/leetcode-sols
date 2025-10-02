# %%
def longestPalindrome(s):
    def is_palindrome(sub_s):
        rev = ""
        for char in sub_s:
            rev = char + rev
        return True if sub_s == rev else False

    if len(s) == 1 or is_palindrome(s):
        return s
    
    longest_palindrome = s[0]

    for i in range(1, len(s)):
        sub_ss = s[:i+1]
        str_to_check = [sub_ss[j:] for j in range(1, len(sub_ss))]
        for sub_s in reversed(str_to_check):
            if len(sub_s) <= len(longest_palindrome):
                continue
            if is_palindrome(sub_s):
                longest_palindrome = sub_s if len(sub_s) > len(longest_palindrome) else longest_palindrome
        
        third_substring = s[:i+1]
        if is_palindrome(third_substring):
            longest_palindrome = longest_palindrome if len(longest_palindrome) >= len(third_substring) else third_substring
    
    return longest_palindrome

s = 'ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy'
# assert longestPalindrome(s) == 'cdc'
longestPalindrome(s)

# %%
'aa'.split('')
