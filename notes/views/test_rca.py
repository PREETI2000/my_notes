def test(data):
    rewards = data.get("reward")
    if rewards > 10:
        print("rewards is greater than 10")
    return True