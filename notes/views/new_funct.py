from notes.models import NotesUser

STORY_SHARE_MESSAGE_SUFFIX = "hello"

def get_qs_data_list(qs, data_key):
    qs = []
    if data_key:
        qs = qs[0]
    return qs

def get_story_text(story_info):
    ds = get_qs_data_list(story_info, data=story_info)
    if ds:
        story_share_text = story_info.get('story_title') + "\n" + STORY_SHARE_MESSAGE_SUFFIX
        print("note user exists")
    x = True if ds else False
    return x

def test_empty_list():
    note_user = NotesUser.objects.filter(name="preeti")
    return note_user[0].name

def test_keyerror(user_data):
    rewards = user_data.get("days", None)
    if rewards > 30:
        print("user is eligible")
        return True
    return False