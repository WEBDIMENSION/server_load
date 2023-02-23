from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def profile(self):
        # self.client.get("/sample", verify=False)
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(0)
