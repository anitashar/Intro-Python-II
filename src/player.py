# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room,items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def add_item(self,item):
        selection= None
        for i in self.current_room.items:
            if i.name == item:
                selection = i
            else:
                continue
        if selection != None:
            self.items.append(selection) 
            self.current_room.items.remove(selection)
            selection.on_take()
        else:
            print(f'Can not find the {item}')




    def drop_item(self,item):
        selection= None
        for i in self.items:
            if i.name == item:
                selection = i
            else:
                continue
        if selection != None:
            self.items.remove(selection) 
            self.current_room.items.append(selection)
            selection.on_drop()
        else:
            print(f'Can not drop the  {item}')
        

    def check_inventory(self):
        print(f'inventory:')
        if len(self.items)>0:
            for item in self.items:
                print(item)
        else:
            print(f'no items')
                
        