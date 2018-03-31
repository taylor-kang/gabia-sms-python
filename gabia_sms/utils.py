import random
import string


def get_nonce():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


def escape_xml_string(value):
    return value.replace('&', '&amp') \
        .replace('<', '&lt') \
        .replace('>', '&gt') \
        .replace("'", '&apos') \
        .replace('"', '&quot')
