import hashlib, json

def crypto_hash(*args):
    """
    Return a SHA-256 hash of given data
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 'two', 'three'): {crypto_hash('one', 'two', 'three')}")

if __name__ == '__main__':
    main()
