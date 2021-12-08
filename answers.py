class QAAnswers:
    A1 = "Интеграционное тестирование, модульное тестирование"
    B1 = "Приёмочное тестирование, Системное тестирование"
    C1 = "Альфа-тестирование, Бета-тестирование " 
    CORRECT_ANSWER_QA1 = ['A', 'B', 'C']    

    A2 = "Раннее тестирование эффективнее"
    B2 = "Тестирование не всегда показывает наличие дефектов"
    C2 = "Группирование дефектов" 
    CORRECT_ANSWER_QA2 = ['A', 'C']

    A3 = "Непонимание требований и спецификаций"
    B3 = "Изменение требований в то время как ПО под испытанием"
    C3 = "Плохая ориентация в версиях ПО" 
    CORRECT_ANSWER_QA3 = ['A', 'B', 'C']    
    
    A4 = "Тестирование черного ящика"
    B4 = "Тестирование желтого ящика"
    C4 = "Тестирование красного ящика" 
    CORRECT_ANSWER_QA4 = ['A']    
    
    A5 = "Это ошибка, неправильное представление, или непонимание со стороны разработчик программного обеспечения"
    B5 = "Это аномалия в программное обеспечение, которое может заставить его вести себя неправильно, а не в соответствии с его спецификация"
    C5 = "Это неспособность программного обеспечения или компонента для выполнять требуемые функции внутри заданные требования к производительности" 
    CORRECT_ANSWER_QA5 = ['B']     

class AnalitixAnswer:

    A1 = "База данных, в которой информация хранится в виде двумерных таблиц, связанных между собой"
    B1 = "Любая база данных - реляционная"
    C1 = "Совокупность данных, не связанных между собой" 
    CORRECT_ANSWER_A1 = ['A']  

    A2 = "Неотсортированные номера и даты всех заказов с именами заказчиков"
    B2 = "Номера и даты всех заказов с именами заказчиков, отсортированные по первой колонке"
    C2 = "Номера и даты всех заказов с именами заказчиков, отсортированные по всем колонкам, содержащим слово Order" 
    CORRECT_ANSWER_A2 = ['A']    

    A3 = "Все верно, запрос покажет все заказы, продавцы которых не проставлены"
    B3 = "Сравнение с NULL можно проводить только с оператором IS"
    C3 = "NULL нужно взять в кавычки" 
    CORRECT_ANSWER_A3 = ['B']    

    A4 = "Уникальные ID продавцов, отсортированные по возрастанию"
    B4 = "Уникальные ID продавцов, отсортированные по убыванию"
    C4 = "Ничего, запрос составлен неверно, ORDER BY всегда ставится в конце запроса" 
    CORRECT_ANSWER_A4 = ['C']    
    
    A5 = "Сначала выполняется OR, а затем AND"
    B5 = "Сначала выполняется AND, а затем OR"
    C5 = "Порядок выполнения операторов AND и OR зависит от того, какой из операторов стоит первым"    
    CORRECT_ANSWER_A5 = ['B']


class DeveloperAnswer:
    A1 = "Кортеж"
    B1 = "Строки"
    C1 = "Множества" 
    CORRECT_ANSWER_D1 = ['A', 'B']

    A2 = "Set"
    B2 = "Кортеж"
    C2 = "Словарь" 
    CORRECT_ANSWER_D2 = ['B']

    A3 = "Интерпретированный"
    B3 = "С динамической типизацией"
    C3 = "Объектно-ориентированный" 
    CORRECT_ANSWER_D3 = ['A','B','C']
    
    A4 = "__class__, __name__"
    B4 = "__class__, __dict__"
    C4 = "__name__, __init__" 
    CORRECT_ANSWER_D4 = ['B']

    A5 = "Экземпляр класса, реализующего протокол дескрипторов"
    B5 = "Декаратор с использованием методов __get__(), __set__(), __delete__()"
    C5 = "Свойство, которое можно переиспользовать"   
    CORRECT_ANSWER_D5 = ['A', 'C']   

class TYPE_TEST:   
    type_test = 'None'

class Answers:
    FIRST = 'None'
    SECOND = 'None'
    THIRD = 'None'
    FOURTH = 'None'
    FIVE = 'None'
    name = 'None'
    surname = 'None'
    age = 'None'
    city = 'None'
