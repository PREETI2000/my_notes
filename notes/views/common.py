from django.core.exceptions import MultipleObjectsReturned


def get_object_or_none(model_name, *args, **kwargs):
    try:
        return model_name.objects.get(*args, **kwargs)
    except model_name.DoesNotExist:
        return None
    except MultipleObjectsReturned:
        return None
