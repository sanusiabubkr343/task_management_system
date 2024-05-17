import factory
from factory import Faker
from task.models import Task
from datetime import datetime, timedelta
import random


class TaskFactory(factory.django.DjangoModelFactory):
    description = Faker('sentence')
    title = Faker('sentence', nb_words=4)  # Generates a fake title-like string
    due_date = factory.LazyAttribute(
        lambda x: datetime.now() + timedelta(days=random.randint(1, 30))
    )
    is_completed = False

    class Meta:
        model = Task
