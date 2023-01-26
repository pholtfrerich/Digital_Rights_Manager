from django import forms

class DigitalRightsGeneratorForm(forms.Form):
    link = forms.CharField(label = 'Link', max_length=2083)
    licensor = forms.CharField(label = 'Licensor', max_length=255)
    content_title = forms.CharField(label = 'Content Title', max_length=255)

    #terms = 'Generic Contract'
    #creator = 'Paul Holtfrerich'
    #licensing_platform = 'Watermark'