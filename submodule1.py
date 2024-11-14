# This file should provided functionality to
# Submodule1 itself and
# ParentModules that include this submodule1

class SubModule1:
    name: str = "SubModule1"

    def say_hello(self):
        print("Hello, I'm the " + name + ".")

if __name__ == "__main__":
    # Instantiate SubModule1
    sub_module = SubModule1()

    # Hello from all modules
    sub_module.say_hello()
