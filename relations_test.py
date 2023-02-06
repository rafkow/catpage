from sheerjoy.models import Gallery

g = list(Gallery.objects.all())
g[0].get_hashtags()

