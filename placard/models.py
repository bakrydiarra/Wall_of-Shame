from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


class Persona(models.Model):
    shamefull_nickname = models.CharField(
        max_length=50, unique=True, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_persona'
        )
    shameful_pic = CloudinaryField('image', default='placeholder')
    shameful_song = models.CharField(max_length=100, blank=False)
    shameful_tv_show = models.CharField(max_length=100, blank=False)
    shameful_habit = models.CharField(max_length=150, blank=False)
    shameful_story = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='placard_likes', blank=True
        )

    class Meta:

        """
        To sort persona in descending oder from the newest to the oldest
        """

        ordering = ['-created_on']

    def __str__(self):
        """
        To return a string representation of Persona -
        displaying persoa in the Django admin interface
        """
        return self.shamefull_nickname

    def number_of_likes(self):
        """
        To return the total number of like on a persona
        """
        return self.likes.count()

    def number_of_comments(self):
        """
        To return the total number of comment on a persona
        """
        return self.comments.count()

    def get_absolute_url(self):
        """
        To render/get the absolute URL of specific object of the model
        """
        return reverse('persona_detail', kwargs={'slug': self.slug})

    def save(self, *args, **Kwargs):

        """
        Reference: https://learndjango.com/tutorials/django-slug-tutorial#slugs
           To use slugify to preopulate shammefull_nickname input into a slug
        """

        if not self.slug:
            self.slug = slugify(self.shamefull_nickname)
        return super().save(*args, **Kwargs)


class Comment(models.Model):

    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, related_name='comments'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_comments'
        )
    content = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        To sort comments in ascending oder from the oldest to the newest
        """
        ordering = ['created_on']

    def __str__(self):
        """
        To return a string representation of the comment -
        displaying comments in the Django admin interface
        """
        return f'{self.author} commented persona {self.persona}'


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_likes'
        )
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, related_name='persona_likes'
        )

    def __str__(self):
        """
        To return a string representation of like -
        displaying likes in the Django admin interface
        """
        return f'{self.author} liked {self.persona}'
