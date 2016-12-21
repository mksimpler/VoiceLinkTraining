from vocollect_core.task.task_runner import TaskRunnerBase

def change_vehicle():
    runner = TaskRunnerBase.get_main_runner()
    task = runner.findTask('coreTaskCustom')
    
    if task is not None:
        from voice import globalwords
        globalwords.words['change vehicle'].enabled = False
        task.change_vehicle()