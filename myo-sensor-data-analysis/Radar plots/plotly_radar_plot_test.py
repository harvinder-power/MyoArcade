import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Scatterpolar(
  r = [39, 28, 8, 7, 28, 39],
  theta = ['A','B','C', 'D', 'E', 'A'],
  fill = 'toself'
)]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0, 50]
    )
  ),
  showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename = "basic")
