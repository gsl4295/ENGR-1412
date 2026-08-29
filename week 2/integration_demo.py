# unnecessarily doing calculus outside of class. we'll say it's for honors credit (it's not)
# using ai is for losers :)
# use your brain, i promise you'll like it
# {from aspen <3}

import csv
import matplotlib.pyplot
import pandas

class Function:
    def __init__(self, function: str, dx: float, domain: tuple):
        self.function = function
        self.dx = dx
        self.domain = domain
        self.x = []
        self.y = []
        self.approximations = []
        self.area_under_curve = 0

    def evaluate_function(self):
        for i in range(int((self.domain[1] - self.domain[0]) / self.dx) + 1):
            x_value = round(i * self.dx, 10) + self.domain[0] # little fix for lower bounds not equal to 0
            self.x.append(x_value) # needs more testing here... who knows what values im forgetting
        for value in self.x:
            formatted_equation = self.function.replace("x",str(value))
            self.y.append(round(eval(formatted_equation), 10))

    def integrate(self):
        for i in range(len(self.x)):
            if i == len(self.x) - 1:
                pass
            else:
                x1 = self.x[i]
                x2 = self.x[i+1]
                y1 = self.y[i]
                y2 = self.y[i+1]
                trapezoidal_area = round((x2 - x1) * (y2 + y1) / 2, 10)
                self.approximations.append(trapezoidal_area)
                self.area_under_curve += trapezoidal_area

    def report_results(self):
        print("--------------- Details ----------------")
        print(f"function = {self.function}")
        print(f"dx = {self.dx}")
        print(f"domain = {self.domain}")
        print("\n--------------- Results ----------------")
        print(f"area under curve = {round(self.area_under_curve, 10)}")
        print("\n--------------- Options ----------------")
        graphing_option = input("(y/n) - graph results? - ")
        if graphing_option == "y":
            self.convert_to_csv()
            self.graph_results()

    def convert_to_csv(self):
        header = ["x","y"]
        data = []
        for row in range(len(self.x)):
            data.append([round(self.x[row], 10), round(self.y[row], 10)])
        with open('integration_output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

    @staticmethod
    def graph_results():
        graph = pandas.read_csv('integration_output.csv')
        graph.plot(x="x", y="y")
        matplotlib.pyplot.grid()
        matplotlib.pyplot.show() # i did it!!!

f = Function("(x*x)", 0.1, (0, 1)) # hardcoding this for now. it'll have text input as an optional thing at some point.
f.evaluate_function()
f.integrate()
f.report_results()