from website import models as models_website

def data(request):
    site = models_website.Siteweb.objects.filter(status=True).first
    return locals()