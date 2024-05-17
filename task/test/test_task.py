import pytest
from task.test.factories import TaskFactory


pytestmark = pytest.mark.django_db
from django.urls import reverse
from task.models import Task
from user.test.factories import UserFactory

task_list_url = "task:task-list"
task_detail_url = "task:task-detail"


class TestTaskCategories:

    def test_create_task(self, api_client, mocked_authentication):
        """Test creation of task"""
        user = UserFactory()
        mocked_authentication(active_user=user)
        payload = {
            "title": "Education",
            "description": "Read my novels",
            "due_date": "2024-05-16T16:43:21.206706Z",
        }
        url = reverse(task_list_url)
        response = api_client.post(url, payload)
        assert response.status_code == 201
        assert response.data.get("title") == payload["title"]

    def test_unauthorized_creation_of_task(self, api_client):
        """Test creation of task without jwt token"""

        payload = {
            "title": "Education",
            "description": "Read my novels",
            "due_date": "2024-05-16T16:43:21.206706Z",
        }
        url = reverse(task_list_url)
        response = api_client.post(url, payload)
        assert response.status_code == 401

    def test_list_task(self, mocked_authentication, api_client):
        """Test  get list of  tasks"""
        user = UserFactory()
        auth_user = mocked_authentication(active_user=user)
        TaskFactory.create_batch(3, user=auth_user)
        url = reverse(task_list_url)
        response = api_client.get(url)
        print(response.data)
        assert response.status_code == 200
        assert response.data.get("total") == 3

    def test_unauthorized_list_task(self, api_client):
        """Test unauthorized get list of  tasks"""
        user = UserFactory()
        TaskFactory.create_batch(3, user=user)
        url = reverse(task_list_url)
        response = api_client.get(url)
        print(response.data)
        assert response.status_code == 401

    def test_get_task(self, mocked_authentication, api_client):
        """Test getting of a task"""
        user = UserFactory()
        auth_user = mocked_authentication(active_user=user)
        task = TaskFactory.create(user=auth_user)
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data.get("title") == task.title
        assert response.data.get("description") == task.description

    def test_unauthorized_get_task(self, api_client):
        """Test unauthorized getting of a task"""
        user=UserFactory()
        task = TaskFactory.create(user=user)
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = api_client.get(url)
        assert response.status_code == 401

    @pytest.mark.parametrize("method_name", ['patch', 'put'])
    def test_update_task_task(self, mocked_authentication, api_client, method_name):
        """Test updating a  task"""
        user = UserFactory()
        auth_user= mocked_authentication(active_user=user)
        task = TaskFactory.create(title="old_title",user=auth_user)
        payload = {
            "title": "new_title",
            "due_date": "2024-05-16T16:43:21.206706Z",
            "description": "new description",
        }
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = getattr(api_client, method_name)(url, data=payload)
        task.refresh_from_db()
        assert response.status_code == 200
        assert response.json()['title'] == payload['title']
        assert task.title == payload['title']

    @pytest.mark.parametrize("method_name", ['patch', 'put'])
    def test_unauthorized_update_task_task(self, api_client, method_name):
        """Test unauthorized updating a  task"""
        user= UserFactory()
        task = TaskFactory.create(title="old_title",user=user)
        payload = {"title": "new_title","due_date":"2024-05-16T16:43:21.206706Z","description":"new description"}
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = getattr(api_client, method_name)(url, data=payload)
        task.refresh_from_db()
        assert response.status_code == 401

    def test_delete_task(self, mocked_authentication, api_client):
        """Test deleting of a task"""
        user = UserFactory()
        auth_user =mocked_authentication(active_user=user)
        task = TaskFactory.create(user=auth_user)
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_unauthorized_delete_task(self, api_client):
        """Test unauthorized deleting of a task"""
        user = UserFactory()
        task = TaskFactory.create(user=user)
        url = reverse(task_detail_url, kwargs={"pk": task.id})
        response = api_client.delete(url)
        assert response.status_code == 401
