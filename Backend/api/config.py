PASSWORD_CONFIG = {
    'MIN_LENGTH': 10,
    'REQUIRE_UPPERCASE': True,
    'REQUIRE_LOWERCASE': True,
    'REQUIRE_NUMBERS': True,
    'REQUIRE_SPECIAL_CHARS': True,
    'PASSWORD_HISTORY_COUNT': 3,
    'MAX_LOGIN_ATTEMPTS': 3,
    'LOCKOUT_DURATION': 30,  # minutes
    'COMMON_PASSWORDS_FILE': 'common_passwords.txt'
}