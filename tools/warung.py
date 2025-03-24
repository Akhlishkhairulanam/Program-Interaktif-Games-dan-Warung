import main
def start():
    while True:
        print('ini warung Akhlish Khairul Anam yang Ganteng Bangett!!!!!')
        play_again = input('kembali ke menu utama? [y/n] ')
        
        if play_again == "y":
            main.menu()      
    
if __name__ == '__main__':
    start()