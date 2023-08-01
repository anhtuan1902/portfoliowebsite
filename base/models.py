from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        # Sắp xếp theo thứ tự giảm dần theo id
        ordering = ['id']


class Project(BaseModel):
    title = models.CharField(max_length=50)
    img = models.FileField(upload_to='portfolio-image', null=False)
    description = models.TextField(max_length=525)
    skill = models.ManyToManyField('Skill', related_name='projects')
    link = models.URLField(null=True)
    start_project = models.DateField()
    end_project = models.DateField()

    def __str__(self):
        return self.title

    def project_img(self):
        return mark_safe('<img src="{}" width="100" alt="product_img"/>'.format(self.img.url))

    def skills(self):
        return ",\n".join([s.name_skill for s in self.skill.all()])


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    img = models.FileField(upload_to='portfolio-image', null=False)

    def __str__(self):
        return self.name

    def project_img(self):
        return mark_safe('<img src="{}" width="100" alt="product_img"/>'.format(self.img.url))


class Skill(BaseModel):
    name_skill = models.CharField(max_length=50, unique=True)
    cate_skill = models.ForeignKey(Category, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_skill


class Contact(models.Model):
    subject = models.CharField(max_length=254, null=False)
    body = models.TextField(max_length=525, null=False)
    email = models.EmailField(max_length=254, null=False)
    name = models.CharField(max_length=254, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

