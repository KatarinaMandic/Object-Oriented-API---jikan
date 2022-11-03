from jikan.Program import Program

while True:
    Program.main_menu()
    choice = Program.user_choice()
    if choice == 'Q':
        Program.exit()
    if choice == '1':
        Program.show_daily_anime()
    if choice == '2':
        Program.get_genre_id()