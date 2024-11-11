from notes.models import NotesUser

STORY_SHARE_MESSAGE_SUFFIX = "hello"


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
    

