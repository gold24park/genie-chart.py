import genie

if __name__ == '__main__':
    chart = genie.ChartData(chartPeriod=genie.GenieChartPeriod.Monthly)
    print(chart.date)

    for entry in chart:
        print(entry.json())

