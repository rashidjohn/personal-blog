from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.FileField(upload_to='post-images')
    tags = models.ManyToManyField('Tag',related_name='tags', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'postapp'
        ordering = ['-created_on']

    def __str__(self) -> str:
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=100, blank=True, null=True)
    msg = models.TextField()
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    image = models.FileField(upload_to='comment-image', default='comment-image/user.png')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def getReplies(self):
        return Comment.objects.filter(parent=self).reverse()
    
    @property
    def isParent(self):
        if self.parent is None:
            return True
        return False
    
class About(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='my_image')
    instagram = models.CharField(max_length=100,blank=True,null=True)
    facebook = models.CharField(max_length=100,blank=True,null=True)
    youtube = models.CharField(max_length=100,blank=True,null=True)
    linkedin = models.CharField(max_length=100,blank=True,null=True)
    telegram = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name    