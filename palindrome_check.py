def check_palindrome(s):
    '''
    string does not contain spaces and special char or num
    if string is a palindrome return true
    '''

    return s == s[::-1]
