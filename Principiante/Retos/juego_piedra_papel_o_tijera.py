import random
options = ('piedra', 'papel', 'tijera')



def run_game():
    computer_winds = 0
    user_winds = 0 
    rounds = 1
    while True:
        print('*'*10)
        print('ROUND', rounds)
        print('*'*10)
        print('computer --> ',computer_winds)
        print('user --> ',user_winds)  

        rounds +=1
        user_option, computer_option = choose_options()
        user_winds,computer_winds = check_rules(user_option , computer_option,user_winds,computer_winds)
        if computer_winds == 2:
            print('El ganador es el computador')
            break    
        if user_winds == 2:
            print('El ganador es el usuario')
            break 
    
def choose_options():
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    computer_option = random.choice(options)
    if not user_option in  options:
        print('Opcion invalida')
        #continue
        return None,None
    print('User option => ',user_option)
    print('Computer option => ', computer_option )
    return user_option , computer_option

def check_rules(user_option, computer_option,user_winds,computer_winds):
    if user_option == computer_option:
            print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Ganaste:piedra gana a tijera')
            user_winds += 1
        else:
            print('Perdiste: por que papel gana a piedra')
            computer_winds += 1
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('Perdiste:papel pierde contra tijera')
            computer_winds += 1
        else:
            print('Ganaste: por que papel gana a piedra')  
            user_winds += 1     
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Ganaste:tijera gana a papel')
            user_winds += 1
        else:
            print('Perdiste: por que tijera pierde contra piedra')
            computer_winds += 1        
    return user_winds,computer_winds

run_game( )


    