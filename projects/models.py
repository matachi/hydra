from PIL import Image
from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db import models
import os
from tempfile import NamedTemporaryFile


class Platform(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Library(models.Model):
    title = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class Tool(models.Model):
    title = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class OverwriteStorage(FileSystemStorage):
    # http://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def large_filename(instance, filename):
    _filename, file_extension = os.path.splitext(filename)
    return 'projects/screenshots/%s%s' % (instance.title, file_extension)


def thumbnail_filename(instance, filename):
    _filename, file_extension = os.path.splitext(filename)
    return 'projects/screenshots/%s-thumbnail%s' % (instance.title,
                                                    file_extension)


class Screenshot(models.Model):
    title = models.CharField(max_length=50)
    large = models.ImageField(upload_to=large_filename,
                              storage=OverwriteStorage(), blank=True)
    thumbnail = models.ImageField(upload_to=thumbnail_filename,
                                  storage=OverwriteStorage(), blank=True)

    def save(self, *args, **kwargs):
        large_initial_file = self.large.file
        super().save(*args, **kwargs)
        if large_initial_file == self.large.file:
            return

        # Open the large file with Pillow
        pillow_image = Image.open(self.large.file)
        # Resize and crop the image
        # pillow_image = ImageOps.fit(pillow_image, (150, 150), Image.ANTIALIAS)
        pillow_image.thumbnail((150, 150), Image.ANTIALIAS)
        # Create a temporary named file
        image_tmp = NamedTemporaryFile(delete=True)
        # Save the resized Pillow image to the temporary named file
        pillow_image.save(image_tmp.name, 'JPEG', quality=95)
        # Save the Django model's thumbnail
        self.thumbnail.save('{}.jpg'.format('kalleanka'), File(image_tmp))
        image_tmp.close()

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    project = models.ForeignKey('Project', related_name='links')


def title_image_filename(instance, filename):
    _filename, file_extension = os.path.splitext(filename)
    return 'projects/title-images/%s%s' % (instance.title, file_extension)


class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date = models.CharField(max_length=50)
    source_code = models.URLField(blank=True)
    license = models.CharField(max_length=50, blank=True)
    platforms = models.ManyToManyField(Platform, related_name='projects')
    programming_languages = models.ManyToManyField(ProgrammingLanguage,
                                                   related_name='projects')
    libraries = models.ManyToManyField(Library, related_name='projects',
                                       blank=True)
    tools = models.ManyToManyField(Tool, related_name='projects', blank=True)
    title_image = models.ImageField(upload_to=title_image_filename,
                                    storage=OverwriteStorage())
    screenshots = models.ManyToManyField(Screenshot, related_name='projects',
                                         blank=True)

    def __str__(self):
        return self.title
