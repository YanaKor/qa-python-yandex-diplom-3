from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = f'{BASE_URL}/login'
    RECOVERY_PAGE = f'{BASE_URL}/forgot-password'
    RESET_PASSWORD_PAGE = f'{BASE_URL}/reset-password'
    PERSONAL_ACCOUNT = f'{BASE_URL}/account/profile'
    ORDER_HISTORY = f'{BASE_URL}/account/order-history'
    FEED_PAGE = f'{BASE_URL}/feed'


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH, ".//nav//p[contains(text(), 'Личный Кабинет')]")  # вход через кнопку «Личный кабинет»
    LOGIN_BUTTON = (
        By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка войти в аккаунт на главной странице
    CONSTRUCTOR_BUTTON = (
        By.XPATH, ".//a[@href='/']")  # вход через кнопку «Личный кабинет»
    ORDER_FEED_BUTTON = (
        By.XPATH, ".//a[@href='/feed']")  # вход через кнопку «Личный кабинет»
    FOCUSED_TEXT = 'link_active'

    BUN_INGREDIENT = (
        By.XPATH, ".//p[contains(text(), 'Краторная булка N-200i')]")  # Выбор булки из списка ингредиентов
    MODAL_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")  # Открытое модальное окно
    CLOSE_MODAL_WINDOW = (
        By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")  # крестик закрытия модального окна
    CONSTRUCTOR_BASKET = (
        By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")  # Конструктор бургера
    COUNTER = (By.XPATH, ".//ul[1]/a[2]//p[contains(@class, 'num')]")  # Счетчик второго ингредиента
    CREATE_ORDER = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ"


class PasswordRecoveryLocators:
    RECOVERY_EMAIL = 'yana_kormshchikova_11666@yandex.ru'
    RECOVERY_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  # ссылка на форму восстановления пароля
    RECOVERY_EMAIL_FIELD = (By.XPATH, ".//form//input[@name='name']")  # Поле email в форме восстановления пароля
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")  # Кнопка восстановить в форме

    EYE_BUTTON = (By.XPATH, ".//div[contains(@class,'input__icon')]")  # Кнопка "глаза" в поле пароля (reset-password)
    FOCUSED_FIELD = (By.XPATH, ".//*[contains(@class,'input__placeholder')]")  #
    FOCUSED_TEXT = 'input__placeholder-focused'  # измененный класс элемента


class PersonalAccountLocators:
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//form//input[@name='name']")  # Поле ввода email на странице входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//form//input[@type='password']")  # Поле ввода пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//form//button[contains(text(), 'Войти')]")  # Кнопка "Войти" в форме
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")  # Кнопка "История заказов в личном кабинете "


class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
    THIRD_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[2]")
    MODAL_ORDER_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")
    # История заказов в лк пользователя
    USER_ORDERS_HISTORY = (
        By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]')

    ORDER_NUMBERS = (By.XPATH, '//p[@class="text text_type_digits-default"]')  # Номера всех заказов в ленте
    LAST_ORDER = (By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]')  # Номер последнего заказа в ленте
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"
    # Счётчик "Выполнено за всё время"
    ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class,"OrderFeed_number")]')
    # Счётчик "Выполнено за сегодня"
    TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class,"OrderFeed_number")]')
