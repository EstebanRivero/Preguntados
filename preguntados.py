import pygame
from funcionespreguntados.funcionespreguntados import*
from datos_preguntados import lista

pygame.init() #Se inicializa pygame
pygame.display.set_caption("Preguntados")
largo = 1280
ancho = 720
config_pantalla = [largo, ancho]
screen = pygame.display.set_mode(config_pantalla) #Se crea una ventana


#!LISTAS

conteo_preguntas = 0
pregunta_a_mostrar = lista[conteo_preguntas]
jugadores = cargar_json("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/proyecto-preguntados.json")

#!Bandera Validas

opcion_a_bandera = True
opcion_b_bandera = True
opcion_c_bandera = True

# medidas_a = 156, 345, 320, 60
# medidas_b = 156, 448, 320, 60
# medidas_c = 156, 549, 320, 60

#!---MEDIDAS UBICACION PREGUNTAS---

ubicacion_a_x = 156
ubicacion_a_y = 345
largo_a = 360
ancho_a = 53

#!---MEDIDAS UBICACION SCORE---

ubicacion_score_x = 150
ubicacion_score_y = 170

#!---MEDIDAS UBICACION USUARIO---

rect_ubicacion_usuario_x = 400
rect_ubicacion_usuario_y = 550

#!---MEDIDAS UBICACION SILENCIAR---

rect_ubicacion_silenciar_x = 10
rect_ubicacion_silenciar_y = 10

#!RECTS

rect_boton_jugar = pygame.Rect(490, 600, 300, 70)
rect_boton_puntaje = pygame.Rect(100, 600, 300, 70)
rect_boton_salir = pygame.Rect(1000, 40, 100, 50)
rect_boton_pregunta = pygame.Rect(977, 57, 250, 70)
rect_boton_respuesta_a = pygame.Rect(ubicacion_a_x, ubicacion_a_y, largo_a, ancho_a)
rect_boton_respuesta_b = pygame.Rect(ubicacion_a_x, ubicacion_a_y+103, largo_a, ancho_a)
rect_boton_respuesta_c = pygame.Rect(ubicacion_a_x, ubicacion_a_y+204, largo_a, ancho_a)
rect_boton_volver = pygame.Rect(984, 573, 150, 80)
rect_reinicio = pygame.Rect(53, 57, 250, 70)
rect_ingreso_usuario = pygame.Rect(rect_ubicacion_usuario_x, rect_ubicacion_usuario_y, 300, 50)
rect_silenciar_musica = pygame.Rect(rect_ubicacion_silenciar_x, rect_ubicacion_silenciar_y, 140, 30)

#!VARIABLES DE ACTIVACION VARIAS.

respuesta_correcta_a = "a"
respuesta_correcta_b = "b"
respuesta_correcta_c = "c"
texto_nombre_usuario = ""

#!SONIDO

pygame.mixer.init
pygame.mixer.music.set_volume(0.1)

sonido_error = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/ErrorSound (online-audio-converter.com).mp3")
sonido_error.set_volume(2)
sonido_correcta = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/Correct_answer (online-audio-converter.com).mp3")
sonido_correcta.set_volume(2)
campeones_musica = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/Sonido_Guile (online-audio-converter.com).mp3")
campeones_musica.set_volume(1)
sonido_juego = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/Metal Hellsinger Intro.mp3")
sonido_juego.set_volume(0.05)
sonido_finalizado = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/Sweet Victory.mp3")
sonido_finalizado.set_volume(0.05)
sonido_jugando = pygame.mixer.Sound("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/Y2meta.app - Street Fighter 5 - Ken's Theme (SFV OST) (320 kbps).mp3")
sonido_jugando.set_volume(0.05)

#!COLORES:

naranja = (255, 119, 19)
azul = (25, 77, 255)
rojo = (255, 20, 25)
amarillo = (227, 245, 13)
negro = (0, 0, 0)
verde = (0, 207, 41)

#!FUENTE

font = pygame.font.SysFont("Default", 50)
font_respuestas = pygame.font.SysFont("Default", 45)
fuente2 = pygame.font.SysFont("Default", 50)
text_start = font.render("Start", True, (amarillo))
text_puntaje = font.render("Puntaje", True, (rojo))
text_salir = font.render("Salir", True, (amarillo))
textpregunta = font.render("Pregunta", True, (amarillo))
textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
textovolver = font.render("Volver", True, (amarillo))
textreinicio = font.render("Reiniciar", True, (amarillo))
textoingreso = font.render("Ingrese su usuario:", True, (amarillo), (rojo))
usuarionombre_usuariotexto_nombre_usuario = font.render(texto_nombre_usuario, True, (amarillo))
texto_silenciar = font_respuestas.render("Silenciar", True, (rojo))

#!SCORE

numeros_score = 000
textoscore = font.render("Score:", True, (amarillo), rojo)
textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)

#!ERRORES

incorrectas = 0

#!BANDERAS

esta_jugando = False #BANDERA CUANDO ESTE JUGANDO
control_reinicio = False #BANDERA PARA CONTROL DE REINICIO
juego_finalizado = False #BANDERA CUANDO FINALIZE EL JUEGO
entrada_de_usuario = False #BANDERA CUANDO VAYA A INGRESAR EL USUARIO
bandera_volver = True #BANDERA PARA VOLVER AL MENU PRINCIPAL (SIN INTERRUMPIR EL GAME)
pantalla_puntaje = False #BANDERA PARA CUANDO ENTRE A PUNTAJE
running = True #BANDERA DE CONTROL DE WHILE
bandera_puntaje = False #BANDERA DE CONTROL DE PUNTAJE
control_musica = False #BANDERA CONTROL DE MUSICA
preguntas = False

sonido_juego.play(10)#!------------MUSICA MENU PRINCIPAL--------------

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: #!SE VERIFICA SI EL USUARIO CERRO LA VENTANA
           running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(f"Mouse down: {event.pos}")

            if rect_boton_jugar.collidepoint(event.pos): #!-----------------------------------COLLIDE JUGAR
                esta_jugando = True
                control_reinicio = True
                sonido_juego.stop()
                sonido_jugando.play(10)

                if bandera_volver == False and juego_finalizado == False:
                    #print("Se reinicia por tramposo")
                    bandera_volver == True
                    incorrectas = 0
                    opcion_a_bandera = True
                    opcion_b_bandera = True
                    opcion_c_bandera = True
                    conteo_preguntas = 0
                    numeros_score = 000
                    pregunta_a_mostrar = lista[conteo_preguntas]
                    textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                    textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                    textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                    textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                    textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))

            if esta_jugando == True and juego_finalizado == False:        
                if rect_boton_pregunta.collidepoint(event.pos): #!---------------------------------COLLIDE PREGUNTA
                    if conteo_preguntas < len(lista)-1:
                        bandera_volver = True
                        opcion_a_bandera = True
                        opcion_b_bandera = True
                        opcion_c_bandera = True
                        incorrectas = 0
                        conteo_preguntas +=1
                        pregunta_a_mostrar = lista[conteo_preguntas]
                        textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                        textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                        textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                        textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                    else:
                        juego_finalizado = True
                        bandera_volver = False
                        opcion_a_bandera = False
                        opcion_b_bandera = False
                        opcion_c_bandera = False
                        control_reinicio = False
                        sonido_finalizado.play(10)
                        sonido_jugando.stop()
                        sonido_juego.stop()

            if opcion_a_bandera == True and esta_jugando == True:
                if rect_boton_respuesta_a.collidepoint(event.pos): #!-------------------------COLLIDE RESPUESTA A
                    #print("Colisiono con a")
                    if respuesta_correcta_a == pregunta_a_mostrar["correcta"]:
                        sonido_correcta.play()
                        #print("Respondio correctamente")
                        if conteo_preguntas < len(lista)-1:
                            bandera_volver = True
                            opcion_b_bandera = True
                            opcion_c_bandera = True
                            conteo_preguntas += 1
                            pregunta_a_mostrar = lista[conteo_preguntas]
                            numeros_score += 10
                            incorrectas = 0
                            textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                            textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                            textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                            textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                            textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                        else:
                            numeros_score += 10
                            bandera_volver = False
                            juego_finalizado = True
                            opcion_a_bandera = False
                            opcion_b_bandera = False
                            opcion_c_bandera = False
                            control_reinicio = False
                            sonido_finalizado.play(10)
                            sonido_jugando.stop()
                    else:
                        #print("respuesta incorrecta")
                        sonido_error.play()
                        textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (rojo))
                        opcion_a_bandera = False
                        incorrectas += 1
                        #print(incorrectas)
                        if incorrectas == 2:
                            if conteo_preguntas < len(lista)-1: 
                                conteo_preguntas += 1
                                pregunta_a_mostrar = lista[conteo_preguntas]
                                incorrectas = 0 
                                textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                                textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                                textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                                textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                                textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                                opcion_a_bandera = True
                                opcion_b_bandera = True
                                opcion_c_bandera = True
                            else:
                                bandera_volver = False
                                juego_finalizado = True
                                opcion_a_bandera = False
                                opcion_b_bandera = False
                                opcion_c_bandera = False
                                control_reinicio = False
                                sonido_finalizado.play(10)
                                sonido_jugando.stop()

            if opcion_b_bandera == True and esta_jugando == True:
                if rect_boton_respuesta_b.collidepoint(event.pos): #!--------------------------COLLIDE PREGUNTA B
                    #print("colisiono con B")
                    if respuesta_correcta_b == pregunta_a_mostrar["correcta"]:
                        sonido_correcta.play()
                        #print("Respondio correctamente")
                        if conteo_preguntas < len(lista)-1:
                            bandera_volver = True
                            opcion_a_bandera = True
                            opcion_c_bandera = True
                            conteo_preguntas += 1
                            pregunta_a_mostrar = lista[conteo_preguntas]
                            numeros_score += 10
                            incorrectas = 0
                            textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                            textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                            textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                            textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                            textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                        else:
                            numeros_score += 10
                            bandera_volver = False
                            juego_finalizado = True
                            opcion_a_bandera = False
                            opcion_b_bandera = False
                            opcion_c_bandera = False
                            control_reinicio = False
                            sonido_finalizado.play(10)
                            sonido_jugando.stop()
                    else:
                        #print("respuesta incorrecta")
                        sonido_error.play()
                        opcion_b_bandera = False
                        textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (rojo))
                        incorrectas += 1
                        #print(incorrectas)
                        if incorrectas == 2:
                            if conteo_preguntas < len(lista)-1:
                                conteo_preguntas += 1
                                pregunta_a_mostrar = lista[conteo_preguntas]
                                incorrectas = 0 
                                textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                                textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                                textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                                textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                                textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                                opcion_a_bandera = True
                                opcion_b_bandera = True
                                opcion_c_bandera = True
                            else:
                                bandera_volver = False
                                juego_finalizado = True
                                opcion_a_bandera = False
                                opcion_b_bandera = False
                                opcion_c_bandera = False
                                control_reinicio = False
                                sonido_finalizado.play(10)
                                sonido_jugando.stop()

            if opcion_c_bandera == True and esta_jugando == True:
                if rect_boton_respuesta_c.collidepoint(event.pos): #!---------------------COLLIDE RESPUESTA C
                    #print("colisiono con c")
                    if respuesta_correcta_c == pregunta_a_mostrar["correcta"]:
                        sonido_correcta.play()
                        #print("Respondio correctamente")
                        if conteo_preguntas < len(lista)-1:
                            bandera_volver = True
                            opcion_a_bandera = True
                            opcion_b_bandera = True
                            conteo_preguntas += 1
                            pregunta_a_mostrar = lista[conteo_preguntas]
                            numeros_score += 10
                            incorrectas = 0
                            textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                            textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                            textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                            textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                            textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                        else:
                            numeros_score += 10
                            bandera_volver = False
                            juego_finalizado = True
                            opcion_a_bandera = False
                            opcion_b_bandera = False
                            opcion_c_bandera = False
                            control_reinicio = False
                            sonido_finalizado.play(10)
                            sonido_jugando.stop()
                    else:
                        #print("respuesta incorrecta")
                        sonido_error.play()
                        textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (rojo))
                        opcion_c_bandera = False
                        incorrectas += 1
                        #print(incorrectas)
                        if incorrectas == 2:
                            if conteo_preguntas < len(lista)-1:
                                conteo_preguntas += 1
                                pregunta_a_mostrar = lista[conteo_preguntas]
                                incorrectas = 0 
                                textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                                textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                                textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                                textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                                textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))
                                opcion_a_bandera = True
                                opcion_b_bandera = True
                                opcion_c_bandera = True
                            else:
                                bandera_volver = False
                                juego_finalizado = True
                                opcion_a_bandera = False
                                opcion_b_bandera = False
                                opcion_c_bandera = False
                                control_reinicio = False
                                sonido_finalizado.play(10)
                                sonido_jugando.stop()

            if control_reinicio == True:
                if rect_reinicio.collidepoint(event.pos): #!--------------------------------------COLLIDE REINICIO 
                    #print("Colisiono reinicio")
                    bandera_volver = True
                    incorrectas = 0
                    opcion_a_bandera = True
                    opcion_b_bandera = True
                    opcion_c_bandera = True
                    conteo_preguntas = 0
                    numeros_score = 000
                    pregunta_a_mostrar = lista[conteo_preguntas]
                    textoscore_2 = font.render(str(numeros_score), True, (amarillo), rojo)
                    textpreguntajugando = font.render(pregunta_a_mostrar["pregunta"], True, (azul))
                    textorespuesta_a = font_respuestas.render(f"A. {pregunta_a_mostrar["a"]}", True, (azul))
                    textorespuesta_b = font_respuestas.render(f"B. {pregunta_a_mostrar["b"]}", True, (azul))
                    textorespuesta_c = font_respuestas.render(f"C. {pregunta_a_mostrar["c"]}", True, (azul))

            if rect_boton_volver.collidepoint(event.pos): #!----------------------------------COLLIDE VOLVER
                #print("Colisiono con volver")
                # menu_principal = True
                control_reinicio = False
                juego_finalizado = False
                esta_jugando = False
                pantalla_puntaje = False
                opcion_a_bandera = True
                opcion_b_bandera = True
                opcion_c_bandera = True
                bandera_puntaje = False
                campeones_musica.stop()
                sonido_juego.play(10)
                sonido_finalizado.stop()
                sonido_jugando.stop()

            if rect_silenciar_musica.collidepoint(event.pos):#!---------------------------------SILENCIAR MUSICA
                # if control_musica == False:
                #     campeones_musica.set_volume(0)
                #     sonido_juego.set_volume(0)
                #     sonido_finalizado.set_volume(0)
                #     sonido_correcta.set_volume(0)
                #     sonido_error.set_volume(0)
                #     sonido_jugando.set_volume(0)
                #     control_musica = True
                #     texto_silenciar = font_respuestas.render("Desenmudecer", True, (amarillo), rojo)
                # else:
                #     campeones_musica.set_volume(1)
                #     sonido_juego.set_volume(0.05)
                #     sonido_finalizado.set_volume(0.05)
                #     sonido_correcta.set_volume(2)
                #     sonido_error.set_volume(2)
                #     sonido_jugando.set_volume(0.05)
                #     control_musica = False
                #     texto_silenciar = font_respuestas.render("Silenciar", True, (amarillo), rojo)
                if control_musica == False:
                    texto_silenciar = font_respuestas.render("Desenmudecer", True, (rojo), amarillo)
                else:
                    texto_silenciar = font_respuestas.render("Silenciar", True, (rojo), amarillo)

                control_musica = controlar_musica(control_musica, campeones_musica, sonido_juego, sonido_finalizado, sonido_correcta, sonido_error, sonido_jugando)


            if bandera_puntaje == False:    
                if rect_boton_puntaje.collidepoint(event.pos): #!---------------------------------COLLIDE PUNTAJE
                    if esta_jugando == False and juego_finalizado == False:
                        ordenar_diccionarios(jugadores, "Score", "<")
                        sonido_juego.stop()
                        campeones_musica.play(10)
                        pantalla_puntaje = True
                        opcion_a_bandera = False
                        opcion_b_bandera = False
                        opcion_c_bandera = False
                        bandera_puntaje = True
                        if len(jugadores) >= 3:
                            primer_jugador = jugadores[0]["nombre_jugador"]
                            primer_score = jugadores[0]["Score"]
                            segundo_jugador = jugadores[1]["nombre_jugador"]
                            segundo_score = jugadores[1]["Score"]
                            tercer_jugador = jugadores[2]["nombre_jugador"]
                            tercer_score = jugadores[2]["Score"]
                            texto_primer_jugador = font.render(f"{primer_jugador} - {str(primer_score)}", True, (amarillo), (rojo))
                            texto_segundo_jugador = font.render(f"{segundo_jugador} - {str(segundo_score)}", True, (amarillo), (rojo))
                            texto_tercer_jugador = font.render(f"{tercer_jugador} - {str(tercer_score)}", True, (amarillo), (rojo))
                        elif len(jugadores) == 2:
                            primer_jugador = jugadores[0]["nombre_jugador"]
                            primer_score = jugadores[0]["Score"]
                            segundo_jugador = jugadores[1]["nombre_jugador"]
                            segundo_score = jugadores[1]["Score"]
                            texto_primer_jugador = font.render(f"{primer_jugador} - {str(primer_score)}", True, (amarillo), (rojo))
                            texto_segundo_jugador = font.render(f"{segundo_jugador} - {str(segundo_score)}", True, (amarillo), (rojo))
                            texto_tercer_jugador = font.render("Sin jugador", True, (amarillo), (rojo))
                        elif len(jugadores) == 1:
                            primer_jugador = jugadores[0]["nombre_jugador"]
                            primer_score = jugadores[0]["Score"]
                            texto_primer_jugador = font.render(f"{primer_jugador} - {str(primer_score)}", True, (amarillo), (rojo))
                            texto_segundo_jugador = font.render("Sin jugador", True, (amarillo), (rojo))
                            texto_tercer_jugador = font.render("Sin jugador", True, (amarillo), (rojo))
                        else:
                            texto_primer_jugador = font.render("Sin jugador", True, (amarillo), (rojo))
                            texto_segundo_jugador = font.render("Sin jugador", True, (amarillo), (rojo))
                            texto_tercer_jugador = font.render("Sin jugador", True, (amarillo), (rojo))

            if rect_boton_salir.collidepoint(event.pos): #!-----------------------------------COLLIDE SALIR 
                if esta_jugando == False and juego_finalizado == False:
                    running=False
            
            if esta_jugando == True and juego_finalizado == True:
                if rect_ingreso_usuario.collidepoint(event.pos): #!-------------------------------COLLIDE USUARIO 
                    #print("Colisiono ingreso")
                    entrada_de_usuario = True
    
        if event.type == pygame.KEYDOWN: #!-----------------Evento de entrada de usuario. (Me mate haciendo esto.)
            if entrada_de_usuario == True:
                if event.key == pygame.K_RETURN and texto_verificado == True:
                    lista_nueva = guardar_jugador(texto_nombre_usuario, numeros_score, jugadores)
                    guardar_json("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/proyecto-preguntados.json", lista_nueva)
                    juego_finalizado = False
                    esta_jugando = False
                    sonido_finalizado.stop()
                elif event.key == pygame.K_BACKSPACE:
                    texto_nombre_usuario = texto_nombre_usuario[:-1]
                else:
                    texto_nombre_usuario += event.unicode
                    texto_verificado = verificar_nombres_juego(texto_nombre_usuario, 8)
                    # if texto_verificado == False:
                        
        
        if esta_jugando == False: #!-----------------------------------------------------------------------PANTALLA DE INICIO 
            #----------FONDO-----------
            fondo = pygame.image.load("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/preguntados.png")
            screen.blit(fondo,(0,0))
            #----------RECTS-----------
            pygame.draw.rect(screen, (rojo), rect_boton_jugar, border_radius = 15)
            pygame.draw.rect(screen, (negro), rect_boton_puntaje, border_radius = 15)
            pygame.draw.rect(screen, (negro), rect_boton_salir, border_radius = 25)
            pygame.draw.rect(screen, (amarillo), rect_silenciar_musica)
            #----------BLITZ-----------
            screen.blit(texto_silenciar, (rect_ubicacion_silenciar_x , rect_ubicacion_silenciar_y))
            screen.blit(text_start, (600, 620))
            screen.blit(text_puntaje, (178, 620))
            screen.blit(text_salir, (1010, 50))
        else: #!--------------------------------------------------------------------------------------------PANTALLA DE JUEGO
            #----------FONDO-----------
            fondo_jugando = pygame.image.load("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/trivia-crack-2_banner.jpg")
            screen.fill((100, 176, 233))
            screen.blit (fondo_jugando,(0,0))
            #----------RECTS-----------
            pygame.draw.rect(screen, (rojo), rect_boton_pregunta, border_radius = 10)
            pygame.draw.rect(screen, (naranja), (100, 240, 1050, 70), border_radius = 10)
            pygame.draw.rect(screen, (naranja), rect_boton_respuesta_a, border_radius = 10)
            pygame.draw.rect(screen, (naranja), rect_boton_respuesta_b, border_radius = 10)
            pygame.draw.rect(screen, (naranja), rect_boton_respuesta_c, border_radius = 10)
            pygame.draw.rect(screen, (rojo), rect_boton_volver, border_radius = 10)
            pygame.draw.rect(screen, (rojo), rect_reinicio, border_radius = 10)
            pygame.draw.rect(screen, (amarillo), rect_silenciar_musica)
            pygame.draw.rect(screen, (rojo), (140, 163, 185, 45), border_radius = 18)
            #----------BLITZ-----------
            screen.blit(texto_silenciar, (rect_ubicacion_silenciar_x , rect_ubicacion_silenciar_y))
            screen.blit(textpregunta, (1025, 77))
            screen.blit(textpreguntajugando, (120, 260))
            medida_text_respuesta_x = 175
            medida_text_respuesta_y = 360
            screen.blit(textorespuesta_a, (medida_text_respuesta_x, medida_text_respuesta_y))
            screen.blit(textorespuesta_b, (medida_text_respuesta_x, medida_text_respuesta_y+100))
            screen.blit(textorespuesta_c, (medida_text_respuesta_x, medida_text_respuesta_y+200))
            # ubicacion_score_x = 150
            # ubicacion_score_y = 170
            screen.blit(textoscore, (ubicacion_score_x, ubicacion_score_y))
            screen.blit(textoscore_2, (ubicacion_score_x+110, ubicacion_score_y))
            screen.blit(textovolver, (1005, 598))
            screen.blit(textreinicio, (100, 77))

        if juego_finalizado == True: #!-------------------------------------------------------------------PANTALLA DE FINALIZACION 
            #----------FONDO-----------
            fondo_finalizado = pygame.image.load("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/preguntados-netflix-trivia-quest.jpg")
            screen.blit(fondo_finalizado, (0,0))
            #----------RECTS-----------
            pygame.draw.rect(screen, (negro), rect_ingreso_usuario, border_radius = 15)
            pygame.draw.rect(screen, (rojo), rect_boton_volver, border_radius = 15)
            pygame.draw.rect(screen, (amarillo), rect_silenciar_musica)
            pygame.draw.rect(screen, (rojo), (495, 90, 300, 50), border_radius = 10)
            #----------FUENTE---------
            texto_de_usuario = font.render(texto_nombre_usuario, True, (255, 255, 0))
            felicitaciones = font.render(f"Tu Score Es: {numeros_score}", True, (amarillo), rojo)
            alerta = font_respuestas.render(f"Ingresar un usuario con menos de 8 caracteres.", True, (rojo), (amarillo))
            #----------BLITZ-----------
            screen.blit(texto_silenciar, (rect_ubicacion_silenciar_x , rect_ubicacion_silenciar_y))
            screen.blit(textovolver, (1005, 598))
            screen.blit(texto_de_usuario, (rect_ubicacion_usuario_x, rect_ubicacion_usuario_y+8))
            screen.blit(felicitaciones, (505, 100))
            screen.blit(textoingreso, (rect_ubicacion_silenciar_x+60, rect_ubicacion_usuario_y+8))
            screen.blit(alerta, (220, rect_ubicacion_usuario_y+70))

        if pantalla_puntaje == True: #!--------------------------------------------------------------------PANTALLA DE PUNTAJE
            #----------FONDO-----------
            fuente2 = pygame.font.SysFont("Default", 50)
            fondo_puntaje = pygame.image.load("Curso_de_ingreso_PYTHON-main/Programacion1/proyecto-preguntados/game-rank-badge-set-with-podium-vector.jpg")
            screen.blit(fondo_puntaje, (0,0))
            #----------RECTS-----------
            pygame.draw.rect(screen, (245, 51, 44), rect_boton_volver, border_radius = 15)
            pygame.draw.rect(screen, (amarillo), rect_silenciar_musica)
            #----------FUENTE---------
            textocampeones = fuente2.render("¡Estos son nuestros campeones!", True, (255, 255, 0))
            #----------BLITZ-----------
            screen.blit(texto_silenciar, (rect_ubicacion_silenciar_x , rect_ubicacion_silenciar_y))
            screen.blit(textovolver, (1005, 598))
            screen.blit(texto_primer_jugador, (950, 300))
            screen.blit(texto_segundo_jugador, (540, 300))
            screen.blit(texto_tercer_jugador, (130, 300))
            screen.blit(textocampeones, (385, 100))

    pygame.display.flip()

pygame.quit()