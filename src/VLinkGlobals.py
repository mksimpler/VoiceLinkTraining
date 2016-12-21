task_name = None
runner = None

def change_vehicle():
    task = runner.findTask(task_name)
    if task is not None:
        from voice import globalwords
        globalwords.words['change vehicle'].enabled = False
        task.change_vehicle()