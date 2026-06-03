import moduleLSB as m
import time
import os

def show_preview():
    # Очищаем консоль перед выводом для красивого эффекта
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
    ===================================================================
     ██╗      ██████╗██████╗      ██████╗ ██████╗ ███╗   ██╗███████╗
     ██║     ██╔════╝██╔══██╗    ██╔════╝██╔═══██╗████╗  ██║██╔════╝
     ██║     ╚█████╗ ██████╔╝    ██║     ██║   ██║██╔██╗ ██║█████╗  
     ██║      ╚═══██╗██╔══██╗    ██║     ██║   ██║██║╚██╗██║██╔══╝  
     ███████╗██████╔╝██████╔╝    ╚██████╗╚██████╔╝██║ ╚████║███████╗
     ╚══════╝╚═════╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                            
                     [ v2.0 | Created by Vorbanux ]
    ===================================================================
    """
    print(banner)

show_preview()

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    menu1 = """
    ┌─────────────────────────────────────────────────────────────┐
    │                        LSB CONSOLE                          │
    └─────────────────────────────────────────────────────────────┘
    
    [»] EXECUTION
    ├─ 1. Encrypt text into image
    └─ 2. Decrypt text from image
    
    [»] INFORMATION
    ├─ 3. Help & Manual
    └─ 4. Version info
    
    [»] SYSTEM
    └─ 0. Exit program
    
    ───────────────────────────────────────────────────────────────
    """
    
    print(menu1)
    con_input = input("Input: ")
    if con_input == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Encrypt text into image\n")
        path = input("image path: ")
        text = input("text: ")
        log = m.image_encript(path, text)
        if log:
            print("Encrypt completed successfully")
        else:
            print("Encrypt don't completed")
        input("Press any key to continue: ")
        menu()
    elif con_input == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Decrypt text from image\n")
        path = input("image path: ")
        log = m.image_decript(path)
        if log:
            print("Encrypt completed successfully.\nText: ", log)
        else:
            print("Encrypt don't completed")
        input("Press any key to continue: ")
        menu()
    elif con_input == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Help & Manual\n")
        print("This console clearly demonstrates how my LSB module works for encrypting text within images. Please enter the correct, and preferably full, path to the image. I don't know what will happen if the path is incomplete. This is my second project posted on GitHub, I hope you enjoyed it")
        input("Press any key to continue: ")
        menu()
    elif con_input == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Version info\n")
        print("Version: 1.0")
        input("Press any key to continue: ")
        menu()
    elif con_input == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exit program\n")
        l = input("Are you sure you want to exit? [y/n]: ")
        if l.lower() == "y":
            print("goodbye!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            menu()
    else:
        menu()

if __name__ == "__main__":
    show_preview()
    time.sleep(3)
    menu()