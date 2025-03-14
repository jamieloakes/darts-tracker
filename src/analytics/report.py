from fpdf import FPDF

import src.analytics.singles_rtw_analysis as singles
import src.analytics.doubles_rtw_analysis as doubles
import src.analytics.legs_analysis as legs
import src.utils as utils

H1_SIZE:int = 34 # Text size for page titles
H2_SIZE:int = 26 # Text size for subheadings
TEXT_SIZE:int = 14 # Text size for normal text

def createCharts() -> None:
    """ Create and save all charts """
    singles.summaryTable()
    singles.dartboardHeatmap()
    doubles.summaryTable()
    doubles.dartboardHeatmap()
    legs.summaryTable()
    legs.timeSeriesAnalysis()


def introduction(pdf_obj:FPDF, date:str) -> None:
    """ Introduction page for report """
    pdf_obj.add_page(orientation='portrait', format='A4')
    # Title
    pdf_obj.set_font(family='Helvetica', size=H1_SIZE, style='B')
    pdf_obj.multi_cell(w=0, padding=(3,0,0,0), text=f'Darts Practice Report {date}\n')

    # Introductory Statement
    pdf_obj.set_font(family='Helvetica', size=TEXT_SIZE)
    pdf_obj.multi_cell(w=0, text='This report contains analysis of my darts practice routine.\n')
    pdf_obj.multi_cell(w=0, text='The data was gathered from the practice_data.db database, and visualisations created showing performance against the objectives of each game.\n')
    pdf_obj.multi_cell(w=0, text='Plotly was used to create the visualisations due to its dedicated table visualisation and easy chart formatting\n')


    # Analysis Objectives
    pdf_obj.set_font(family='Helvetica', size=H2_SIZE, style='B')
    pdf_obj.multi_cell(w=0, padding=(12,0,0,0), text='Analysis Objectives\n')
    pdf_obj.set_font(family='Helvetica', size=TEXT_SIZE)
    pdf_obj.multi_cell(w=0, text='The purpose of this report is to assess performance for each practice game and identify areas for improvement. The main objectives can be defined as:\n')
    pdf_obj.multi_cell(w=0, text='- Reduce number of attempts at each single number\n')
    pdf_obj.multi_cell(w=0, text='- Increase number of hits at each double number\n')
    pdf_obj.multi_cell(w=0, text='- Improve scoring average\n')
    pdf_obj.multi_cell(w=0, text='- Improve checkout percentage\n')
    pdf_obj.multi_cell(w=0, text='- Increase number of legs won\n')


    # Table of Contents
    pdf_obj.set_font(family='Helvetica', size=H2_SIZE, style='B')
    pdf_obj.multi_cell(w=0, padding=(12,0,0,0), text='Table of Contents\n')
    pdf_obj.set_font(family='Helvetica', size=TEXT_SIZE)
    pdf_obj.multi_cell(w=0, text='- Page 2: Singles RTW Summary Table\n')
    pdf_obj.multi_cell(w=0, text='- Page 3: Singles RTW Heatmap\n')
    pdf_obj.multi_cell(w=0, text='- Page 4: Doubles RTW Summary Table\n')
    pdf_obj.multi_cell(w=0, text='- Page 5: Doubles RTW Heatmap\n')
    pdf_obj.multi_cell(w=0, text='- Page 6: 501 Summary Table\n')
    pdf_obj.multi_cell(w=0, text='- Page 7: 501 Time Series Analysis\n')


def generateReport() -> None:
    """ Main function for generating report """
    createCharts()
    today:str = utils.getTodaysDate()
    pdf_obj:FPDF = FPDF()
    
    introduction(pdf_obj=pdf_obj, date=today)

    pdf_obj.output(name=f'report_{today}.pdf')


if __name__ == '__main__':
    generateReport()