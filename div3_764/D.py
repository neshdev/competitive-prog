"""
https://codeforces.com/contest/1624/problem/D

"""

from collections import Counter

def shortest(n,k,s):
    """
    greedy method.
    Need to make k strings.
    String has to be palindrome.
    String can be even or odd
    if odd, middle can be any character.

    What about color and swapping?. This just lets us know that we can color a character to swap them and basically construct any string that we want.
    A color can be given to any char.
    for ex:
        aaaaa
        k=3
        112233

        Same 'a' can have different colors.

    Greedily put pairs in each bucket. Find if we can put 1 extra character in every bucket. (making it odd)

    Note: it doesn't matter how you distribute the strings. (You don't even need to make the string, but illustrations are for visual understanding)

    Ex2:

        aaaaaa
        k = 3
        counter = { 6 : 'a' }

        We need k=3 strings

        s1: __
        s2: __
        s3: __

        Distribute each pair into bucket as evenly as possible. This is same as dividing by k

        s1: aa
        s2: aa
        s3: aa

        so ans = min(len(s1),len(s2),len(s3)) = 2

    Ex6:
        abcabcabcac
        k = 2
        counter = {
            a : 4
            b : 3
            c : 4
        }

        pairs = (2,'a'), (1, 'b'), (2, 'c')
        rem = (1,'b')

        we need k=2 strings:
        s1: ___
        s2: ___

        Distribute each pair into bucket as evenly as possible. This is same as dividing by k. 5 // 2 = 2 pairs

        So far, we have:
        s1: ab_ba
        s2: ca_ac

        we still have 1 pair remaining and other remaining chars. pairs = (1,a), rem: (1,b) so in total (a,a,b)
        we can apply these chars in the middle and extend the string. If we can give 1 char to every bucket, then we can extend the length of the string by 1
        
        So, we need to take 5 % 2, the remaining chars and add it our remainder.
        rem = (pairs % k) * 2 + rem
        if   rem >= k then we can give 1 char to every bucket, extending our answer
        else the smallest string is already found

        Applying what we have:

        s1: ababa
        s2: cabac

        So the ans=min(len(s1),len(s2)) = 5

    """
    freq = Counter(s)
    pairs = 0
    rem = 0
    for key,val in freq.items():
        q,r = divmod(val,2)
        if q:
            pairs += q
        if r:
            rem += r

    ans = 2 * (pairs // k)
    rem += 2 * (pairs % k)
    if rem >= k:
        ans += 1
    return ans

t = int(input())
for _ in range(t):
    n,k = [int(x) for x in  input().split()]
    s = input()
    ans = shortest(n,k,s)
    print(ans)


