from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
import requests
import random


kv='''
Manager:
    Fir:
    Sec:        
<Fir>:
    id:s1
    name:'home'
    
    MDCarousel:
        id:mc1
        direction:'bottom'
        pos_hint:{'center_x':0.5,'center_y':0.6} 
        size_hint:1,0.5
      
            
   
    MDIconButton:
        icon:'refresh'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        size_hint:1,0.1
        md_bg_color:0,0,1,1
        on_press:app.refresh()
        




    





    MDTopAppBar:
        id:tb1
        pos_hint:{'top':1}
        title:'IMAGE DOWNLOADER'
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]
        md_bg_color:0,0,1,1

    MDNavigationDrawer:
        id:nd1
     




'''













class Manager(ScreenManager):
    pass

class Fir(Screen):
    pass

class Sec(Screen):
    pass
    
    
    

class Demo(MDApp):
    def build(self):
        self.b=Builder.load_string(kv)   
        return self.b    
            
    def on_start(self):
        try:
            for i in range(0,2):
                rr1=random.randint(1,10000)
                rr2 = f"https://picsum.photos/seed/{rr1}/600/400"
                r1=requests.get(rr2)
                if r1.status_code ==200:
                    rr=self.b.get_screen('home').ids.mc1
                    rr3 =MDCard(on_press=lambda x,imgu=rr2:self.click())
                    rr4 =AsyncImage(source=rr2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
                
                    rr.add_widget(rr3)
                    rr3.add_widget(rr4)

        except requests.exceptions.ConnectionError:
            self.b.get_screen('home').ids.mc1.add_widget(MDCard(MDLabel(text='NO INTERNET CONNECTION',font_style='H6')))            
            toast("No internet connection")
            
        except requests.exceptions.Timeout:
            toast("Request timed out")
        except requests.exceptions.HTTPError as e:
            toast(f"HTTP error: {e}")
        except FileNotFoundError:
            toast("Save location not found")
        except PermissionError:
            toast("Permission denied while saving")                

        except Exception as e:
            toast(f'{e}')                                                                                                
                                                                
                                                                                                
                                                                                                                                                                
    def click(self):
        toast('RAM-RAM')       

    def refresh(self):
        try:
            self.b.get_screen('home').ids.mc1.clear_widgets()            
            for i in range(0,2):
                rr1=random.randint(1,10000)
                rr2 = f"https://picsum.photos/seed/{rr1}/600/400"
                r1=requests.get(rr2)
                if r1.status_code ==200:
                    rr=self.b.get_screen('home').ids.mc1
                    rr3 =MDCard(on_press=lambda x,imgu=rr2:self.click())
                    rr4 =AsyncImage(source=rr2,size_hint=(1,1),allow_stretch=True,keep_ratio=False)
                
                    rr.add_widget(rr3)
                    rr3.add_widget(rr4)
                
        except requests.exceptions.ConnectionError:
            self.b.get_screen('home').ids.mc1.add_widget(MDCard(MDLabel(text='NO INTERNET CONNECTION',font_style='H6')))            
            toast("No internet connection")
            
        except requests.exceptions.Timeout:
            toast("Request timed out")
        except requests.exceptions.HTTPError as e:
            toast(f"HTTP error: {e}")
        except FileNotFoundError:
            toast("Save location not found")
        except PermissionError:
            toast("Permission denied while saving")                

        except Exception as e:
            toast(f'{e}')                                  
                                
                        
        
    
Demo().run()  
    