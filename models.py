from django.db import models

import base64

class UploadedFile(models.Model):

    _data = models.TextField(
            db_column='data',
            blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
    filename = models.CharField(max_length=256)
    fileKey = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

class urlKeyList(models.Model):
    urlKey = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
