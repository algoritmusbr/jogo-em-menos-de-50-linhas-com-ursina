from ursina import *
import random

app = Ursina()
camera.orthographic = True
camera.fov = 10
nave = Entity(model='quad', texture='assets/nave.png', collider='box', scale=(2, 1), y=-3)
espaco1 = Entity(model='quad', texture='assets/espaco.png', scale=15, z=1)
espaco2 = duplicate(espaco1, y=15)
cenario = [espaco1, espaco2]

obstaculos = []

def novo_obstaculo():
    val = random.uniform(-2, 2)
    novo = duplicate(nave, texture='assets/obstaculo.png', x=2 * val, y=25,
                    rotation_z=90 if val < 0 else -90)
    obstaculos.append(novo)
    invoke(novo_obstaculo, delay=0.5)

novo_obstaculo()

def update():
    nave.x -= held_keys['a'] * 5 * time.dt
    nave.x += held_keys['d'] * 5 * time.dt
    for espaco in cenario:
        espaco.y -= 6 * time.dt
        if espaco.y < -15:
            espaco.y += 30
    for obstaculo in obstaculos:
        if obstaculo.x < 0:
            obstaculo.y -= 10 * time.dt
        else:
            obstaculo.y -= 5 * time.dt
        if obstaculo.y < -10:
            obstaculos.remove(obstaculo)
            destroy(obstaculo)
    if nave.intersects().hit:
        nave.shake()

app.run()
