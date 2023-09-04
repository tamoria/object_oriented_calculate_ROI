class calculateRentalIncome():

    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.total_investment = 0


    def calculate_income(self):
        
        rental_income = input("How much rental income do you expect to receive per month ? ")
        self.total_income += int(rental_income)
        
        laundry_income = input("How much laundry income do you expect to receive per month ? ")
        self.total_income += int(laundry_income)

        storage_income = input("How much storage income do you expect to receive per month ? ")
        self.total_income += int(storage_income)

        misc_income = input("How much miscellaneous income do you expect to receive per month ? ")
        self.total_income += int(misc_income)

        print("Total Income:", self.total_income)


    def calculate_expenses(self):

        tax = input("How much will you pay for taxes per month? ")
        self.total_expenses += int(tax)

        insurance = input("How much will you pay for insurance per month? ")
        self.total_expenses += int(insurance)

        utilities = input("How much will you pay for utilities per month? ")
        self.total_expenses += int(utilities)

        homeowners_association = input("How much will you pay for HOA per month? ")
        self.total_expenses += int(homeowners_association)

        lawn_or_snow = input("How much will you pay for lawn or snow maintenance per month? ")
        self.total_expenses += int(lawn_or_snow)

        vacancy = input("How much will you put towards a possible vacancy per month? ")
        self.total_expenses += int(vacancy)

        repairs = input("How much will you put towards repairs per month? ")
        self.total_expenses += int(repairs)

        capital_expenses = input("How much will you put towards capital expenses (ex: buying a new roof) per month? ")
        self.total_expenses += int(capital_expenses)

        property_management = input("How much will you pay towards property management per month? ")
        self.total_expenses += int(property_management)

        mortgage = input("How much will you pay for mortgage per month? ")
        self.total_expenses += int(mortgage)

        misc_expenses = input("How much will you put towards misc expenses per month? ")
        self.total_expenses += int(misc_expenses)
        

        print("Total Monthly Expenses:", self.total_expenses)

    def calculate_cashflow(self):

        income_expenses = self.total_income - self.total_expenses
        print(f"Monthly Cash Flow: {income_expenses}")

    def calculate_ROI(self):
    

        down_payment = input("How much did you put towards your down payment? ")
        self.total_investment += int(down_payment)

        closing_costs = input("How much did you pay towards closing costs? ")
        self.total_investment += int(closing_costs)

        repair_budget = input("How much did you put towards a repair budget (ex: repainting)? ")
        self.total_investment += int(repair_budget)

        misc = input("How much money did you put towards any miscellaneous reasons? ")
        self.total_investment += int(misc)

        print(f"Total Investment: {self.total_investment}")

        annual_cash_flow = (int(self.total_income) - int(self.total_expenses)) * 12
        print(f"Annual Cash Flow: {annual_cash_flow}")

        cash_on_cash_ROI = int(annual_cash_flow)/int(self.total_investment) * 100
        print(f"Rental Property ROI: {cash_on_cash_ROI}%")

run = calculateRentalIncome()
run.calculate_income()
run.calculate_expenses()
run.calculate_cashflow()
run.calculate_ROI()


