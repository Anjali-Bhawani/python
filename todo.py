todo_list = []
end_of_todo = 'n'
while end_of_todo != 'y':
    todo_item = input("enter your work")
    add_todo = todo_list.append(todo_item)
    end_of_todo = input("enter n if you want to add more otherwise y")
print(todo_list)
