# usamos pwinput para que no muestre el password al insertarlo
import pwinput
import pandas as pd

menu = {'Items': ['Greek Gyro', 'Classic Burger', 'Cheeseburger', 'Bacon Burger', 'Mushroom Swiss Burger', 'Veggie Burger', 'Greek Salad', 'Green Salad', 'French Fries', 'Greek Fries', 'Soft Drinks', 'Beer', 'Milkshake'],
        'Description': ['Traditional Greek-style gyro with lamb or chicken, tzatziki sauce, lettuce, tomato, and onion on a pita bread.',
                         '100% beef patty, lettuce, tomato, onion, and special sauce.',
                         'Same as the classic, but with a choice of American, cheddar, or Swiss cheese.',
                         'Classic burger with crispy bacon and cheddar cheese.',
                         'Classic burger with sautéed mushrooms and Swiss cheese.',
                         'Vegetarian patty with lettuce, tomato, onion, and special sauce.',
                         'A classic Greek salad with tomatoes, cucumbers, onions, feta cheese, and Kalamata olives, dressed with olive oil and lemon juice.',
                         'A mix of greens, tomatoes, cucumbers, and onions, dressed with vinaigrette.',
                         'Crispy golden fries, salt and pepper to taste',
                         'Crispy golden fries topped with feta cheese and a sprinkle of oregano.',
                         'Coke, Diet Coke, sprite, Fanta',
                         'Selection of domestic and imported beers',
                         'Vanilla, Chocolate, Strawberry'],
        'Price': [7.99, 6.99, 7.49, 8.99, 8.49, 6.99, 5.99, 4.99, 3.99, 4.99, 1.99, 3.99, 4.99],
        'Category': ['Gyros', 'Burgers', 'Burgers', 'Burgers', 'Burgers', 'Burgers', 'Salads', 'Salads', 'Fries', 'Fries', 'Beverages', 'Beverages', 'Desert'],
        'Ingredients': ['Lamb or chicken, tzatziki sauce, lettuce, tomato, onion, pita bread', 'Beef patty, lettuce, tomato, onion, special sauce', 'Beef patty, lettuce, tomato, onion, special sauce, cheese', 'Beef patty, bacon, lettuce, tomato, onion, special sauce, cheddar cheese', 'Beef patty, sautéed mushrooms, Swiss cheese, lettuce, tomato, onion, special sauce', 'Vegetarian patty, lettuce, tomato, onion, special sauce', 'Tomatoes, cucumbers, onions, feta cheese, Kalamata olives, olive oil, lemon juice', 'Mixed greens, tomatoes, cucumbers, onions, vinaigrette', 'Potatoes, salt, pepper', 'Potatoes, feta cheese, oregano', '', '', '']
}

df = pd.DataFrame(menu)
#print(df)
#print(df.Items)


#Crearemos una clase de usuario, definirá permisos y cuentas abiertas
users_data = {'admin':{'name': 'admin', 'charge': 'gerente', 'password': '1234', 'active_tables': [], 'closed_tables': []}}
#users = {'name': '', 'charge': '', 'psswd': '', 'tables': {'actives': [], 'closed': []} }
table = {'name': '', 'items': [], 'assigned_to': '', 'bill': 0, 'active': False} 
comida = {'categoría': '', 'precio': 0, 'ingredientes': [], 'tags': []}

def intro ():
    user_input = input('🌿 Welcome, enter your name: ')
    user_input = user_input.lower()
    if user_input in users_data.keys():
        
        psswd_temp = ''
        while psswd_temp != users_data[user_input]['password']:
            psswd_temp = pwinput.pwinput(prompt='Password: ')

            if psswd_temp == users_data[user_input]['password']:
                user_input = User(user_input, users_data[user_input]['charge'], users_data[user_input]['password'])
                user_input.options()
                print()

            else:
                print('Incorrect password, try again')
                
    else:
        print('Not a registered user')
        intro()

# We will create a function that stores data and some methods to add info to the user
class User:
    def __init__(self, name, charge, password):
        self.name = name
        self.charge = charge
        self.password = password
        self.active_tables = []
        self.closed_tables = []

    def __ref__(self):
        return "{name} is a {charge} and has {number} of active tables: {tables}".format(name=self.name, charge = self.charge, number = len(self.tables['actives']), tables = self.tables['actives'])

    def options(self):
        if self.charge == 'gerente': 
            action = input(''':::: :::: :::: :::
OPCIONES:
1.- Abrir una cuenta
2.- Agregar un producto
3.- Crear un usuario
0.- Salir
:::: :::: :::: :::

'Elija el número de la opción: ''')
        else:
            action = input(''':::: :::: :::: :::
OPCIONES:
1.- Abrir una cuenta
2.- Agregar un producto
0.- Salir
:::: :::: :::: :::

'Elija el número de la opción: ''')

        if action == '1':
            print('>> New table')
            self.add_table()
        elif action == '2': 
            print('>> Adding product')
            #self.add_item()
        elif action == '3': 
            print('>> Add new user')
            print()
            self.add_user()
        elif action == '0': 
            print('>> ' + self.name.title() + ' has been signed off.')
            print()
            self.sign_off()
        else:
            print('>> That\'s not an option')

    def add_table(self):
        new_table = input('Select new table: ')

        #Aqui vamos, se agrega la mesa aunque ya la tenga alguien más
        temp_available = True 
        for i in users_data:
            if new_table in users_data[i]['active_tables']:
                temp_available = False
                print('Table {table} is already in {name}\'s tables.'.format(table = new_table, name = users_data[i]['name'].title()))
                #add_table(self) Aquí va un recursion

        if temp_available == True:
            users_data[self.name]['active_tables'].append(new_table)
            print('✨ Table {table} has been added to {name}\'s tables.'.format(table = new_table, name = self.name.title()))

        """ if new_table in users_data[self.name]['active_tables']:
            print('That table already exists in {name}\'s active tables')
        #elif new_table in #any other people's tables
            # say it's active on someone elses tables """
            
        
        print()
        print(users_data)
        self.options()


    def add_user(self):
        cargos = ['gerente', 'cajero', 'mesero']

        if self.charge == 'gerente':
            new_name = input('{name}, agrega nombre del nuevo usuario: '.format(name=self.name.title()))
            
            new_charge = ''
            while new_charge not in cargos:
                new_charge = input(self.name.title() + ', agrega el puesto para ' + new_name.title() + '. Gerente, Cajero o Mesero: ')
                new_charge = new_charge.lower()
                if new_charge in cargos:
                    print('>> ' + new_name.title() + ' has been added as ' + new_charge.title() + '.')
                    print()
                else:
                    print('>> Esa opción no existe')

            def new_password_function():
                new_password = ''
                while len(new_password) != 4:
                    new_password = pwinput.pwinput(prompt=self.name.title() + ', inserta nuevo password para ' + new_name.title() + ', 4 dígitos: ')
                    if len(new_password) == 4:
                        continue
                    else: 
                        print('>> El password debe ser de 4 caracteres.')
                    
                confirm_psswd = ''
                confirm_psswd_try = 0
                while new_password != confirm_psswd:
                    confirm_psswd = pwinput.pwinput(prompt='Confirmar password: ')
                    if new_password == confirm_psswd: 
                        users_data[new_name] = {'name':new_name.lower(), 'charge': new_charge, 'password': new_password, 'active_tables': [], 'closed_tables': []}
                        print()
                        print('✨ {nombre} ha sido añadido como {charge} al sistema.'.format(nombre = users_data[new_name]['name'].title(), charge=users_data[new_name]['charge'] ))
                        print()
                        self.options()
                    else:
                        confirm_psswd_try +=1
                        print('Confirmation failed, try again')
                        if confirm_psswd_try > 3:
                            new_password_function()
            
            new_password_function()
            
        elif self.charge != 'gerente':
            print('{name} no tiene los permisos para dar de alta un nuevo usuario.'.format(name=self.name.title())) 
            self.options()

    def sign_off(self):
        intro()

print()
intro()


