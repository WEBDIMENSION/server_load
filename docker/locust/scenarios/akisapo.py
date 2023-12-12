from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    host = "https://www.akisapo.jp"
    tasks = {UserBehavior:1}
    wait_time = constant(0)
