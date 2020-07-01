# Generated by Django 3.0.7 on 2020-07-01 10:10

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='image',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media'))]),
        ),
    ]
