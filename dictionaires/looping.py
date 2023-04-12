a_dict = {"key1": "value1", "key2": "value2"}

for key in a_dict:
    print(key)

for key in a_dict:
    print(key, '->', a_dict[key])

for item in a_dict.items():
    print(item)

for key in a_dict.keys():
    print(key)