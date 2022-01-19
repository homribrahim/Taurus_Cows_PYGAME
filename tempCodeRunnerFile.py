    if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    if (self==button1):
                        jeu()
                    if (self==button2):
                        aide()
                    if (self==button3):
                        options()
                    if (self==button4):
                        credit()
                    if (self==button_Quit):
                        sys.exit()    
                    if (self==button_expert):
                        creation_expert()
                    if (self==button_beginner):
                        creation_beginner()
                    if (self==button_stop_music):
                        pygame.mixer.pause()  
                        main_menu()   

                    self.pressed = False
                    self.change_text(self.text)   