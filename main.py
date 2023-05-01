import os, time
todo = []

def add():
  time.sleep(1)
  os.system("clear")
  

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  elif menu == "4":
    remove
  else:
    print("That is not a valid input")
    time.sleep(1)
    os.system("clear")
    continue