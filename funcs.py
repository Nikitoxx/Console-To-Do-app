def show_menu():
    print('''\nMenu:
          
1.Show tasks
2.Finished tasks
3.Add new task
4.Exit\n''')


def show_tasks():
    a = open('tasks.txt', 'r')
    
    for i in a:
        print(i, end='')
        
    a.close() 


show_tasks()


