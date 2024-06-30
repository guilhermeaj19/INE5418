from passwordbruteforce.password_solver import PasswordSolver

passwd_solver = PasswordSolver("127.0.0.1:5551")
passwd_solver.wait_password()
