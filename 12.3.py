import tkinter as tk
from tkinter import messagebox

class IceCreamStand:
    def __init__(self):
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint']
        self.scoops_sold = {flavor: 0 for flavor in self.flavors}

    def get_flavors(self):
        return self.flavors

    def get_scoops_sold(self):
        return self.scoops_sold

    def sell_scoop(self, flavor):
        if flavor in self.flavors:
            self.scoops_sold[flavor] += 1
            return True
        else:
            return False

class IceCreamStandGUI(tk.Frame):
    def __init__(self, master, ice_cream_stand):
        super().__init__(master)
        self.master = master
        self.ice_cream_stand = ice_cream_stand
        self.create_widgets()

    def create_widgets(self):
        # Создание метки с заголовком
        self.header_label = tk.Label(self, text='Available flavors:')
        self.header_label.grid(row=0, column=0, pady=10)

        # Создание кнопок для каждого вкуса мороженого
        flavors = self.ice_cream_stand.get_flavors()
        for i, flavor in enumerate(flavors):
            button = tk.Button(self, text=flavor, command=lambda flavor=flavor: self.sell_scoop(flavor))
            button.grid(row=i+1, column=0, padx=5, pady=5)

    def sell_scoop(self, flavor):
        success = self.ice_cream_stand.sell_scoop(flavor)
        if success:
            messagebox.showinfo('Sale', 'One scoop of {} sold!'.format(flavor))

# Пример использования класса и графического интерфейса
if __name__ == '__main__':
    ice_cream_stand = IceCreamStand()
    root = tk.Tk()
    app = IceCreamStandGUI(root, ice_cream_stand)
    app.pack()
    root.mainloop()