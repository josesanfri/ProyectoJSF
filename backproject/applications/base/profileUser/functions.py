# Local imports
from applications.utils.functions import generate_random_string

def profile_image_directory_path(instance, filename):
    random_string = generate_random_string()
    return 'users/user_{}/profile-image/{}/{}'.format(instance.user.pk, random_string, filename)

def document_directory_path(instance, filename):
    random_string = generate_random_string()
    return 'users/user_{}/documents/{}/{}'.format(instance.user.pk, random_string, filename)

def interest_image_path(instance, filename):
    return 'interests/interest_{}/{}'.format(instance.pk, filename)
