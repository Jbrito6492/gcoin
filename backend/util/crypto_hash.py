import hashlib, json

def crypto_hash(*args):
    """
    Return a SHA-256 hash of given data
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    # print(f'stringified_args: {stringified_args}')
    joined_data = ''.join(stringified_args)
    # print(f'joined_data: {joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 'two', 'three'): {crypto_hash('one', 'two', 'three')}")

if __name__ == '__main__':
    main()
