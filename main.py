from Project1 import Poisson, Bernoulli, NBinom, Geometric, MultiNomial
from Project2 import NormalDistribution, TDistribution
from Project3 import T_Distribution
import os
import time


class Menu:

    def main_menu(self):
        print('1.Install Modules')
        print('2.Project 1')
        print('3.Project 2')
        print('4.Project 3')
        print('5.Exit')

    def project_one_menu(self):
        print('1.Bernoulli')
        print('2.Negative Binom')
        print('3.Poisson')
        print('4.Geometric')
        print('5.Multi Nomial')
        print('6.Exit')

    def project_two_menu(self):
        print('1.Normal Distribution')
        print('2.TStudent Distribution')
        print('3.Exit')

    def install_modules(self):
        os.system('pip install -r requirments.txt')
        time.sleep(2)
        print('Installation success!')
        time.sleep(2)
        os.system('cls')

    def start(self):
        while True:
            os.system('cls')
            self.main_menu()
            first_input = int(input('Enter the number: '))
            if first_input == 1:
                self.install_modules()
            elif first_input == 2:
                os.system('cls')
                self.project_one_menu()
                second_input = int(input('Enter the number: '))
                if second_input == 1:
                    func = Bernoulli()
                    func.get_input()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 2:
                    func = NBinom()
                    func.get_input()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 3:
                    func = Poisson()
                    func.get_input()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 4:
                    func = Geometric()
                    func.get_input()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 5:
                    func = MultiNomial()
                    func.get_input()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 6:
                    continue
            elif first_input == 3:
                os.system('cls')
                self.project_two_menu()
                second_input = int(input('Enter the number: '))
                if second_input == 1:
                    func = NormalDistribution()
                    func.input_user()
                    func.get_pmf()
                    func.draw_diagram()
                elif second_input == 2:
                    func = TDistribution()
                    func.input_user()
                    func.draw_diagram()
                elif second_input == 3:
                    continue
            elif first_input == 4:
                os.system('cls')
                func = T_Distribution()
                func.get()
                key = input('Press "Enter" to continue')
            elif first_input == 5:
                break


if __name__ == '__main__':
    m = Menu()
    m.start()



