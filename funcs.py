def show_menu():
    print('''\nMenu:
          
1.Show tasks
2.Finished tasks
3.Add new task
4.To assign a completed task
5. Clear
6. Delete Task
7.Exit\n''')


def show_tasks():
    a = open('tasks.txt', 'r')
    if a:
        for i in a:
            print(i)
        a.close()
    
    
def show_finish_task():
    a = open('tasks.txt', 'r')
    for i in a:
        if '[x]' in i:
            print(i)
    a.close()
    

def add_task():
    while True:
        a = input('Write your task: ')
        with open('tasks.txt', 'a') as file:
            file.write(f'[] {a}\n')
        b = input('Do you want to add one more? 1.Yes 2.No ')
        if b.lower() == 'yes':
            continue
        else:
            break


def clear():
    with open('tasks.txt', 'w') as file:
        file.write("")


def del_task():
    while True:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            
        #Перебираем циклом строки
        for i, v in enumerate(tasks, 1):
            print(f'{i}. {v}')
        
        try:
            user = int(input('Which task do you want to delete ---> '))
            if 1 <= user <= len(tasks):
                del tasks[user - 1]
            else:
                print("There's no such task!")
                break
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
                break
            
        except ValueError:
            break
        

def complete_task():
    while True:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            
        #Перебираем циклом строки
        for i, v in enumerate(tasks, 1):
            print(f'{i}. {v}')
        
        try:
            user = int(input('Which task have you complete ---> '))
            if 1 <= user <= len(tasks):
                tasks[user - 1] = tasks[user - 1].replace('[]','[x]')
            else:
                print("There's no such task!")
                break
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
                break
            
        except ValueError:
            break
        