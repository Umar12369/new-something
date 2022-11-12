class Program:
   def __init__(self):
       self.user_input = None

   def get_user_input(self):
       while True:
           try:
               self.user_input = int(input("Please enter a number: "))
               break
           except ValueError:
               print("Invalid input, please try again.")

   def run(self):
       self.get_user_input()
       print(f"You entered: {self.user_input}")

if __name__ == "__main__":
   program = Program()
   program.run()
print("Thank You")