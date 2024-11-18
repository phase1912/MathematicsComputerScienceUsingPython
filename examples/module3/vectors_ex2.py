import plotly.graph_objects as go
import numpy as np


# Створення об'єкта "Figure" для графіка
fig = go.Figure()


# Додавання горизонтальної осі X
fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', name='X-вісь'))


# Додавання вертикальної осі Y
fig.add_trace(go.Scatter(x=[0, 0], y=[-10, 10], mode='lines', name='Y-вісь'))


# Відмітка для початку координат
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=8, color='red'), name='Початок координат'))


# Додавання координатної сітки
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')


# Зображення деяких точок
points_x = np.random.randint(-8, 8, 5)
points_y = np.random.randint(-8, 8, 5)


fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', marker=dict(size=10, color='blue'), name='Точка'))


# Налаштування вигляду графіка
fig.update_layout(
    title='Координатна система на площині з точками',
    xaxis=dict(title='Вісь X'),
    yaxis=dict(title='Вісь Y'),
    showlegend=True
)


# Відображення графіка
fig.show()