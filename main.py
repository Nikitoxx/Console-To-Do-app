import funcs as f

menu_funcs = {'1': f.show_tasks,
              '2': f.show_finish_task,
              '3': f.add_task,
              '4': f.complete_task,
              '5': f.clear,
              '6': f.del_task
              }
#realise the logic of app 
while True:
    f.show_menu()
    choise = input('Select menu item: ')
    if choise not in menu_funcs:
        print('There\'s no such option')
    elif choise == '7':
        break
    else:
        menu_funcs.get(choise)()
    

