from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
 
class LabelBoxLayout(BoxLayout):
    def __init__(self,**kwargs):
        super(LabelBoxLayout, self).__init__(**kwargs)
 
        #设置引用时，markup属性必须设置为真（True、1）
        #将Label文本标记，单击Lable文本时会触发绑定的事件，单击hello文本则不会
        label_ref=Label(text='[ref=label]Label[/ref]',markup=True,color=(.9,.2,.1,1))
 
        #绑定触发事件，回调方法
        label_ref.bind(on_ref_press=self.print_it)
        self.add_widget(label_ref)
 
    #未使用到self,建议设置为静态方法
    @staticmethod
    def print_it(*args):
        print('print_it')
 
 
class LabelApp(App):
    def build(self):
        return LabelBoxLayout()
 
if __name__ =='__main__':
    LabelApp().run()