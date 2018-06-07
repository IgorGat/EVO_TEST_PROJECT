from django.db import models

class Record(models.Model) :
    text=models.TextField()
    def _get_unique_elements(self):
         d = {}; text=self.text.split(' ')
         for i in range(len(text)):
             key = text[i]
             if key != ' ':
                quont=d.get(key, 0)+1
                d[key]=quont
         return sorted(d.values(), reverse=True)
