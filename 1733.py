def minimumTeachings(n, languages, friendships) -> int:
    languages = [set(l) for l in languages]
    non_common_frs = []

    for frs in friendships:
        l, r = frs
        if len(languages[l-1].intersection(languages[r-1])) == 0:
            non_common_frs.append(frs)

    if len(non_common_frs) == 0:
        return 0

    non_speak_l = {}
    min_ppl = 10000000
    for lang in range(n):
        non_speak_l[lang] = set([])
        for l, r in non_common_frs:
            lang_l, lang_r = languages[l-1], languages[r-1]
            if lang+1 not in lang_l:
                non_speak_l[lang].add(l)
            if lang+1 not in lang_r:
                non_speak_l[lang].add(r)
        min_ppl = min(min_ppl, len(non_speak_l[lang]))
    return min_ppl


# n = 2
# languages = [[1], [2], [1, 2]]
# friendships = [[1, 2], [1, 3], [2, 3]]
# n = 5
# languages = [[1], [5], [1, 5], [5]]
# friendships = [[1, 2], [1, 3], [1, 4], [2, 3]]
# n = 11
# languages = [[3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6], [5, 10, 6, 4, 8, 7], [6, 11, 7, 9], [11, 10, 4], [6, 2, 8, 4, 3], [
#     9, 2, 8, 4, 6, 1, 5, 7, 3, 10], [7, 5, 11, 1, 3, 4], [3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9], [8, 6, 10, 2, 3, 1, 11, 5], [5, 11, 6, 4, 2]]
# friendships = [[7, 9], [3, 7], [3, 4], [2, 9], [1, 8], [5, 9], [8, 9], [6, 9], [3, 5], [4, 5], [4, 9], [3, 6], [1, 7], [
#     1, 3], [2, 8], [2, 6], [5, 7], [4, 6], [5, 8], [5, 6], [2, 7], [4, 8], [3, 8], [6, 8], [2, 5], [1, 4], [1, 9], [1, 6], [6, 7]]
# n = 17
# languages = [[4, 7, 2, 14, 6], [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9], [16], [10], [10, 3], [4, 12, 8, 1, 16, 5, 15, 17, 13], [4, 13, 15, 8, 17, 3, 6, 14, 5, 10], [
#     11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12], [4, 14, 6], [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6], [14], [7, 14], [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4]]
# friendships = [[4, 11], [3, 5], [7, 10], [10, 12], [5, 7], [4, 5], [3, 8], [1, 5], [1, 6], [7, 8], [4, 12], [2, 4], [8, 9], [3, 10], [4, 7], [5, 12], [
#     4, 9], [1, 4], [2, 8], [1, 2], [3, 4], [5, 10], [2, 7], [1, 7], [1, 8], [8, 10], [1, 9], [1, 10], [6, 7], [3, 7], [8, 12], [7, 9], [9, 11], [2, 5], [2, 3]]
# print(minimumTeachings(n, languages, friendships))
