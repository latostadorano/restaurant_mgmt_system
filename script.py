# usamos pwinput para que no muestre el password al insertarlo
import pwinput
import pandas as pd

menu = {'Items': ['Greek Gyro', 'Classic Burger', 'Cheeseburger', 'Bacon Burger', 'Mushroom Swiss Burger', 'Veggie Burger', 'Greek Salad', 'Green Salad', 'French Fries', 'Greek Fries', 'Soft Drinks', 'Beer', 'Milkshake'],
        'Items_code': ['10', '20', '21', '22','23','24', '30', '31', '40', '41', '50', '51', '60'],
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
tables_data = {}
#table = {'table': '', 'items': {}, 'assigned_to': '', 'bill': 0, 'active': False} 
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
                print('❗️ Incorrect password, try again')
                
    else:
        print('❗️ Not a registered user')
        intro()

# We will create a function that stores data and some methods to add info to the table 
class Table: 
    def __init__(self, table, assigned_to):
        self.table = table
        self.assigned_to = assigned_to
        self.items = {}
        self.bill = 0
        self.active = True
    def __ref__(self):
        return "Table {table} is assigned to {assigned_to}. It has {number_of_items}, and it's bill is about {bill}".format(table=self.table, assigned_to=self.assigned_to, number_of_items=len(self.items), bill=self.bill)

    def add_item_table (self, table):
        # Haremos un método dentro de la calse de Tables para detectar si sigue queriendo añadir items a la misma cuenta o a otra
        self.table = str(table)
        number_of_items = int(input('How many items? '))
        print()
        item_code = ''
        #print(df.Items_code)
        while item_code not in df['Items_code'].values: 
            item_code = input('Enter the item\'s code you\'ll add to table {table}: '.format(table = self.table))
            # If the item exists in menu:
            if item_code in df.Items_code.values:
                # item_name = el producto que concuerda con ese código
                item_name = df.loc[df['Items_code'] == item_code, 'Items'].iloc[0]
                # sacamos el precio según el código en el menú
                item_price = df.loc[df['Items_code']== item_code, 'Price'].iloc[0]

                # agregamos cantidad y producto a la cuenta
                if item_name in tables_data[self.table]['items']:
                    tables_data[self.table]['items'][item_name][0] += number_of_items
                else:
                    tables_data[self.table]['items'][item_name] = [number_of_items, item_price]

                # agregamos producto a la cuenta y actualizamos la cuenta
                tables_data[self.table]['bill'] += round((item_price * number_of_items),2)

                print(tables_data)
                print('✨ {num} {item} were added to table {table}'.format(num = number_of_items, item = item_name, table = self.table))
                print()

                input_adding = ''
                options_adding = ['y', 'Y', 'n', 'N']
                while input_adding not in options_adding:
                    input_adding = input('Do you want to add another item? y/n : ')
                    if input_adding in options_adding:
                        if input_adding == 'y' or input_adding == 'Y':
                            self.add_item_table(self.table)
                        else: 
                            pass
                    else: 
                        print('❗️ That is not an option. ')
                
            else: 
                print('❗️ That item doesn\'t exists')
        pass

    
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
            print()
            self.add_item()
        elif action == '3': 
            print('>> Add new user')
            print()
            self.add_user()
        elif action == '0': 
            print('>> ' + self.name.title() + ' has been signed off.')
            print()
            self.sign_off()
        else:
            print('❗️  That\'s not an option')

    def add_item(self):
        table_input = ''
        number_of_items = 0
        while table_input not in tables_data:
            table_input = input('Select the table to add items to: ')
            if table_input in tables_data: 
                if table_input in users_data[self.name]['active_tables']:
                    table_to_add = Table(table_input, self.name)
                    table_to_add.add_item_table(table_input)
                    # LLamaremos a un método en tables que añadirá los items a su misma mesa si así desea continuar
                    self.options()
                else: 
                    print('❗️ That account isn\'t yours')
                    print()
            else: 
                print('Table {table} does not exists.'.format(table = table_input))

    def add_table(self):
        new_table = input('Select new table: ')
        table_available = True 
        for i in users_data:
            if new_table in users_data[i]['active_tables']:
                table_available = False
                print('❗️ Table {table} is already in {name}\'s tables.'.format(table = new_table, name = users_data[i]['name'].title()))
                self.add_table()

        if table_available == True:
            users_data[self.name]['active_tables'].append(new_table)
            print('✨ Table {table} has been added to {name}\'s tables.'.format(table = new_table, name = self.name.title()))
            tables_data[new_table] = {'name': new_table, 'items': {}, 'assigned_to': self.name, 'bill': 0, 'active': True}
            print(tables_data)            

        """ if new_table in users_data[self.name]['active_tables']:
            print('That table already exists in {name}\'s active tables')
        #elif new_table in #any other people's tables
            # say it's active on someone elses tables """
            
        
        print()
        print(users_data)
        self.options()

    def add_user(self):
        puesto = ['gerente', 'cajero', 'mesero']

        if self.charge == 'gerente':
            new_name = input('{name}, agrega nombre del nuevo usuario: '.format(name=self.name.title()))
            
            new_charge = ''
            while new_charge not in puesto:
                new_charge = input(self.name.title() + ', agrega el puesto para ' + new_name.title() + '. Gerente, Cajero o Mesero: ')
                new_charge = new_charge.lower()
                if new_charge in puesto:
                    print('>> ' + new_name.title() + ' has been added as ' + new_charge.title() + '.')
                    print()
                else:
                    print('❗️ Esa opción no existe')

            def new_password_function():
                new_password = ''
                while len(new_password) != 4:
                    new_password = pwinput.pwinput(prompt=self.name.title() + ', inserta nuevo password para ' + new_name.title() + ', 4 dígitos: ')
                    if len(new_password) == 4:
                        continue
                    else: 
                        print('❗️ El password debe ser de 4 caracteres.')
                    
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
                        print('❗️ Confirmation failed, try again')
                        if confirm_psswd_try > 3:
                            new_password_function()
            
            new_password_function()
            
        elif self.charge != 'gerente':
            print('❗️ {name} no tiene los permisos para dar de alta un nuevo usuario.'.format(name=self.name.title())) 
            self.options()

    def sign_off(self):
        intro()

print()
intro()


