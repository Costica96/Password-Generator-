# This program is a Password Generator and will generate a random password!
import random
from tkinter import N
UPPER_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",\
     "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LOWER_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",\
     "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "&", "_", "-"]
i = 0
indice_lista = ""
password = ""
print("Bun venit la generatorul de parole!")

nr_upper_let = int(input("Cate litere mari doriti sa contina parola dumneavoastra: "))
if nr_upper_let >= 0 :
     upper_let_list = random.choices(UPPER_LETTERS, weights = None, k = nr_upper_let)
     nr_lower_let = int(input("Cate litere mici doriti sa contina parola dumneavoastra: "))
     if nr_lower_let >= 0 :
          lower_let_list = random.choices(LOWER_LETTERS, weights = None, k = nr_lower_let) 
          nr_numbers = int(input("Cate numere doriti sa contina parola dumneavoastra: "))
          if nr_numbers >= 0 :
               nr_numb_list = random.choices(NUMBERS, weights = None, k = nr_numbers)
               special_characters = input("Doriti sa utilizati caractere speciale (Da/Nu): ").title()
               if special_characters == "Da" :
                    nr_special_characters = int(input("Cate caractere speciale doriti sa contina parola dumneavoastra: "))
                    if nr_special_characters >= 0:
                         sp_charact_list = random.choices(SPECIAL_CHARACTERS, weights = None, k = nr_special_characters)
                         final_list = upper_let_list + lower_let_list + nr_numb_list + sp_charact_list 
                         random.shuffle(final_list)
                    else :
                         print("Verificati numarul de caractere speciale pe care il doriti!")
               elif special_characters == "Nu" :
                    final_list = upper_let_list + lower_let_list + nr_numb_list
                    random.shuffle(final_list)
               else :
                    print("Revina cand te hotarasti daca doresti caractere speciale!")
          else :
               print("Verificati numarul de cifre pe care il doriti!")
     else :
          print("Verificati numarul de litere mici pe care il doriti!")
else :
     print("Verificati numarul de litere mari pe care il doriti!")


while i < len(final_list) :
     indice_lista = final_list[i]
     password = password + indice_lista
     i = i + 1

print(password)
