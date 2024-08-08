#def perform_action(action):
#    match action:
#        case 'add':
#            return 'Adding item'
#        case 'delete':
#            return 'Deleting item'
#        case 'update':
#            return 'Updating item'
#        case _:
#            return 'Unknown action'
#    result = perform_action('add')
#    print(result) # Output: Adding item


def perform_action(action):
    foo_dict: dict = {"add": "Adding item", "delete": "Deleting item", "update": "Updating item"}
    result = foo_dict.get("add")
    print(result)  # Output: Adding item
    return action
perform_action("add")

