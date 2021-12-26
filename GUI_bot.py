import dialogflow
from google.api_core.exceptions import InvalidArgument
import os
from tkinter import *


class GUI_bot(Tk):
    # Access key for google apps
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private_key4.json'
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path('test-t9ek', 'Teacher')

    def __init__(self):
        super().__init__()

        self.title('GUI bot')
        self.geometry('500x300')
        self.text_space = Text(width=25)
        self.msg_space = Entry()
        self.send_btn = Button(text='Отправить', command=self.sending)

        self.text_space.place(x=5, y=5, relwidth=0.9, relheight=0.8)
        self.msg_space.place(rely=0.9, x=5, relwidth=0.8,)
        self.send_btn.place(relx=0.85, rely=0.9, )

    def sending(self):
        # Получаем сообщение для бота
        msg = self.msg_space.get()

        # Сформируем строку запрос для бота
        text_input = dialogflow.types.TextInput(text=msg, language_code='ru')
        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)
            # print(response)
            if response.query_result.fulfillment_text:
                self.print_text(response.query_result.fulfillment_text +\
                    '(' + response.query_result.intent.display_name + ')')
            else:
                self.print_text('Мин тоби не понимать!')

        except InvalidArgument:
            raise

    def print_text(self, text):
        self.text_space.insert(END, '\n\n'+text)


if __name__ == '__main__':
    root = GUI_bot()
    root.mainloop()
