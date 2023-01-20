# usamos pwinput para que no muestre el password al insertarlo
import pwinput

#Crearemos una clase de usuario, definirá permisos y cuentas abiertas
users_data = {'admin':{'name': 'admin', 'charge': 'gerente', 'password': '1234'}}
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
        self.tables = {'actives':[], 'closed':[]}

    def __ref__(self):
        return "{name} is a {charge} and has {number} of active tables: {tables}".format(name=self.name, charge = self.charge, number = len(self.tables['actives']), tables = self.tables['actives'])

    def options(self):
        action = input(''':::: :::: :::: :::
OPCIONES:
1.- Abrir una cuenta
2.- Agregar un producto
3.- Crear un usuario
0.- Salir
:::: :::: :::: :::

'Elija el número de la opción: ''')

        if action == '1':
            print('>> New table')
            #self.new_table()
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

            
            new_password = ''
            while len(new_password) != 4:
                new_password = pwinput.pwinput(prompt=self.name.title() + ', inserta password para ' + new_name.title() + ', 4 dígitos: ')
                if len(new_password) == 4:
                    print('>> Nuevo password agregado')
                    print()
                else: 
                    print('>> El password debe ser de 4 caracteres.')
                
            confirm_psswd = pwinput.pwinput(prompt='Confirmar password: ')
            if new_password == confirm_psswd: 
                users_data[new_name] = {'name':new_name.lower(), 'charge': new_charge, 'password': new_password}
                print()
                print('✨ {nombre} ha sido añadido como {charge} al sistema.'.format(nombre = users_data[new_name]['name'].title(), charge=users_data[new_name]['charge'] ))
                print()
                self.options()
            
        elif self.charge != 'gerente':
            print('{name} no tiene los permisos para dar de alta un nuevo usuario.'.format(name=self.name)) 
            self.options()

    def sign_off(self):
        intro()

print()
intro()


