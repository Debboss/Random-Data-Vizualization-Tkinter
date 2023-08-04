import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data2 import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# Define colorful pastel colors for each chart
sales_colors = ["#FFCCCC", "#FFCC99", "#FFFF99", "#CCFFCC"]
inventory_colors = ["#FFB6C1", "#FFD700", "#90EE90", "#87CEFA"]
product_colors = ["#F0E68C", "#98FB98", "#FFB6C1", "#FFA07A"]
year_colors = ["#87CEEB"]
month_colors = ["#DDA0DD"]

# Set the background color to gray for all the figures
plt.rcParams['figure.facecolor'] = 'lightgray'

# chart 1: bar chart of sales data
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values(), color=sales_colors)
ax1.set_title("Sales by product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

# chart 2: horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values(), color=inventory_colors)
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")

# chart 3: pie chart of product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%', colors=product_colors)
ax3.set_title("Product Breakdown")

# chart 4: line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()), color=year_colors[0])
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")

# chart 5: area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(list(inventory_month_data.keys()), list(inventory_month_data.values()), color=month_colors[0])
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")

root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

# Organizing the charts in a 3x2 layout
upper_frame = tk.Frame(root)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side='left', fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side='left', fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side='left', fill="both", expand=True)

lower_frame = tk.Frame(root)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side='left', fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side='left', fill="both", expand=True)

root.mainloop()
