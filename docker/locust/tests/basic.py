from locust import HttpLocust, TaskSequence, seq_task, between
from locust.clients import HttpSession

def initialize(l):
    l.client.get("/initalize")

def item_list(l):
    l.client.get("/item_list")

def add_item(l):
    l.client.post("/add_item", {"item_name":"$B$"$"$"(B"})

class ScenarioTask(TaskSequence):

    # ()$BFb$N?tCM!a<B9T=gHV(B
    @seq_task(1)
    def initialize(self):
        initialize(self)

    @seq_task(2)
    def item_list(self):
        item_list(self)

    @seq_task(2)
    def add_item(self):
        add_item(self)

class WebsiteUser(HttpLocust):
    task_set = ScenarioTask

    # $B%?%9%/4V$N;~4V!#(B1~3$BIC$G%i%s%@%`IC?t$G<B;\$9$k(B
    wait_time = between(1.0, 3.0)
