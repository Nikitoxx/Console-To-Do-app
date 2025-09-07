def show_menu():
    print('''\nMenu:
          
1.Show tasks
2.Finished tasks
3.Add new task
4.To assign a completed task
5.Exit\n''')


def show_tasks():
    a = open('tasks.txt', 'r')
    for i in a:
        print(i, end='')
    a.close()
    
    
def show_finish_task():
    a = open('tasks.txt', 'r')
    for i in a:
        if '(done)' in i:
            b = i.replace('(done)', '')
            print(b)
    a.close()
    
show_finish_task()

