import math
import plotly.graph_objects as go


if __name__ == '__main__':
    all_n = [i for i in range(3, 50)]

    alpha = []
    beta = []
    for n in all_n:
        sum_val_alpha = 0
        for k in range(n):
            sum_val_alpha += 1.0 / math.comb(n-1, k)

        alpha.append(2.0 * sum_val_alpha / (n ** 2))

        sum_val_beta = 0
        for k in range(n-1):
            v1 = math.comb(n-1, k+1)
            v2 = math.comb(n-1, k)
            sum_val_beta += math.comb(n - 2, k) * (1.0 / v1 - 1.0 / v2) ** 2
        beta.append(sum_val_beta / (n ** 2))

    y = [math.sqrt(alpha[n-3] + (n-1) * beta[n-3]) for n in all_n]

    line_color = 'teal'
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=all_n, y=y, mode='lines+markers', marker_color=line_color, marker_line_color=line_color))

    fig.update_layout(font_size=25, showlegend=False, xaxis_title='Number of features', yaxis_title='Bound')
    fig.write_image('lipschitz_bounds.png')
