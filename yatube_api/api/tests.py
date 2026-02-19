from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post, Group

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаём тестового пользователя и группу
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-group',
            description='Описание тестовой группы'
        )
        cls.post = Post.objects.create(
            text='Тестовый пост',
            author=cls.user,
            group=cls.group
        )

    def test_post_creation(self):
        """Проверяем, что пост создался корректно."""
        self.assertEqual(self.post.text, 'Тестовый пост')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.group.title, 'Тестовая группа')
        self.assertEqual(str(self.post), 'Тестовый пост')

    def test_group_creation(self):
        """Проверяем создание группы."""
        self.assertEqual(self.group.slug, 'test-group')
        self.assertEqual(str(self.group), 'Тестовая группа')



