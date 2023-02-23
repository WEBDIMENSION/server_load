from locust import HttpLocust, TaskSequence, seq_task, between
from locust.clients import HttpSession

def initialize(l):
    l.client.get("/initalize")

def item_list(l):
    l.client.get("/item_list")

def add_item(l):
    l.client.post("/add_item", {"item_name":"あああ"})

class ScenarioTask(TaskSequence):

    # ()内の数値＝実行順番
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

    # タスク間の時間。1~3秒でランダム秒数で実施する
    wait_time = between(1.0, 3.0)
