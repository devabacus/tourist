from django.db import models

# Create your models here.
class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    rating = models.FloatField(null=True)
    def __str__(self):
        return str(self.telegram_id)

class Channel(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.telegram_id)
    

class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

class Flag(models.Model):
    flag_name = models.CharField(max_length=100)

class Message(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE, null=True)
    dialogue_id = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    message = models.TextField(null=True)
    from_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    replies = models.IntegerField(null=True)
    reply_to_msg_id = models.IntegerField(null=True)
    reply_to_top_id = models.IntegerField(null=True)
    reactions = models.CharField(max_length=200, null=True, blank=True)
    max_id = models.IntegerField(null=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    flags = models.ManyToManyField(Flag, blank=True)
    
    def __str__(self):
        return self.message