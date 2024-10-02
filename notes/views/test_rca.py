def test(data):
    rewards = data.get("reward")
    if rewards > 10:
        print("rewards is less than 10")
    return True