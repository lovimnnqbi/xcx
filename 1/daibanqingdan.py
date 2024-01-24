class TodoList:
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)

    def remove_task(self, task):
        if task in self.todo_list:
            self.todo_list.remove(task)

    def view_tasks(self):
        for i, task in enumerate(self.todo_list):
            print(f"{i + 1}. {task}")

if __name__ == "__main__":
    todo_list = TodoList()
    while True:
        print("
待办事项清单：")
        todo_list.view_tasks()
        action = input("请输入操作（add/remove/view/quit）：")
        if action == "add":
            task = input("请输入待办事项：")
            todo_list.add_task(task)
        elif action == "remove":
            task = input("请输入待办事项编号：")
            try:
                task_index = int(task) - 1
                todo_list.remove_task(todo_list.todo_list[task_index])
            except (ValueError, IndexError):
                print("无效的待办事项编号，请重新输入。")
        elif action == "view":
            todo_list.view_tasks()
        elif action == "quit":
            break
        else:
            print("无效的操作，请重新输入。")
