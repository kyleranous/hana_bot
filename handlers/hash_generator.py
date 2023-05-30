"""
Generates Hashes for a given string
"""
import hashlib


def sha256_hash(string):
    """
    Generates a sha256 hash for a given string
    :param string: string to be hashed
    :return: sha256 hash
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def md5_hash(string):
    """
    Generates a md5 hash for a given string
    :param string: string to be hashed
    :return: md5 hash
    """
    return hashlib.md5(string.encode('utf-8')).hexdigest()