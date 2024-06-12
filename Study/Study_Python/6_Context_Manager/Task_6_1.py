def find(file, key):
    passwords_set = set()

    def get_password(dct):
        if key in dct:
            value = dct.get(key)
            passwords_set.update(value) if isintance(value, list) else passwords_set.add(value)

    with open(file, 'r') as f:
        json.load(f, object_hook = get_password)

    return list(passwords_set)
