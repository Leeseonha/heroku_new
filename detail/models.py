from django.db import models

class Detail(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Detail, related_name = 'comments', on_delete = models.CASCADE)
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.content
    


