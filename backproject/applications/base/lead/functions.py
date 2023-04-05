def curriculum_path(instance, filename):
    return 'job_application/application_{}/{}'.format(instance.pk, filename)