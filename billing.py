class payment:
    def __init__(self, amountneeded, amountpaid=0.0):
        self.amountneeded = float(amountneeded)
        self.amountpaid = float(amountpaid)

    def tax(self):
        return self.amountneeded * 0.1

    def tipping(self, percent_choice):
        tip_percentages = {1: 0.05, 2: 0.10, 3: 0.15, 4: 0.20}
        percent = tip_percentages.get(percent_choice, 0.0)
        return self.amountneeded * percent

    def askForTip(self):
        istip = input("would you like to tip *(yes / no): ").strip().lower()
        if istip == "yes":
            print("How much would you like to tip?")
            print("1- 5%      2- 10%\n3- 15%       4- 20%")
            percent = int(input())
            tip = self.tipping(percent)
            return tip
        return 0.0

    def calculate_total(self):
        tip = self.askForTip()
        return self.amountneeded + self.tax() + tip

    def change(self, total_due):
        return self.amountpaid - total_due

    def sendMoney(self, finance_account, amount):
        finance_account.add_money(amount)


class cashpayment(payment):
    def process_cash(self, drawer: Drawer):
        total_due = self.calculate_total()
        print(f"Total Due (with tax & tip): ${total_due:.2f}")
        
        self.amountpaid = float(input(f"Enter cash presented by customer: "))
        change_due = self.change(total_due)
        
        if change_due < 0:
            print(f"Not enough cash! Short by ${abs(change_due):.2f}")
            return False
        
        self.sendMoney(drawer, self.amountpaid)
        if change_due > 0:
            drawer.remove_money(change_due)
            print(f"Change returned: ${change_due:.2f}")
        return True


class cardPayment(payment):
    def process_card(self, bank: Bank):
        total_due = self.calculate_total()
        print(f"Total Due (with tax & tip): ${total_due:.2f}")
        self.amountpaid = total_due
        self.sendMoney(bank, total_due)
        return True
