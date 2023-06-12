import requests
from selenium import webdriver
import time
import sched
import time
from tkinter import *

s = sched.scheduler(time.time, time.sleep)

bot_token = '5617893594:AAEr62YSHfbSzWyZLwFWYU8sQ6FLXEOAuOo'




def startf(timedur=5, normal_value_for_result=10):
    # Берем данные из полей программы, интерфейс tkinter
    chatID = chatid.get()
    timedur = timdur.get()
    normal_value_for_result = normal__result.get()


    s.enter(int(timedur), 1, startf)  # Перезапуск через timedur секунд
    driver = webdriver.Chrome()
    driver.get("https://coinsbit.io/ru/trade_classic/PLCUX_PLCU") # Сайт, который нужно проверить

    time.sleep(5)
    # Ищем по Xpath нужный нам элемент
    main_page = driver.find_elements(
        "xpath", "//div[contains(@class, 'trade-last-orders-table__row')][20]/div[3]") # таким образом можно выбрать любой элемент на любом сайте

    # Парсим нужную нам инфу
    for word in main_page:
        result = (word.text)

    # Отправляем сообщение в тг, если оно соответствует условию

        if float(result) < float(normal_value_for_result):
            def tele_bot_send(bot_token, chatID, message):
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chatID}&parse_mode=Markdown&text={message}'
                response = requests.get(url)
                return response.json()
            response = tele_bot_send(bot_token, chatID, f'Сумма = {result}')
            break
        else:
            driver.quit()
            s.run()




# Интерфейс с помощью Tkinter

root = Tk()


root['bg'] = 'white'
root.title('PriceChecker')
root.geometry('550x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=400, width=350)


canvas.pack()

frame = Frame(root, bg='silver')
frame.place(relwidth=1, relheight=1)

text0 = Label(frame, text='Для работы напишите в телеграмме боту botforlaunch_bot и нажмите /start')
text0.pack()

text1 = Label(
    frame, text="Введите ваш ID, для этого обратитесь к боту в телеграмме (Get My ID)")
text1.pack()

chatid = Entry(frame, text='id', bg='white')
chatid.pack()

text2 = Label(
    frame, text="Введите время, по которому программа будет обновлять данные (в секундах)")
text2.pack()

timdur = Entry(frame, bg='white')
timdur.pack()

text3 = Label(frame, text="Введите желаемое значение суммы (сообщение придет, если ваша сумма больше)")
text3.pack()

normal__result = Entry(frame, bg='white')
normal__result.pack()

btn = Button(frame, text='Запустить', bg='yellow', command=startf)
btn.pack()


# Цикл, чтобы работала программа
 
while True:
    root.update()
    root.update_idletasks()
