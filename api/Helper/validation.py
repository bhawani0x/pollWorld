import re


class Validation:
    @staticmethod
    def is_valid_email(email):
        if not email:
            return False
        elif len(email) > 320:
            return False
        elif not (re.match(
                '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$',
                email)):
            return False
        else:
            return True
