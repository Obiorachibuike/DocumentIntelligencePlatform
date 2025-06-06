# Generated by Django 5.2.1

from django.db import migrations, models
import django.core.validators
import django.db.models.deletion
import documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Document title', max_length=255)),
                ('file_path', models.FileField(help_text='Uploaded document file', upload_to=documents.models.document_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'docx', 'md'])])),
                ('file_type', models.CharField(help_text='File extension', max_length=10)),
                ('file_size', models.PositiveIntegerField(help_text='File size in bytes')),
                ('page_count', models.PositiveIntegerField(default=0, help_text='Number of pages')),
                ('status', models.CharField(choices=[('uploading', 'Uploading'), ('processing', 'Processing'), ('processed', 'Processed'), ('error', 'Error')], default='uploading', help_text='Processing status', max_length=20)),
                ('error_message', models.TextField(blank=True, help_text='Error details if processing failed', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DocumentChunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk_index', models.PositiveIntegerField(help_text='Sequential chunk number')),
                ('text', models.TextField(help_text='Chunk text content')),
                ('page_numbers', models.JSONField(default=list, help_text='List of page numbers this chunk spans')),
                ('embedding_id', models.CharField(help_text='Reference ID in vector store', max_length=255)),
                ('token_count', models.PositiveIntegerField(default=0, help_text='Number of tokens in chunk')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(help_text='Parent document', on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='documents.document')),
            ],
            options={
                'verbose_name': 'Document Chunk',
                'verbose_name_plural': 'Document Chunks',
                'ordering': ['document', 'chunk_index'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='documentchunk',
            unique_together={('document', 'chunk_index')},
        ),
    ]