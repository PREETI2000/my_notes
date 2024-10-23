from notes.models import NotesUser

STORY_SHARE_MESSAGE_SUFFIX = "hello"

def test_rewards(data):
    rewards = data["reward"]
    if rewards > 10:
        print("rewards is greater than 10")

    return True

def test_empty_list():
    note_user = NotesUser.objects.filter(name="preeti")
    return note_user[0].name

def main_func(data):
    if test_rewards():
        return True
    return False

def test_keyerror(user_data):
    rewards = user_data.get("days", None)
    if rewards > 30:
        print("user is eligible")
        return True
    return False

def get_qs_data_list(qs, data_key):
    qs = []
    if data_key:
        qs = qs[0]
    return qs

def return_data_value():
    data = {
        "name":"Preeti"
    },
    return data


def get_story_text(story_info):
    ds = get_qs_data_list(qs, data=story_info)
    if ds:
        story_share_text = story_info.get('story_title') + "\n" + STORY_SHARE_MESSAGE_SUFFIX
        print("note user exists")
    x = True if ds else False
    return x

def get_notes():
    x = NotesUser.objects.filter(name="preeti")
    y = x[0].name
    return y

def get_inactive_notes():
    x = NotesUser.objects.filter(is_active=False)
    y = x[0].name
    return y
    
def get_active_notes():
    x = NotesUser.objects.filter(is_active=True)
    y = x[0].name
    return y
    

