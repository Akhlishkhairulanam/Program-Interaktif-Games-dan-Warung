import random
import main
def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4   
        
        cuppy_position = random.randint(1, 4)
        goa = goa_kosong.copy()
        goa[cuppy_position - 1] = "|0_0|"

        goa_kosong_str = ' '.join(goa_kosong)
        goa = ''.join(goa)
        
        print(f'Coba Perhatikan di bawah ini!\n\n {goa_kosong}\n ')
        
        pilihan_user = input("Menurut kamu CUPPY di Goa mana berada? [1/2/3/4]: ")

        if pilihan_user == cuppy_position:
            print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
        else:
            print(f"\n{goa}\n\nUncchhh kamu kalah 🙊")

        # Tanyakan apakah ingin bermain lagi
        play_again = input("\n\n Apakah mau bermain GAME nya lagi? [y/n]: ")
        
        if play_again == 'n':
            main.menu()

    print("Program Selesai!")

if __name__ == '__main__':
    start()