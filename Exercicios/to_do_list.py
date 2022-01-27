def show_tasks(task_list=[]):
    if task_list == []:
        print('Your task list is empty. ')
    else:
        print(20*'=-=')
        print("Tasks: ")
        for task in task_list:
            print(f'- {task}')
        print(20*'=-=')


def undo_task(task_list, lasts_removed_tasks):
    removed_task = task_list.pop()
    lasts_removed_tasks.append(removed_task)
    print('Task removed.')
    return task_list


def redo_task(task_list, lasts_removed_tasks):
    task_list = lasts_removed_tasks.pop()
    print('The last task is back to your task list.')
    return task_list


def add_task(task):
    task_list.append(task)
    print('The task added sucessfully!')


if __name__ == "__main__":
    task_list = []
    choices = ('add', 'undo', 'redo', 'list')
    lasts_removed_tasks = []
    while True:
        user_input = str(input("Add, Undo, Redo or List a task ? ")).lower()
        if user_input in choices:
            if user_input == 'add':
                task = str(input('Type a task to be added:'))
                add_task(task)

            elif user_input == 'list':
                show_tasks(task_list)

            elif user_input == 'undo':
                task_list = undo_task(task_list, lasts_removed_tasks)
                print(lasts_removed_tasks)

            elif user_input == 'redo':
                if lasts_removed_tasks:
                    last_task = redo_task(task_list, lasts_removed_tasks)
                    task_list.append(last_task)
                else:
                    print("There's nothing to be done!")
        else:
            print('Type a valid choice.')
