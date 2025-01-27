class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def password_too_common(pwd, specials):
    only_digit = pwd.isdigit()
    only_let = pwd.isalpha()
    only_spec = all(w in specials for w in pwd)
    return only_digit or only_let or only_spec

special_ch = {"@", "*", "&", "%"}
while True:
    passw = input()
    if passw == "Done":
        break
    if len(passw) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if password_too_common(passw, special_ch):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not any(c in special_ch for c in passw):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    if ' ' in passw:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")