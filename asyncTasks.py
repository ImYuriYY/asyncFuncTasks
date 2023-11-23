import asyncio

# TASK 1

# async def Plus(a,b):
#     print("Складывание началось")
#     await asyncio.sleep(3)
#     print(a+b)
#     return a+b

# async def square(a):
#     print("Возведение в квадрат началось")
#     await asyncio.sleep(4)
#     print(a**2)
#     return a**2

# async def main():
#     count=list()
#     task1 = asyncio.create_task(Plus(4,4))
#     task2 = asyncio.create_task(square(4))
#     await asyncio.gather(task1, task2)


# asyncio.run(main())









# TASK 2

# НЕ рабочее. Так и не понял как его сделать адекватно

# takeCall = True
# receiveVisitors = True
# resTickets = True
# graphControl = True
# documentsFill = True

# async def take_call(tk):
#     await asyncio.sleep(5)
#     if tk == True:
#         resTickets = False
#         documentsFill = False
#         while True:
#             print('Ответ на телефонный звонок')
#             await asyncio.sleep(10)
#             resTickets = True
#             documentsFill = True
#             print('Звонок завершён')

# async def receive_visitors():
#     await asyncio.sleep(5)
#     while receiveVisitors == True:
#         resTickets = False
#         documentsFill = False
#         print('Приём посетителей начался')
#         await asyncio.sleep(10)
#         resTickets = True
#         documentsFill = True
#         print('Больше не принимаем посетителей')

# async def res_tickets():
#     while resTickets == True:
#         print('Начало бронирования билетов на самолёт')
#         await asyncio.sleep(10)
#         print('Больше не пытаемся бронировать билеты на самолёт')
#     else:
#         print('Больше не пытаемся бронировать билеты на самолёт')

# async def graph_control():
#     await asyncio.sleep(5)
#     while graphControl == True:
#         resTickets = False
#         documentsFill = False
#         print('Контролируем график')
#         await asyncio.sleep(10)
#         resTickets = True
#         documentsFill = True
#         print('Больше не контролируем график')

# async def documents_fill():
#     while documentsFill == True:
#         print('Начали заполнять документы')
#         await asyncio.sleep(10)
#         print('Больше не заполняем документы')
#     else:
#         print('Больше не заполняем документы')


# async def main():
#     task1 = asyncio.create_task(take_call(True))
#     task2 = asyncio.create_task(receive_visitors())
#     task3 = asyncio.create_task(res_tickets())
#     task4 = asyncio.create_task(graph_control())
#     task5 = asyncio.create_task(documents_fill())
    
#     await asyncio.wait([task3, task5, task4, task1, task2])

# if __name__ == '__main__':
#     asyncio.run(main())