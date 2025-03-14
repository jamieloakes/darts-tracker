from fpdf import FPDF

import src.analytics.singles_rtw_analysis as singles
import src.analytics.doubles_rtw_analysis as doubles
import src.analytics.legs_analysis as legs


def createCharts() -> None:
    """ Create and save all charts """
    singles.summaryTable()
    singles.dartboardHeatmap()
    doubles.summaryTable()
    doubles.dartboardHeatmap()
    legs.summaryTable()
    legs.timeSeriesAnalysis()