from passwordbruteforce.producer import Producer

prod = Producer("127.0.0.1:5552")
prod.solve_passwords("passwords.txt", "list", "password_files/wordlist.txt")