# %%
def reportSpam(message, bannedWords) -> bool:
    bannedWords = set(bannedWords)
    count = 0
    for t in message:
        if t in bannedWords:
            count += 1
            if count >= 2:
                return True
    return False

message = ["hello","world","leetcode"]
bannedWords = ["world","hello"]
reportSpam(message, bannedWords)
# %%
