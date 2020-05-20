from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_uses_post_list(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_uses_post_detail(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_uses_post_new(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_uses_post_edit(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'blog/post_list.html')
