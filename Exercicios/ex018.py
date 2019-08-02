from math import sin,cos,tan,radians

angulo = float(input("Digite o angulo: "))

seno = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))

print("O SENO de {} é: {:.4f} \ne COSSENO de {} é: {:.4f} \ne TANGENTE de {} é: {:.4f}"
    .format(angulo, seno, angulo, cos, angulo, tg))
