"""
Contains functions that convert database ID to and from a base62 ID containing
alphabets and numbers

ref: http://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/
"""

def shorturl_from_id(n):
    """
    Generate a short code given an integer. Integer is DB key

    :param n: Integer key that associated with URL
    :return: Short code for a given integer
    """

    m = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    s = ""

    while n:
        s += m[int(n%62)]
        n = int(n / 62)

    return s[::-1]


def shorturl_to_id(short_url):
    """
    Converts the code to corresponding internal database id

    :param short_url: URL code
    :return: Returns id previously generated
    """
    id = 0

    for c in short_url:
        if 'a' <= c <= 'z':
          id = id*62 + ord(c) - ord('a')
        if 'A' <= c <= 'Z':
          id = id*62 + ord(c) - ord('A') + 26
        if '0' <= c <= '9':
          id = id*62 + ord(c) - ord('0') + 52

    return id