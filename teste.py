#Importa o app da blibliteca app
from kivy.app import App 

#Importa a função Label 
from kivy.uix.label import Label

#Criação de classe chamada MainApp com parametro App
class MainApp(App):

#Define uma função build para a variavel label    
    def build(self):

        #Texto que vai ser apresentado com definição da dimensão da escrita
        label= Label(text='Codigo de teste inicial',
             size_hint=(.5, .5),
             pos_hint={'center_x': .5, 'center_y': .5 })     
        
        #retorno da estrutura label 
        return label
    
#chamada da função 
if __name__== '__main__':
    #Defino que app é igual MainApp da classe e adiciona dentro do App.run
    App=MainApp()
    App.run()