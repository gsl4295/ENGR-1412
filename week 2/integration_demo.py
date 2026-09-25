import csv
import matplotlib.pyplot
import pandas

class Function:
    def __init__(self, function: str, domain: tuple):
        self.function = function
        self.domain = domain
        self.x = []
        self.y = []
        self.approximations = []
        self.area_under_curve = 0
        self.dx = self.domain[1] - self.domain[0]
        self.dx_results = {}
        self.counter = 0
        self.calculation_counter = 0

    def evaluate_function(self):
        for i in range(int((self.domain[1] - self.domain[0]) / self.dx) + 1):
            x_value = round(i * self.dx, 10) + self.domain[0] # little fix for lower bounds not equal to 0
            self.x.append(x_value) # needs more testing here... who knows what values im forgetting
        for value in self.x:
            formatted_equation = self.function.replace("x",str(value))
            try:
                self.y.append(round(eval(formatted_equation), 10))
            except ZeroDivisionError:
                self.y.append(0)

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
        return round(self.area_under_curve, 10)

    def reset_results(self):
        self.area_under_curve = 0
        self.x.clear()
        self.y.clear()
        self.calculation_counter += len(self.approximations)
        self.approximations.clear()

    def dx_optimizer(self):
        self.counter += 1
        self.dx *= (1/2)
        self.dx = round(self.dx, 10)
        self.evaluate_function()
        self.dx_results[self.counter] = self.integrate()
        if self.counter == 1:
            self.reset_results()
            self.dx_optimizer()
        else:
            previous_area = self.dx_results[self.counter - 1]
            current_area = self.dx_results[self.counter]
            try:
                percent_area_difference = abs(current_area / previous_area)
            except ZeroDivisionError:
                percent_area_difference = 0
            if percent_area_difference < 0.9999:
                self.reset_results()
                self.dx_optimizer()
            else:
                self.calculation_counter += len(self.approximations)
                self.report_results()

    def report_results(self):
        print("--------------- Details ----------------")
        print(f"function = {self.function}")
        print(f"domain = {self.domain}")
        print(f"total trapezoids calculated = {self.calculation_counter}")
        print(f"trapezoids in this graph = {len(self.approximations)}")
        print("\n--------------- Results ----------------")
        print(f"optimized dx = {self.dx}")
        print(f"approximated area under curve = {round(self.area_under_curve, 10)}")
        print("\n--------------- Options ----------------")
        print("Integral solved :)")
        graphing_option = input("(y/n) - graph results? - ")
        if graphing_option == "y":
            self.convert_to_csv()
            self.graph_results()
        else:
            exit(0)

    def convert_to_csv(self):
        header = ["x","f(x)"]
        data = []
        for row in range(len(self.x)):
            data.append([round(self.x[row], 10), round(self.y[row], 10)])
        with open('integration_output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

    def graph_results(self):
        graph = pandas.read_csv('integration_output.csv')
        graph.plot(x="x", y="f(x)", title=f"dx = {self.dx}  |  A = {round(self.area_under_curve, 10)}")
        matplotlib.pyplot.grid()
        matplotlib.pyplot.show() # i did it!!! aaaaaaaaaa


f = Function("(x*x)+(6*x)+9", (-10, 10)) # hardcoding this stuff for now. it'll have text input as an optional thing at some point.
f.dx_optimizer()