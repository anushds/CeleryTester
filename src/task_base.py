from celery import Task


class TaskBase(Task):
    abstract = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"Task {task_id} failed with exception {exc}")
        super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        print(f"Task {task_id} succeeded with result {retval}")
        super().on_success(retval, task_id, args, kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError("Tasks must implement the run method")