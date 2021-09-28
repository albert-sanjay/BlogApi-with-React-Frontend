from django.http import response
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from blog.models import Category, Post
from django.contrib.auth.models import User

# Create your tests here.
class PostTests(APITestCase):

    def test_view_post(self):
        url = reverse('api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )


        data = {
            'title':'new', 'author':'1', 'excerpt': 'new',
            'content': 'new'
        }

        client.login(username=self.testuser1.username, password='123456789')

        url = reverse('api:listcreate')
        response = client.post(url, data , format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')

        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', author=self.testuser1 , status='published')

        client.login(username=self.testuser1.username, password='123456789')

        url = reverse(('api:detailcreate'), kwargs={'pk':1})

        response = client.put(
            url, {
                "title": " New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)