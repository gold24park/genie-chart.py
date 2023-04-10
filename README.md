# 🧞 지니뮤직 차트 API: genie-chart.py
![genie](./image.jpg)

genie-chart.py is a Python API that retrieves the TOP 100 chart information from the [Genie](https://www.genie.co.kr/).

## Installation
```commandline
pip install genie-chart.py
```

## Quickstart
The main usage of genie-chart.py is similar to [billboard.py](https://github.com/guoguo12/billboard-charts).
```commandline
>>> from genie import *
>>> chart = ChartData(chartPeriod=GenieChartPeriod.Monthly)
>>> print(chart[0].json())
{
    "artist": "NewJeans",
    "image": "https://image.genie.co.kr/Y/IMAGE/IMG_ALBUM/083/325/577/83325577_1672649874616_1_140x140.JPG/dims/resize/Q_80,0",
    "lastPos": 1,
    "peakPos": 1,
    "rank": 1,
    "title": "Ditto"
}
>>> print(chart.date)
2023-04-09 00:00:00
```

### ChartData Arguments
- `date` – The chart date
- `chartPeriod`
  - GenieChartPeriod.Realtime – 실시간
  - GenieChartPeriod.Daily – 일간
  - GenieChartPeriod.Weekly – 주간
  - GenieChartPeriod.Monthly – 월간
  - GenieChartPeriod.Alltime – 누적
- `fetch` – A boolean value that indicates whether to retrieve the chart data immediately. If set to `False`, you can fetch the data later using the `fetchEntries()` method.

### Chart entry attributes
`ChartEntry` can be accessed using the `ChartData[index]` syntax. A `ChartEntry` instance has the following attributes:
- `title` – The title of the track
- `artist` – The name of the artist
- `image` – The URL of the cover image for the track
- `peakPos` - The track's peak position on the chart.
- `lastPos` - The track's last position on the previous period.
- `rank` – The track's current rank position on the chart.

### K-Pop music chart Python APIs
- [Melon | melon-chart.py](https://github.com/gold24park/melon-chart.py)
- [Bugs | bugs-chart.py](https://github.com/gold24park/bugs-chart.py)
- [Genie | genie-chart.py](https://github.com/gold24park/genie-chart.py)
- [Vibe | vibe-chart.py](https://github.com/gold24park/vibe-chart.py)
- [Flo | flo-chart.py](https://github.com/gold24park/flo-chart.py)

## Dependencies
- [requests](https://requests.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.
