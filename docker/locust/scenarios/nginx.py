from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")
    @task(1)
    def cate(self):
        self.client.get("/cate/")
    @task(1)
    def not_found_404(self):
        self.client.get("/unkown/")

class WebsiteUser(HttpUser):
    host = "http://develop.local:49182"
    tasks = {UserBehavior:1}
    wait_time = constant(0)
