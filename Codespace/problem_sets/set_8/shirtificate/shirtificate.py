# CS50 Shirtificate



# Imports libraries for program
from fpdf import FPDF


# Instantiates pdf as FPDF class object
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Prompts user for name
name = input("Name: ")
# Creates blank page
pdf.add_page()
# Sets initial font
pdf.set_font("helvetica", "", 52)
# Imports image
pdf.image("shirtificate.png", x=10, y=50, w=pdf.epw)
# Writes title
pdf.cell(pdf.epw, 30, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
# Moves cursor
pdf.set_y(90)
# Changes font color to white
pdf.set_text_color(255)
# Changes font size
pdf.set_font("helvetica", "", 24)
# Writes text on shirt
pdf.cell(pdf.epw, 50, f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')
# Creates .pdf
pdf.output("shirtificate.pdf")