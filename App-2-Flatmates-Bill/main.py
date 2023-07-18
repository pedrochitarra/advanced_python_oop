from fpdf import FPDF
import webbrowser


class Bill:
    """Object that contains data about a bill, such as total amount."""
    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period


class Flatmate:
    """Represents a person who lives in a flat with another person and
    pays part of the bill."""
    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house/\
                (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount * weight


class PdfReport:
    """Represents the report with the amount that each flatmate has to pay,
    also the information of the complete bill."""
    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("files/house.png", w=30, h=30)

        # Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C',
                 ln=1)
        # Insert period and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=f'{bill.period}', border=1, ln=1)

        # Insert amount and value of the first flatmate
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40,
                 txt=f'{round(flatmate1.pays(bill, flatmate2), 2)}',
                 border=1, ln=1)

        # Insert amount and value of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40,
                 txt=f'{round(flatmate2.pays(bill, flatmate1), 2)}',
                 border=1, ln=1)
        pdf.output(self.filename)
        webbrowser.open(self.filename)


bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print("John pays :", john.pays(bill, mary))
print("Mary pays :", mary.pays(bill, john))

report = PdfReport("test.pdf")
report.generate(john, mary, bill)
