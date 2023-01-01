from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from blog.models import Tag, Post, Comment

=======
from blog.models import Tag, Post

admin.site.register(Tag)
>>>>>>> 2813ec5e2876bcf7914d967a2f36a82e68ea41e2


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

<<<<<<< HEAD
# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
    

=======
admin.site.register(Post, PostAdmin)
>>>>>>> 2813ec5e2876bcf7914d967a2f36a82e68ea41e2
