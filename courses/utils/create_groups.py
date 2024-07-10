from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

admin_group, admin_created = Group.objects.get_or_create(name="site-admin")
member_group, member_created = Group.objects.get_or_create(name="member")
user_group, user_created = Group.objects.get_or_create(name="user")

ct = ContentType.objects.get_for_model(User)

create_courses = Permission.objects.create(
        codename='create_courses',
        name='Can create courses',
        content_type=ct,
        )

update_courses = Permission.objects.create(
        codename='update_courses',
        name='Can update courses',
        content_type=ct,
        )

delete_courses = Permission.objects.create(
        codename='delete_courses',
        name='Can delete courses',
        content_type=ct,
        )

create_questions = Permission.objects.create(
        codename='create_questions',
        name='Can create questions',
        content_type=ct,
        )

create_choices = Permission.objects.create(
        codename='create_choices',
        name='Can create choices',
        content_type=ct,
        )

member_courses = Permission.objects.create(
        codename='member_courses',
        name='Can get member courses',
        content_type=ct,
        )

user_courses = Permission.objects.create(
        codename='get_courses',
        name='Can get courses',
        content_type=ct,
        )

admin_perms = [
        create_courses,
        update_courses,
        delete_courses,
        create_questions,
        create_choices,
        ]

admin_group.permissions.set(admin_perms)
member_group.permissions.add(member_courses)
user_group.permissions.add(user_courses)
