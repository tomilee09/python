from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':

  output_file('graficado.html')
  fig = figure()
  x = [0, 1, 2, 3, 4]
  y = [0, 1, 4, 9, 16]
  fig.line(x, y)
  show(fig)
  
  
  " hola " sdsd
  """ hola 'sd sdsdñdsds sdsds'sdsd"""