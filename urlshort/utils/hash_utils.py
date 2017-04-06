def shorturl_from_id(n):
    m = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    s = ""

    while n:
        s += m[int(n%62)]
        n = int(n / 62)

    return s[::-1]


def shorturl_to_id(short_url):
    id = 0

    for c in short_url:
        if 'a' <= c <= 'z':
          id = id*62 + ord(c) - ord('a')
        if 'A' <= c <= 'Z':
          id = id*62 + ord(c) - ord('A') + 26
        if '0' <= c <= '9':
          id = id*62 + ord(c) - ord('0') + 52

    return id