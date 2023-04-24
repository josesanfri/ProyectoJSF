def restaurant_image_path(instance, filename):
    return 'restaurant/restaurant_{0}/images/{1}'.format(instance.restaurant.pk, filename)
