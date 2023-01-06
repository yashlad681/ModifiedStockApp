from django.db import models

class SearchLog(models.Model):
    stock_name = models.CharField(max_length=10,null=True,blank=True)
    searched_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.stock_name
