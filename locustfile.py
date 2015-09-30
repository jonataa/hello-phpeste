from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    @task
    def hello(self):
        self.client.get("/hello")

    @task
    def count(self):
        self.client.get("/count")

    @task
    def writefile(self):
        self.client.get("/writefile")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 5000
