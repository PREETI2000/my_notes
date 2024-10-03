from notes.models import NotesUser


def test(data):
    rewards = data["reward"]
    if rewards > 10:
        print("rewards is greater than 10")

    return True

def test_empty_list():
    note_user = NotesUser.objects.filter(name="preeti")
    return note_user[0].name
    
def test_keyerror(user_data):
    rewards = user_data.get("days", None)
    if rewards > 30:
        print("user is eligible")
        return True
    return False
