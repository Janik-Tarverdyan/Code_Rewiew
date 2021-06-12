from API.Core import components
from flask import Markup


routes = {
    '/': ['home', "Главная"],
    '/services': ['star', "Услуги"],
    '/about_us': ['file', "О нас"],
    # '/faq': ['comment-alt-text', "Вопросы и ответы"],
    '/contact_us': ['accounts-alt', "Связь"],
}


Title = {
    "Company": {
        'Brand': "Master",
        'Name': "Mind",
        'Description': 'Company Description'
    },
    "Brand_Name": Markup('<strong>Master</strong> <span>Mind</span>')
}


Header = {
    'Slider': {
        'Web_Site': {
            'Title': Markup("<strong>Веб сайты</strong> / <strong class='color-warning'>  О главном</strong>"),

            'Sub_Title': Markup("Ваш сайт будет иметь то что <span class='color-warning'>выберите</span>. "),

            'Description': {
                'item_1': {
                    'icon': "fas fa-chart-line",
                    'type': "info",
                    "text": Markup("Доверяя <span class='color-warning'>Анализ</span> Вашего\
                                    <span class='color-warning'>бизнеса</span> в руки опытных\
                                    специалистов, Вы начнете свой путь с достоверным планом развития."),
                },

                'item_2': {
                    'icon': "fas fa-drafting-compass",
                    'type': "royal",
                    "text": Markup("<span class='color-warning'>Дизайн</span> может\
                                    полностью быть Вашим или мы сделаем индивидуально для Вас."),
                },

                'item_3': {
                    'icon': "fa fa-user-secret",
                    'type': "danger",
                    "text": Markup("Мы гарантируем <span class='color-warning'>\
                                    Безопасность</span> сайта даже после окончания работ.")
                },

                'item_4': {
                    'icon': "fas fa-search-dollar",
                    'type': "success",
                    "text": Markup("С помощью <span class='color-warning'>Продвижения</span> мы доведем\
                                    сайт до максимальной посещаемости."),
                },

            },

            'Button': {
                'Buy': {
                    'url': "/contact_us#for_by_WebSite",
                    'label': "Купить",
                    'position': "Right",
                    'icon': "fas fa-dollar-sign",
                    'type': 'royal',
                },

                'Rent': {
                    'url': "#Rent",
                    'label': "Аренда",
                    'position': "Left",
                    'icon': "zmdi zmdi-case",
                    'type': 'success',
                },
            },
        },
        'Partnership': {
            'Title':  Markup("<strong>Партнёрские Программы</strong>"),
            'Sub_Title': Markup("Все могут <span class='color-warning'>сотрудничать</span>\
                                с нами <span class='color-warning'>определенно</span>"),
            'Description': {
                'Делясь прибылью': {
                    # 'icon': "fas fa-file-signature",
                    # 'icon': "fas fa-file-alt",
                    # 'icon': "fas fa-file-invoice",
                    'icon': "fas fa-file-medical-alt",
                    'type': "info",
                    "text": Markup("<span class='color-warning'>Делясь</span> прибылью, и\
                    обьязательствами с нами с Вашим\
                    <span class='color-warning'>проектом-заказом</span>,\
                    по изначальной взаимной договорённости."),
                },
                'Нанимая сотрудников': {
                    'icon': "fas fa-user-graduate",
                    'type': "royal",
                    "text": Markup("<span class='color-warning'>Нанимая сотрудников,</span>\
                   каротых мы Вам предложим"),
                },
                'Предлагая продукт': {
                    'icon': "fas fa-file-invoice-dollar",
                    'type': "success",
                    "text": Markup("<span class='color-warning'>Предлагая продукт</span> совместного производство\
                    принимая взаимно согласованные условия."),
                },
                'Инвестируя': {
                    'icon': "fas fa-hand-holding-usd",
                    'type': "warning",
                    "text": Markup("<span class='color-warning'>Инвестируя</span> в одну или в нескольких наших\
                             бизнес идей, подробно о которых прочтете."),
                },
            },
            'Button': {
                'Invest': {
                    'url': "#Become_a_partner",
                    'label': "Стать партнером",
                    'position': "Left",
                    'icon': "far fa-handshake",
                    'type': 'warning',
                },
            },
        }
    },
    'Basic': {
        'logo_img': "/static/site/Master_Mind/img/logo.png",
        'Title': Markup("<span>Master</span> Mind"),
        'Description': Markup("<p class='lead lead-lg\
                                        color-warning text-center center-block\
                                        mt-2 mw-800 text-uppercase fw-300\
                                        animated fadeInUp animation-delay-7'>\
                                        Компания мечты"
                              )
    },
    'Price': {
        'Title': "Услуги",
        'Description': Markup("<p class='lead lead-lg\
                                        color-warning text-center center-block\
                                        mt-2 mw-800 text-uppercase fw-300\
                                        animated fadeInUp animation-delay-7'>\
                                    Откройте для себя наши проекты и\
                                    строгий процесс создания.\
                                    Наши принципы - это креативность,\
                                    дизайн, опыт и знания.")
    },
    'Services': {
        'IT Аудит': {
            'Backgrounds': "",
        },
        'Бизнес Анализ': {
            'Backgrounds': "",
        },
        'Дизайн UX-UI': {
            'Backgrounds': "",
        },
    },
}


Services = {
    'Advance': {
        'Title': "Топ Услуги",
        'Description': Markup("<span> Если Вашего бизнеса нет в Интернете, то Вас нет в бизнесе! 🙂 </span>  "),

        'item_1': {
            'Type': "info",
            'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/m1.png",
            'Title': "Бизнес-Анализ",
            'Description': "Качество продукта зависит от требовательного бизнес-анализа.\
                    Гарантия Вашего успеха заключается в решении победить.",
            'Button': {
                'Buy': {
                    'url': "#discuss/service/business_analysis",
                    'icon': "far fa-handshake",
                    'label': "Обсудить"
                },
                'More_info': {
                    'url': "#about/service/business_analysis",
                    'icon': "fa fa-rocket",
                    'label': "Подробнее"
                },
            }
        },
        'item_2': {
            'Type': "danger",
            'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/m2.png",
            'Title': "Дизайн UX/UI",
            # 'Description': "Дизайн – это лицо вашей компании.\
            #                 Удобство в использовании и внешний вид залог вашего успеха.",
            'Description': "Дизайн – это лицо Вашей компании.\
                    Удобство в использовании и профессиональный\
                    внешний вид влекут за собой потребителей.",
            'Button': {
                'Buy': {
                    'url': "#discuss/service/design-UX_UI",
                    'icon': "far fa-handshake",
                    'label': "Обсудить"
                },
                'More_info': {
                    'url': "#about/service/design-UX_UI",
                    'icon': "fas fa-anchor",
                    'label': "Подробнее"
                },
            },
        },
        'item_3': {
            'Type': "royal",
            'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/m3.png",
            'Title': "Создание Веб Сайтов",
            # 'Description': "Креативный сайт -это Ваш офис в интернете\
            #                 и главный инструмент вашего бизнеса.\
            #                 Визитка в мир успешного бизнеса.",
            'Description': "Веб сайт - это Ваш офис в интернете,\
                    главный инструмент продаж и визитка в\
                    мир успешного бизнеса.",
            'Button': {
                'Buy': {
                    'url': "#discuss/service/web_sites",
                    'icon': "far fa-handshake",
                    'label': "Обсудить"
                },
                'More_info': {
                    'url': "#about/service/web_sites",
                    'icon': "zmdi zmdi-devices",
                    'label': "Подробнее"
                },
            },
        },
        'item_4': {
            'Type': "success",
            'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/m4.png",
            'Title': "Продвижение Сайта",
            # 'Description': "Каждый день в Яндексе и Гугле люди запрашивают более 100 миллиардов запросов по всему миру.\
            #                 Каждый поисковой запрос заставляет поисковую систему искать на него ответ.\
            #                 Причем поисковые системы должны обеспечить наиболее релевантные,\
            #                 полезные и надежные ответы для пользователя.\
            #                 Вот поэтому нужно сделать так что большинство откликнулись именно на Ваш сайт. ",
            'Description': "Каким бы мощным не был Ваш сайт,\
                    он не будет посещаемым без продвижения.\
                    Продвижение увеличивает ценность вашего\
                    сайта среди ответных ссылок в поисковых системах.",
            'Button': {
                'Buy': {
                    'url': "#discuss/service/promotion_website",
                    'icon': "far fa-handshake",
                    'label': "Обсудить"
                },
                'More_info': {
                    'url': "#about/service/promotion_website",
                    'icon': "zmdi zmdi-search-in-page",
                    'label': "Подробнее"
                },
            },
        },
    },
    'All': {
        'Title': "Наши Услуги",
        'IT Аудит': {
            'icon': "fas fa-audio-description",
            'href': "/info/service/IT_Аудит",
            'Title': "IT Аудит",
            'Description': "Ежедневно система информационных технологий растет и\
                            усложняется, занимая все больше времени и финансов.",
            'Buttons': {
                'Заказать': {
                    'href': "#Заказать",
                    'label': "Заказать",
                },
            },
        },
        'Бизнес Анализ': {
            'icon': "fas fa-chart-line",
            'href': "/info/service/Бизнес_Анализ",
            'Title': "Бизнес Анализ",
            'Description': "Качество продукта зависит от\
                            требовательного бизнес-анализа.\
                            Гарантия Вашего успеха заключается в решении победить.",
            'Buttons': {
                'Заказать': {
                    'href': "#Заказать",
                    'label': "Заказать",
                },
            },
        },
        'Дизайн UX-UI': {
            'icon': "fas fa-drafting-compass",
            'href': "/info/service/Дизайн_UX-UI",
            'Title': "Дизайн UX-UI",
            'Description': "Дизайн – это лицо Вашей компании.\
                            Удобство в использовании и\
                            профессиональный внешний вид\
                            влекут за собой потребителей.",
            'Buttons': {
                'Заказать': {
                    'href': "#Заказать",
                    'label': "Заказать",
                },
            },
        },
        'Веб сайты': {
            'icon': "zmdi zmdi-devices",
            'href': "/info/service/Дизайн_UX-UI",
            'Title': "Веб сайты",
            'Description': "Веб сайт - это Ваш офис в интернете,\
                            главный инструмент продаж и визитка\
                            в мир успешного бизнеса.",
            'Buttons': {
                'Заказать': {
                    'href': "#Заказать",
                    'label': "Заказать",
                },
            },
        },
        'Продвижение Сайта': {
            'icon': "fa fa-rocket",
            'href': "/info/service/Дизайн_UX-UI",
            'Title': "Продвижение Сайта",
            'Description': "Каким бы мощным не был Ваш сайт,\
                            он не будет посещаемым без продвижения.\
                            Продвижение увеличивает ценность вашего\
                            сайта среди ответных ссылок в поисковых системах.",
            'Buttons': {
                'Заказать': {
                    'href': "#Заказать",
                    'label': "Заказать",
                },
            },
        },
    },
}


Slider = {
    'Portfolio': {
        'Title': "Наши Работы",
        'Category': "job",
        'items': {
            'BestCon': {
                'Title': "Бэсткон",
                'Description': "Строительно-инвестиционная компания\
                                Агентство недвижимости\
                                Более 15 лет успешной работы на рынке недвижимости!",
                'image': "/static/site/Master_Mind/img/BestCon.png",
            },
            'Liederlernen': {
                'Title': "Онлайн-школа пианистов",
                'Description': "Онлайн школа пианистов,\
                                которая поможет вам осуществить\
                                свою мечту шаг за шагом. ",
                'image': "/static/site/Master_Mind/img/Liederlernen.png",
            },
        }
    },
    'Services': {
        'Slid_1': {
            'Title': {
                'text': "Консультация в сфере ИТ",
                'color': "primary",
            },
            'Description': {
                'text': "B2B B2C C2C C2B B2G",
                'color': "warning",
            },
            'items': {
                'Презентация работоспособности': {
                    'Icon': "zmdi zmdi-present-to-all zmdi-hc-fw",
                    'Color': "success",
                    'Text': Markup("Презентация работоспособности"),
                },
                'Анализ_направления_бизнеса': {
                    'Icon': "fas fa-chart-line",
                    'Color': "info",
                    'Text': Markup("Анализ направления бизнеса."),
                },
                'Выявление_проблем_деятельности': {
                    'Icon': "zmdi zmdi-bug",
                    'Color': "warning",
                    'Text': Markup("Выявление проблем деятельности"),
                },
                'Конкурентоспособные решения развития': {
                    'Icon': "fas fa-hands-helping",
                    # 'Color': "danger",
                    'style_color': "#f7ea21",
                    'Text': Markup("<p style='color: #f7ea21'>Конкурентоспособные решения.</p>"),
                },
            },
            'images': components.Find.Images(Path='Services',
                                             Name='Slider',
                                             Language='Russian'),
        },
        'Slid_2': {
            'Title': {
                'text': "Развитие бизнеса в ИТ",
                'color': "success",
            },
            'Description': {
                'text': "B2B B2C C2C C2B B2G",
                'color': "warning",
            },
            'items': {
                'Разработка_бизнес_моделей': {
                    'Icon': "fas fa-file-invoice-dollar",
                    'Color': "warning",
                    'Text': Markup("Разработка бизнес моделей."),
                },
                'Решение_бизнес_задач': {
                    'Icon': "fas fa-tasks",
                    'Color': "success",
                    'Text': Markup("Решение бизнес задач."),
                },
                'Индивидуальный_дизайн_бренда': {
                    'Icon': "fas fa-drafting-compass",
                    # 'Color': "royal",
                    'style_color': "#f7ea21",
                    'Text': Markup("<p style='color: #f7ea21'>Индивидуальный дизайн бренда.</p>"),
                },
                'Профессиональные_услуги': {
                    'Icon': "fas fa-check-circle",
                    'Color': "info",
                    'Text': Markup("Профессиональные услуги."),
                },
            },
            'images': components.Find.Images(Path='Services',
                                             Name='Slider',
                                             Language='Russian'),
        },
    },
}


Subscribe = {
    'Title': "Подписывайся",
    'Text': "Текст для Подписки",
    'Form': {
        'action': "/send",
        'method': "POST",
        'Input_Label': "электронная почта",
        'Button_Label': "Подписывайся",
    },
}


Info = {
    'Basic': {
        'Title': Markup("Как <strong>стать партнером</strong> компании?"),
        'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock.png",
        'Button': {
            'Portfolio': {
                'url': "#More",
                'type': "royal",
                'icon': "fas fa-info-circle",
                'label': 'подробнее'
            },
        },
        'Text': {
            'Text_1': "Мы предусмотрели варианты сотрудничества,\
                        дав предпочтение которым Вы можете стать\
                        нашим партнером, делив работу и прибыль с нами.",
            'Text_2': "Если Вы предприниматель, кто хочет инвестировать в\
                        нашу компанию или в неповторимые в своем реализации\
                        бизнес идей, иметь растущий пассивный доход от\
                        процента и увеличить их когда захотите,\
                        то Вам необходимо ознакомиться с нашей\
                        инвестиционно-партнерской программой.",
            'Text_3': "Одновременно Вы можете стать партнером не\
                        инвестируя больших денег, а реализовав с\
                        нами Вашу бизнес идею: продукт, услугу,\
                        деля обязательства и доход от бизнеса на\
                        индивидуальных, взаимно согласованных\
                        условиях, в зависимости от предстоящих работ.",
        },
    },
    'Advance': {
        'Title': "Технология, которая объединяет команды",
        'Description': "Интеллектуальные приложения, которые помогут вам сделать лучшую работу.",

        'Linux': {
            'Name': "Linux",
            'id': "linux",
            'icon': "linux",
            'image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock4.png",
            'title': "Объединяйте идеи быстрее",
            'text': {
                'paragraph_1': "Создавайте документы, электронные таблицы и презентации из\
                                любого места. Поделитесь ими с товарищами по команде и\
                                работайте вместе над одним файлом, в то же время.",

                'paragraph_2': "петь свою работу легко с одним логином для всего,\
                                что вы делаете. Административный контроль предлагает\
                                двухэтапную проверку для повышения безопасности всей компании."
            },
            'button': {
                'info': {
                    'type': "info",
                    'url': "#info",
                    'icon': "info",
                    'label': "more info",
                },
                'action': {
                    'type': "danger",
                    'url': "#action",
                    'icon': "chart-donut",
                    'label': "Action",
                }
            }
        },
        'MacOS': {
            'Name': "MacOS",
            'id': "macos",
            'icon': "apple",
            'image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock4.png",
            'title': "Объединяйте идеи быстрее",
            'text': {
                'paragraph_1': "Создавайте документы, электронные таблицы и презентации из\
                               любого места. Поделитесь ими с товарищами по команде и\
                               работайте вместе над одним файлом, в то же время.",

                'paragraph_2': "петь свою работу легко с одним логином для всего,\
                               что вы делаете. Административный контроль предлагает\
                               двухэтапную проверку для повышения безопасности всей компании."
            },
            'button': {
                'info': {
                    'type': "info",
                    'url': "#info",
                    'icon': "info",
                    'label': "more info",
                },
                'action': {
                    'type': "danger",
                    'url': "#action",
                    'icon': "chart-donut",
                    'label': "Action",
                }
            }
        },
        'Windows': {
            'Name': "Windows",
            'id': "windows",
            'icon': "windows",
            'image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock4.png",
            'title': "Объединяйте идеи быстрее",
            'text': {
                'paragraph_1': "Создавайте документы, электронные таблицы и презентации из\
                                любого места. Поделитесь ими с товарищами по команде и\
                                работайте вместе над одним файлом, в то же время.",

                'paragraph_2': "петь свою работу легко с одним логином для всего,\
                                что вы делаете. Административный контроль предлагает\
                                двухэтапную проверку для повышения безопасности всей компании."
            },
            'button': {
                'info': {
                    'type': "info",
                    'url': "#info",
                    'icon': "info",
                    'label': "more info",
                },
                'action': {
                    'type': "danger",
                    'url': "#action",
                    'icon': "chart-donut",
                    'label': "Action",
                }
            }
        },
        'Android': {
            'Name': "Android",
            'id': "android",
            'icon': "android",
            'image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock4.png",
            'title': "Объединяйте идеи быстрее",
            'text': {
                'paragraph_1': "Создавайте документы, электронные таблицы и презентации из\
                                любого места. Поделитесь ими с товарищами по команде и\
                                работайте вместе над одним файлом, в то же время.",

                'paragraph_2': "петь свою работу легко с одним логином для всего,\
                                что вы делаете. Административный контроль предлагает\
                                двухэтапную проверку для повышения безопасности всей компании."
            },
            'button': {
                'info': {
                    'type': "info",
                    'url': "#info",
                    'icon': "info",
                    'label': "more info",
                },
                'action': {
                    'type': "danger",
                    'url': "#action",
                    'icon': "chart-donut",
                    'label': "Action",
                }
            }
        },
        'iOS': {
            'Name': "iOS",
            'id': "ios",
            'icon': "smartphone-iphone",
            'image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/mock4.png",
            'title': "Объединяйте идеи быстрее",
            'text': {
                'paragraph_1': "Создавайте документы, электронные таблицы и презентации из\
                                любого места. Поделитесь ими с товарищами по команде и\
                                работайте вместе над одним файлом, в то же время.",

                'paragraph_2': "петь свою работу легко с одним логином для всего,\
                                что вы делаете. Административный контроль предлагает\
                                двухэтапную проверку для повышения безопасности всей компании."
            },
            'button': {
                'info': {
                    'type': "info",
                    'url': "#info",
                    'icon': "info",
                    'label': "more info",
                },
                'action': {
                    'type': "danger",
                    'url': "#action",
                    'icon': "chart-donut",
                    'label': "Action",
                }
            }
        },
    },
    'Description': {
        'Title': "Почему мы разработали собственную архитектуру?",
        'Paragraph': {
            'Title': 'Ваш заказ построится на нем!!!',
            'Text': {
                'Text_1': Markup("В потребности достичь более выразительных\
                            результатов, чем можно было с помощью\
                            существующих конструктивных инструментов,\
                            мы разработали собственную строительную\
                            архитектуру на наиболее гибком фреймворке\
                            высокоуровневого языка <strong>Питона</strong>, на <strong>Фласке</strong>."),
                'Text_2': Markup("Ежедневные трудности потребления больших данных,\
                            основательные принципы идеологии <strong>No SQL</strong> толкнули\
                            нас изменить обычную базу данных на нами\
                            разработанную <strong>новую систему сбора данных</strong>."),
                'Text_3': Markup("Беспредельно неаккуратное <strong>расположение информационных\
                            сегментов</strong> заставили нас задуматься о <strong>максимально\
                            координированной системе</strong>, которая решит проблемы\
                            трат информационного пространство в пользу\
                            производительности архитектуры."),
            }
        },
        'Advantage': {
            'Title': "Преимущества",
            'items': {
                'item_1': {
                    'id': "One",
                    'icon': "user-secret",
                    'title': "Высокий уровень безопасности",
                    'description': {
                        'Paragraph_1': "Преимущество обеспечения безопасности\
                                        кроется в нескольких аспектах. Прежде всего,\
                                        архитектура новая и не раскрытая.\
                                        Данные находятся не на обычных известных всем баз,\
                                        а на кардинально изменённых. И наконец,\
                                        для каждого клиента архитектура другая и не повторимая.",
                    },
                },
                'item_2': {
                    'id': "Two",
                    'icon': "desktop",
                    'title': "Инновационность",
                    'description': {
                        'Paragraph_1': "Стоять на месте, использовать обычные знакомые\
                                        нам подходы и не искать улучшенных решений,\
                                        значит вовсе не продвинуться, не идти в\
                                        ногу с новыми технологиями.",
                        'Paragraph_2': "Беспроигрышно применив нашу конструктивную\
                                        архитектуру мы бросили вызов существующим\
                                        определениям эффективности.",
                    },
                },
                'item_3': {
                    'id': "Three",
                    'icon': "rocket",
                    'title': "Быстрота, гибкость и удобность",
                    'description': {
                        'Paragraph_1': "Архитектура работает быстро и эффективно\
                                        благодаря склонности изменяться быстрее\
                                        любого существующего фреймворка,\
                                        уменьшив выполнение загрузки до секунды.",
                    },
                },
                'item_4': {
                    'id': "Four",
                    'icon': "database",
                    'title': "Работа с большими данными",
                    'description': {
                        'Paragraph_1': "С помощью уникальности архитектуры,\
                                        данные собираются и сохраняются нестандартно.\
                                        Мы решили все проблемы касающийся\
                                        использования и работы с большими данными.",
                    },
                },
            },
        },
    },
    'About_US': {
        'Title': "О Нас",
        'Description': "Мы приносим креативные и практичные решения для\
                        Вашего бизнеса, высокое качество в ИТ,\
                        используем отличающийся подход в работе,\
                        поощряем возрастающую зарплату за достоинства.",
        'Paragraph': {
            'paragraph_1': "У нас работают специалисты в области консалтинга и информационных технологий,\
                        имеющие многолетний опыт в областях ИТ и бизнеса.\
                        Мы создаем и развиваем Ваши конкурентные преимущества,\
                        которые привлекают новых клиентов,\
                        повышают лояльность существующих и не оставляют никаких шансов конкурентам.",
            'paragraph_2': "Для эффективного решения Баших  бизнес задач  мы привлекаем ведущих консультантов,\
                        ИТ-специалистов и экспертов в области современных технологий для определения\
                        стратегии развития компании, разработки целевой архитектуры информационных систем,\
                        вычислительной инфраструктуры и подходов к обеспечению информационной безопасности,\
                        что позволяет значительно снизить затраты компании и увеличить эффект от инвестиций в ИТ.",
            'paragraph_3': "Мы предлагаем индивидуальные высокотехнологические решения,\
                        которые помогут Вам стать успешнее в вашей отрасли.\
                        Многолетний опыт работы помогает нам разрабатывать эффективные\
                        стратегические и консалтинговые решения не только для Армянского,\
                        Российского, но и для Международного рынка. Мы стремимся сочетать высочайшее качество кода,\
                        объективно красивый дизайн и новые технологические решения при\
                        разработке проектов любых масштабов от сайтов-визиток и\
                        интернет-магазинов до эксклюзивных интернет-решений.",
            'paragraph_4': "Все, что необходимо для успешного веб-проекта Вы сможете найти в списке наших услуг.\
                        Вы можете заказать комплекс услуг \"под ключ\" или каждую услугу отдельно.\
                        Мы нацелены на долгосрочное, а главное эффективное сотрудничество и партнерство.\
                        При заказе наших услуг обеспечим не только своевременное создание индивидуального,\
                        качественного сайта, обеспечиваем максимальную отказоустойчивость и\
                        продвижение в рейтинге популярных поисковых сервисов.",
        },
        'Principles': {
            'Title': "Наши принципы",
            'items': {
                'text_1': "Профессионализм и компетентность",
                'text_2': "Соблюдение этики во всем и со всеми.",
                'text_3': "Чистый и документированный код",
                'text_4': "Доверительные отношения с клиентами",
                'text_5': "Поиск нестандартных инновационных решение",
                'text_6': "Цены соответствующие качеству.",
                'text_7': "Не перестающее саморазвитие.",
                'text_8': "Высокий результат выше всяких похвал.",
            },
        },
        'Our_look': {
            'Title': "Наш взгляд",
            'Author': Markup("С уважением <br> команда «Master Mind» LLC"),
            'Paragraph': {
                'item_1': "В первую очередь, интересуясь нами, Вы должны знать,\
                            что мы играем открыто. Каждый документ, который подпишем,\
                          каждое соглашение, в которое придем в деловом кругу,\
                          осуществится на высоком уровне в рамках соглашения и закона.\
                          Исключительно всей командой являясь закоренелыми патриотами,\
                          мы намерены улучшить качество работы в международном масштабе,\
                          уровень обслуживания местных и иностранных клиентов,\
                          условия трудящихся в нашей компании и, в конце концов,\
                          мы намерены улучшить экономику страны.",
            },
            'Our_approach': {
                'Title': "Наши подходы",
                'items': {
                    'item_1': {
                        'id': "One",
                        'icon': "fas fa-user-tie",
                        'title': "Узнаём наших клиентов",
                        'description': {
                            'Paragraph_1': "До начала работы мы вникаемся в малейшие\
                                            детали деятельности нашего клиента,\
                                            чтобы создать удовлетворительный\
                                            продукт для индивидуального заказчика.",
                        },
                    },
                    'item_2': {
                        'id': "Two",
                        'icon': "fa fa-pie-chart",
                        'title': "Боремся за Ваш прибыль",
                        'description': {
                            'Paragraph_1': "Создаем самый качественный, надежный,\
                                            легкий, эффективный и продвинутый сайт\
                                            для долгосрочного достижения максимальной прибыли.",
                        },
                    },
                    'item_3': {
                        'id': "Three",
                        'icon': "fas fa-info-circle",
                        'title': "Ценим и уважаем трудящихся",
                        'description': {
                            'Paragraph_1': "Уделяем достойное внимание не только клиентам,\
                                            но и работникам, сделая обязательства желательными\
                                            и отдых достигаемым, поскольку залог успеха\
                                            зависит от всех и каждого.",
                        },
                    },
                },
            },
        },
        'History': {
            'Title': "Наша история",
            'Histories': {
                'Startup': {
                    'Title': 'Стартавалы',
                    'Sub_Title': 'Master Mind',
                    'Year': '2015 - 2016',
                    'Location_City': 'Ереван',
                    'Description': 'Lorem ipsum dolor sit amet,\
                                    consectetuer adipiscing elit.\
                                    Aenean commodo ligula eget dolor.\
                                    Aenean massa. Cum sociis natoque\
                                    penatibus et magnis dis parturient montes,\
                                    nascetur ridiculus mus.\
                                    Donec quam felis, ultricies nec,\
                                    pellentesque eu, pretium quis, sem.',
                    'ToDo': {
                        1: "Lorem ipsum dolor sit amet",
                        2: "Maecenas tempus tellus eget",
                        3: " dolor sit amet tempus tellus eget"
                    },
                }
            },
        },
    },
    'Portfolio': {
        'items': {
            'BestCon': {
                'Title': "Бэсткон",
                'Short_Description': "Строительно-инвестиционная компания",
                'Description': "Lorem ipsum dolor sit amet,\
                            consectetur adipisicing elit.\
                            Autem, repellat, vitae porro\
                            ex expedita cumque nulla.",
                'Images': {
                    'src': components.Find.Images(Path='Portfolio',
                                                  Name='bestcon',
                                                  Language='Russian'),
                    'Title': [
                        "Главная Страница",
                        "Новостройки",
                        "Выгодная ипотека",
                    ],
                    'Description': [
                        "Агентство недвижимости Бэсткон Более 15 лет успешной работы на рынке недвижимости!",
                        "Это страница сделана на JS и PHP",
                        "Подбор оптимальной программы",
                    ],
                },
                'Feedback': {
                    'Client': {
                        'Title': 'Отзыв Клиента',
                        # 'Paragraph': 'Хорошая команда интересные методы работы,\
                        #              могу точно сказать эти парни профессионалы своего дела.',
                        'Paragraph': Markup("В первую очередь, интересуясь нами, Вы должны знать,\
                                     что мы играем открыто. Каждый документ, который подпишем,\
                                     каждое соглашение, в которое придем в деловом кругу,\
                                     осуществится на высоком уровне в рамках соглашения и закона.\
                                     Исключительно всей командой являясь закоренелыми патриотами,\
                                     мы намерены улучшить качество работы в международном масштабе,\
                                     уровень обслуживания местных и иностранных клиентов,\
                                     условия трудящихся в нашей компании и, в конце концов,\
                                     мы намерены улучшить экономику страны.\
                                     <p>Хорошая команда интересные методы работы,\
                                     могу точно сказать эти парни профессионалы своего дела.</p>"),
                        'Sign': Markup("С уважением <br> клиент проекта «БестКон» LLC"),
                    },
                    'Team': {
                        'Title': 'Создатель',
                        'Name': 'Гор Варданян',
                        'Paragraph': Markup("Хорошый клиент интересные методы работы,\
                                     могу точно сказать этот профессионал своего дела."),
                        'Position': "Веб Программист",
                        'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/avatar3.jpg",
                        'Sign': Markup("С уважением"),
                    },
                },
                'Info': {
                    'Data': {
                        'Title': ["Названия", "Информация"],
                        'Category': ["Категория", "э-коммерция, строительство, информация"],
                        'Author': ["Автор", "Ашот Абгарян"],
                        'Year': ["Год", "2010"],
                    },
                    'Description': {
                        'Title': "Описание",
                        'Paragraph': Markup("Лорем Ипсум морковь,\
                                            расширенные которой скидках.\
                                            Радости в жизни, равную ему,\
                                            потому что она раза свободного\
                                            времени задолженность по счету.\
                                            <p>Дом равного ему с самого получения.</p>"),
                        'Preview': {
                            'Label':  "Посмотреть",
                            'href': "https://bestcon.ru"
                        },
                    },
                },
            },
            'Liederlernen': {
                'Title': "Онлайн Школа",
                'Short_Description': "Онлайн школа пианистов,\
                                которая поможет вам осуществить\
                                свою мечту шаг за шагом.\
                                Итак, если вы всегда хотели\
                                научиться играть на пианино,\
                                тогда вы сделали отличный первый шаг!",

                # 'Description': "Проект Liederlernen.de\
                #                 родился от любви к музыке,\
                #                 от страсти к урокам музыки и\
                #                 желания нести радость музыки в мир.\
                #                 Мы верим, что музыка не знает границ,\
                #                 и приглашаем вас в нашу страсть!",

                'Images': {
                    'src': components.Find.Images(Path='Portfolio',
                                                  Name='liederlernen',
                                                  Language='Russian'),
                    'Title': [
                        "Главная Страница",
                        "Урокы",
                        "Урокы",
                    ],
                    'Description': [
                        "Ваша мечта научиться играть на пианино теперь может сбыться!",
                        "Страница курсов которые разделены на блоки.",
                        "Страница курсов которые разделены на блоки.",
                    ],
                },
                'Feedback': {
                    'Client': {
                        'Title': 'Отзыв Клиента',
                        # 'Paragraph': 'Хорошая команда интересные методы работы,\
                        #              могу точно сказать эти парни профессионалы своего дела.',
                        'Paragraph': Markup("В первую очередь, интересуясь нами, Вы должны знать,\
                                     что мы играем открыто. Каждый документ, который подпишем,\
                                     каждое соглашение, в которое придем в деловом кругу,\
                                     осуществится на высоком уровне в рамках соглашения и закона.\
                                     Исключительно всей командой являясь закоренелыми патриотами,\
                                     мы намерены улучшить качество работы в международном масштабе,\
                                     уровень обслуживания местных и иностранных клиентов,\
                                     условия трудящихся в нашей компании и, в конце концов,\
                                     мы намерены улучшить экономику страны.\
                                     <p>Хорошая команда интересные методы работы,\
                                     могу точно сказать эти парни профессионалы своего дела.</p>"),
                        'Sign': Markup("С уважением <br> клиент проекта «Онлайн Школа» LLC"),
                    },
                    'Team': {
                        'Title': 'Создатель',
                        'Name': 'Гор Варданян',
                        'Paragraph': Markup("Хорошый клиент интересные методы работы,\
                                     могу точно сказать этот профессионал своего дела."),
                        'Position': "Веб Программист",
                        'Image': "https://agmstudio.io/themes/material-style/2.4.4/assets/img/demo/avatar3.jpg",
                        'Sign': Markup("С уважением"),
                    },
                },
                'Info': {
                    'Data': {
                        'Title': ["Названия", "Информация"],
                        'Category': ["Категория", "э-коммерция, учёба, музыкальный, блог"],
                        'Author': ["Автори", "Александр Шлегер, Дрор Карташ"],
                        'Year': ["Год", "2014"],
                    },
                    'Description': {
                        'Title': "Описание",
                        'Paragraph': Markup("Проект Liederlernen.de\
                                             родился от любви к музыке,\
                                             от страсти к урокам музыки и\
                                             желания нести радость музыки в мир.\
                                             Мы верим, что музыка не знает границ,\
                                             и приглашаем вас в нашу страсть!\
                                            <p>«Музыка выражает то, что нельзя\
                                            сказать и о чем нельзя молчать».\
                                            Виктор Хюго</p>"),
                        'Preview': {
                            'Label':  "Посмотреть",
                            'href': "https://liederlernen.de"
                        },
                    },
                },
            },
        }
    },
    'Services': {
        'IT Аудит': {
            'Title': "IT Аудит",
            'Texts': {
                'Left': {
                    1: "Ежедневно система информационных\
                        технологий растёт и усложняется,\
                        занимая все больше времени и финансов.\
                        Однако результаты не всегда оправдывают\
                        затраты на обслуживание ИТ-структуры.\
                        Со временем удобство и привычное\
                        ведение дел сменяются вновь появившимися\
                        рисками. Подобные ситуации требуют контроля\
                        руководителями как изнутри,\
                        так и независимыми экспертами – с внешней стороны.\
                        Для получения своевременной, актуальной и\
                        систематизированной информации заказывают IT-аудит.",

                    2: Markup("В основном аудит стандартизирован под <strong>международные стандарты\
                                ISA 401, CobiT</strong>, Положения по <strong>международной аудиторской\
                                практике 1002, 1003, 1004, 1008, 1009.</strong>\
                                Однако есть и отечественный стандарт\
                                – <span class='color-primary'>\
                                «Аудит в условиях <span class='color-warning'>\
                                компьютерной обработки данных</span> <strong>(КОД)</strong>»</span>."),

                    3: "Практически все аудиторские компании предоставляют ряд документов\
                        по итогам проверочных работ. Как правило, это отчеты по результатам\
                        IT-аудита компании в целом, а также об исходе проверки системы\
                        информационной безопасности предприятия. К дополнительным\
                        документам относятся рекомендации по устранению\
                        несогласованностей в бизнес-процессах, планы развития ИТ-структуры\
                        организации, отчетность о текущем состоянии системы, а также другая\
                        документация, ранее согласованная сторонами.",
                },
                'Right': {
                    2: "На сегодня можно выделить шесть\
                        основных разновидностей услуг\
                        по аудиту IT-инфраструктуры.",
                    'Numbers': [
                        "Первая услуга – это обследование ИТ, которое выполняется\
                        частным образом. Эта услуга включает в себя сбор информации,\
                        необходимой для проведения других работ. При обследовании\
                        аудиторы не анализируют неточности либо ошибки и не\
                        оценивают состояние инфраструктуры.",

                        "Следующая вторая услуга представляет собой экспертную\
                        оценку ИТ. Аудиторы оценивают целесообразность и\
                        адекватность финансирования тех или иных бизнес-решений.",

                        "К услугам технического аудита относятся сбор и анализ\
                        информации о технической составляющей ИТ-инфраструктуры.\
                        Этот вид работы отличается узкой специализацией и небольшим объемом.",

                        "При аудиторской проверке бизнес-процессов обычно назначается\
                        лицо, ответственное за ведение различных процессов, а также\
                        оценивается поведение персонала и клиентов. Кроме этого, при\
                        проведении такого аудита проводится анализ документации.",

                        "Аудит критерия ИТ включает в себя сбор информации об\
                        определенных частях и процессах ИТ-структуры, а также выдачу\
                        рекомендаций по какому-то конкретному критерию.",

                        "Название комплексный аудит говорит само за себя. Это вид\
                        проверки, при котором осуществляется анализ взаимосвязи\
                        процессов, обеспечивающих полную функциональную работу IT-инфраструктуры.",
                    ],
                },
            },
            'Services': {},
        },
        'Бизнес Анализ': {
            'Title': "Бизнес Анализ",
            'Texts': {
                'Left': {
                    1: "Бизнес-анализ — деятельность,"
                       "которая делает возможным проведение"
                       "Изменений в организации,"
                       "приносящих пользу Заинтересованным Сторонам,"
                       "путём выявления Потребностей и обоснования Решений,"
                       "описывающих возможные пути реализации Изменений."
                       "Основная задача бизнес-анализа - это сделать возможным"
                       "проведение Изменений в организации, путем реализации"
                       "выбранного Решения. Решение разрабатывается с целью"
                       "устранения выявленных в процессе бизнес-анализа"
                       "Бизнес-проблем. Понятие Решение включает в себя"
                       "широкий диапазон возможных путей устранения выявленных"
                       "Бизнес-проблем: разработка новых или изменение"
                       "существующих бизнес-процессов или бизнес-правил,"
                       "оптимизация организационной структуры организации,"
                       "разработка новых стратегических"
                       "планов организации и т.п.",

                    2: Markup("Исторически сложилось так, что бизнес-анализ "
                              "был наиболее востребован и долгое время"
                              "развивался в области информационных"
                              "технологий. В данной области наиболее"
                              "распространенным Решениемявляется автоматизация"
                              "бизнес-процессов организации, т.е. разработка"
                              "информационной системы. В данном случае"
                              "бизнес-аналитик отвечает за выявление"
                              "бизнес-требований по отношению к"
                              "бизнес-процессам и/или бизнес-правилам,"
                              "которые будут автоматизированы в рамках"
                              "реализации Решения. В рамках инициатив по"
                              "разработке информационных систем (IT проектов)"
                              "бизнес-аналитик тесно взаимодействует с"
                              "представителями профессии "
                              "“<a target='_blang'"
                              "href='http://profstandart.rosmintrud."
                              "ru/obshchiy-informatsionnyy-blok/natsionalnyy-"
                              "reestr-professionalnykh-standartov/reestr-"
                              "professionalnykh-standartov/index.php?ELEMENT_"
                              "ID=50437'>Системный аналитик</a>”."),

                    3: "Достаточно часто в IT проектах один человек"
                       "может совмещать в своей работе обе роли,"
                       "т.е. бизнес- и системный аналитик.",
                },
                'Right': {
                    2: "Бизнес-анализ как дисциплина тесно связан с анализом "
                       "требований, но нацелен на определение изменений для "
                       "организации, которые требуются для того, "
                       "чтобы организация достигла стратегических целей. "
                       "Эти изменения включают изменения в стратегии, "
                       "структуре, политике, процессах и "
                       "информационных системах.",
                    'Collaps': {
                            'item_1': {
                                    'id': "One",
                                    'title': "Разработка стратегии внедрения"
                                             "систем бизнес-аналитики",
                                    'description': {
                                            'Paragraph_1': "Определение"
                                                           "состава информации,"
                                                           "который следует"
                                                           "анализировать для"
                                                           "повышения"
                                                           "эффективности"
                                                           "бизнеса",

                                            'Paragraph_2': "Выявление возможностей по получению требуемых данных",
                                            'Paragraph_3': "Проектирование целевой архитектуры систем бизнес-аналитики",
                                            'Paragraph_4': "Выявление необходимых изменений в бизнес-процессах, адаптация учетных систем и изменение формотчетности",
                                            'Paragraph_5': "Разработка и внедрение системы ключевых показателей эффективности (KPI)",
                                    },
                            },
                            'item_2': {
                                    'id': "Two",
                                    'title': "Разработка функционально-технических требований",
                                    'description': {
                                            'Paragraph_1': "Обследование бизнес-процессов заказчика, консолидация и формализация бизнес-требований к BI-системам",
                                            'Paragraph_2': "Разработка документов «Техническое задание», «Функциональные требования» и т.п.",
                                            'Paragraph_3': "Обследование ИТ-ландшафта заказчика",
                                            'Paragraph_4': "Формирование технических требований, ИТ-архитектуры систем на основе выявленных бизнес-требований и с учетом имеющейся ИТ-инфраструктуры",
                                            'Paragraph_5': "Разработка рекомендаций по выбору платформ, удовлетворяющих сформированным функционально-техническим требованиям",
                                            'Paragraph_6': "Формирование документов «Технический проект», «Техническая спецификация», «Описание архитектуры системы» и т.п.",
                                    },
                            },
                            'item_3': {
                                    'id': "Three",
                                    'title': "Анализ источников данных",
                                    'description': {
                                            'Paragraph_1': "Обследование источников данных",
                                            'Paragraph_2': "Определение, формализация состава объектов и атрибутов, необходимых для дальнейшего анализа",
                                            'Paragraph_3': "Сегментация данных по степени их значимости для анализа",
                                            'Paragraph_4': "Определение возможностей расширения состава получаемых данных с привлечением внешних дополнительных источников",
                                    },
                            },
                            'item_4': {
                                    'id': "Four",
                                    'title': "Разработка корпоративных хранилищ данных и витрин данных",
                                    'description': {
                                            'Paragraph_1': "Проектирование и разработка ETL-процедур: извлечение, трансформация и загрузка данных",
                                            'Paragraph_2': "Разработка процедур и инструментов для сопоставления данных из разных источников (бизнес-правила, общие справочники, таблицы сопоставлений и т.п.)",
                                            'Paragraph_3': "Определение и реализация сценариев очистки и трансформации данных",
                                            'Paragraph_4': "Проектирование объектной модели хранилища данных и целевой архитектуры хранилища данных",
                                            'Paragraph_6': "Разработка хранилища данных",
                                            'Paragraph_7': "Документирование разработанной функциональности",
                                    },
                            },
                            'item_5': {
                                    'id': "Five",
                                    'title': "Разработка дизайна интерфейса системы",
                                    'description': {
                                            'Paragraph_1': "Исследование бизнес-процессов заказчика, выявление оптимальных сценариев анализа данных",
                                            'Paragraph_2': "Проектирование "
                                                           "дизайна "
                                                           "аналитических "
                                                           "панелей в соответствии со сценариями анализа, специальными требованиями заказчика (корпоративный дизайн, brandbook),"
                                                           "визуальными возможностями выбранной платформы",
                                            'Paragraph_3': "Сегментация данных по степени их значимости для анализа",
                                            'Paragraph_4': "Определение возможностей расширения состава получаемых данных с привлечением внешних дополнительных источников",
                                    },
                            },
                            'item_6': {
                                    'id': "Six",
                                    'title': "Настройка и разработка аналитических панелей, дашбордов",
                                    'description': {
                                            'Paragraph_1': "Разработка модели данных для реализации аналитической отчетности",
                                            'Paragraph_2': "Разработка скриптов загрузки данных (из источников, витрин данных) в модель данных аналитического приложения",
                                            'Paragraph_3': "Разработка визуальной части – аналитических отчетов (панелей, дашбордов)",
                                            'Paragraph_4': "Разработка регламентных отчетов и настройка периодической доставки отчетов пользователям",
                                            'Paragraph_5': "Реализация правил разграничения прав доступа на уровне отчетов или на уровне данных в рамках одного отчета",
                                    },
                            },
                            'item_7': {
                                    'id': "Seven",
                                    'title': "Техническая поддержка и аудит аналитических решений",
                                    'description': {
                                            'Paragraph_1': "Консультации по функциональности и характеристикам системы, аудит настроек системы",
                                            'Paragraph_2': "Анализ и предоставление инструкций по устранению ошибок в системе",
                                            'Paragraph_3': "Анализ и "
                                                           "исправление ошибок пользователей системы или ошибок, допущенных при конфигурировании системы",
                                            'Paragraph_4': "Модификации системы, документирование модификаций",
                                            'Paragraph_5': "Разработка и актуализация документации",
                                            'Paragraph_6': "Взаимодействие с "
                                                           "производителем "
                                                           "программного "
                                                           "обеспечения в "
                                                           "части "
                                                           "формирования "
                                                           "запросов на "
                                                           "исправление "
                                                           "выявленных ошибок "
                                                           "ПО и предоставление"
                                                           "заказчику информации по результатам выполнения запросов",
                                            'Paragraph_7': "Информирование о выходе новых версий и функциональных изменениях платформы",
                                            'Paragraph_8': "Перевод аналитических систем на новые версии ПО",
                                            'Paragraph_9': "Мониторинг и выявление «узких мест» в производительности аналитических приложений",
                                            'Paragraph_10': "Оптимизация "
                                                            "разработанной функциональности с целью повышения производительности (на уровне ETL, модели данных, расчетов и т.п.)",
                                    },
                            },
                    },
                },
            },
            'Services': {},
        },
        'Дизайн UX-UI': {
            'Title': "Дизайн UX-UI",
            'Texts': {
                'Left': {
                    1: "Ежедневно система информационных\
                        технологий растет и усложняется,\
                        занимая все больше времени и финансов.\
                        Однакорезультаты не всегда оправдывают\
                        затраты на обслуживание ИТ-структуры.\
                        Со временем удобство и привычное\
                        ведение дел сменяются вновь появившимися\
                        рисками. Подобные ситуации требуют контроля\
                        руководителями как изнутри,\
                        так и независимыми экспертами – с внешней стороны.\
                        Для получения своевременной, актуальной и\
                        систематизированной информации заказывают IT-аудит.",

                    2: Markup("В основном аудит стандартизирован под <strong>международные стандарты\
                                ISA 401, CobiT</strong>, Положения по <strong>международной аудиторской\
                                практике 1002, 1003, 1004, 1008, 1009.</strong>\
                                Однако есть и отечественный стандарт\
                                – <span class='color-primary'>\
                                «Аудит в условиях <span class='color-warning'>\
                                компьютерной обработки данных</span> <strong>(КОД)</strong>»</span>."),

                    3: "Практически все аудиторские компании предоставляют ряд документов\
                        по итогам проверочных работ. Как правило, это отчеты по результатам\
                        IT-аудита компании в целом, а также об исходе проверки системы\
                        информационной безопасности предприятия. К дополнительным\
                        документам относятся рекомендации по устранению\
                        несогласованностей в бизнес-процессах, планы развития ИТ-структуры\
                        организации, отчетность о текущем состоянии системы, а также другая\
                        документация, ранее согласованная сторонами.",
                },
                'Right': {
                    2: "На сегодня можно выделить шесть\
                        основных разновидностей услуг\
                        по аудиту IT-инфраструктуры.",
                    'Numbers': [
                        "Первая услуга – это обследование ИТ, которое выполняется\
                        частным образом. Эта услуга включает в себя сбор информации,\
                        необходимой для проведения других работ. При обследовании\
                        аудиторы не анализируют неточности либо ошибки и не\
                        оценивают состояние инфраструктуры.",

                        "Следующая, вторая, услуга представляет собой экспертную\
                        оценку ИТ. Аудиторы оценивают целесообразность и\
                        адекватность финансирования тех или иных бизнес-решений.",

                        "К услугам технического аудита относятся сбор и анализ\
                        информации о технической составляющей ИТ-инфраструктуры.\
                        Этот вид работы отличается узкой специализацией и небольшим объемом.",

                        "При аудиторской проверке бизнес-процессов обычно назначается\
                        лицо, ответственное за ведение различных процессов, а также\
                        оценивается поведение персонала и клиентов. Кроме этого, при\
                        проведении такого аудита проводится анализ документации.",

                        "Аудит критерия ИТ включает в себя сбор информации об\
                        определенных частях и процессах ИТ-структуры, а также выдачу\
                        рекомендаций по какому-то конкретному критерию.",

                        "Название комплексный аудит говорит само за себя. Это вид\
                        проверки, при котором осуществляется анализ взаимосвязи\
                        процессов, обеспечивающих полную функциональную работу IT-инфраструктуры.",
                    ],
                },
            },
            'Services': {},
        },
    },
}


Contact = {
    'Page': {
        'Brand': Title['Brand_Name'],
        'Address': {
            'Location': {
                'label': "795 Folsom Ave, Suite 600",
                'icon': "zmdi zmdi-pin",
                'color': "danger"
            },
            'State': {
                'label': "San Francisco, CA 94107",
                'icon': "zmdi zmdi-map",
                'color': "warning"
            },
            'eMail': {
                'label': "example@domain.com",
                'icon': "zmdi zmdi-email",
                'color': "info"
            },
            'Phone': {
                'label': "+34 123 456 7890 ",
                'icon': "zmdi zmdi-phone",
                'color': 'royal'
            },
            # 'Fax': {
            #     'label': "+34 123 456 7890 ",
            #     'icon': "fa fa-fax",
            #     'color': "success"
            # },
        },
        'Form': {
            'Title': 'Напишите нам',
            'input': {
                'Name': {
                    'label': "Имя",
                    'placeholder': "Фамилия, Имя, Отчество",
                    'name': "Name",
                    'type': "text",
                },
                'Email': {
                    'label': "Е-Майл",
                    'placeholder': "Электронная почта",
                    'name': "Email",
                    'type': "email",
                },
                'Subject': {
                    'label': "Тема",
                    'placeholder': "Тема",
                    'name': "Subject",
                    'type': "text",
                },
                'Message': {
                    'label': "Сообщение",
                    'placeholder': "Ваше сообщение...",
                    'name': "Message",
                    'type': "textarea",
                },
            },
            'Button_label': "ОТПРАВИТЬ",
        }
    },
}


Message = {
    'alert': {
        'Text': "Сообщения"
    },
    'Нет информации': "Нет информации"
}


data = {
    'language': 'ru',
    'logo': "/static/site/Master_Mind/img/logo.png",
    'title_icon': "/static/site/Master_Mind/img/title_icon.png",
    'urls': routes,
    'LT': Title['Company'],
    'Brand_Name': Title['Brand_Name'],
    'Header': Header,
    'Services': Services,
    'Info': Info,
    'Slider': Slider,
    'Contact': Contact,
    'Message': Message,
    'Subscribe': Subscribe,
}
