# Русская терминология ERA SOFT

Этот документ устанавливает обязательный словарь пользовательского интерфейса
ERA SOFT. Русские названия применяются только на уровне отображения. Английские
имена DocType, полей, маршрутов, API, модулей и исходного кода не переименовываются.

## Языковая стратегия

1. **Русский (`ru`)** — основной язык пользователей и язык сайта по умолчанию.
2. **Кыргызский (`ky`)** — следующий язык локализации после стабилизации русского
   словаря.
3. **English (`en`)** — язык разработчиков, диагностики, исходного кода и
   интеграционных контрактов.

Пользователь может выбрать English в своих настройках. Миграции ERA SOFT не
должны возвращать такого пользователя на русский после осознанного выбора.

## Правила

- Один бизнес-смысл имеет один основной термин во всех Workspace, формах и отчетах.
- Английские идентификаторы не показываются пользователю, но остаются в коде.
- Для закрепленных названий используется написание `е`: **Счет**, **Отчеты**.
- `Project` в операционном учете строительства — **Объект**. Раздел верхнего
  уровня сохраняет согласованное название **Проекты**.
- `Material Request` используется как техническая сущность ERPNext для заявки на
  закупку и показывается пользователю как **Заявка на закупку**.
- `Account` в управленческом интерфейсе ERA показывается как **Статья затрат**.
  Английское слово допустимо только в коде и технической документации.
- Для `Purchase Order` закреплено **Заказ на закупку**; варианты «заказ на
  покупку» и «заказ поставщику» в интерфейсе не используются.
- Для `Payment Entry` закреплено **Оплата**; варианты «запись оплаты» и «платеж»
  не используются как название документа.

## Основной бизнес-словарь

| Внутренний источник | Стандарт ERA SOFT | Не использовать в интерфейсе |
|---|---|---|
| Customer | Клиент | Customer, Покупатель |
| Supplier | Поставщик | Supplier |
| Contractor | Подрядчик | Contractor |
| Employee | Сотрудник | Employee |
| Company | Компания | Company |
| Project | Объект | Project, Проект для отдельной карточки объекта |
| Projects | Проекты | Projects |
| Construction Site | Строительный объект | Construction Site |
| Building / Block | Корпус / блок | Building / Block |
| Floor | Этаж | Floor |
| Work Category | Вид работ | Work Category |
| Cost Category | Статья затрат | Cost Category |
| Account | Статья затрат | Account, Аккаунт |
| Cost | Себестоимость | Cost |
| Item | Номенклатура | Item, Товар в общем названии справочника |
| Warehouse | Склад | Warehouse |
| Site Warehouse | Склад объекта | Site Warehouse |
| Material Delivery | Поставка материалов | Material Delivery |
| Material Transfer | Перемещение материалов | Material Transfer |
| Material Consumption | Списание материалов | Material Consumption |
| Stock Entry | Движение запасов | Stock Entry |
| Purchase Request / Material Request | Заявка на закупку | Purchase Request, Запрос материала |
| Request for Quotation | Запрос предложения | Request for Quotation |
| Supplier Quotation | Предложение поставщика | Supplier Quotation |
| Purchase Order | Заказ на закупку | Purchase Order, Заказ на покупку, Заказ поставщику |
| Purchase Receipt | Приемка материалов | Purchase Receipt, Квитанция на покупку |
| Purchase Invoice | Счет поставщика | Purchase Invoice, Счет на покупку |
| Service Purchase | Закупка услуг | Service Purchase |
| Payment Entry | Оплата | Payment Entry, Запись оплаты, Платеж |
| Payment | Оплата | Payment |
| Advance Payment | Авансовая оплата | Advance Payment |
| Bank Account | Банковский счет | Bank Account |
| Bank Transaction | Банковская операция | Bank Transaction |
| Accounts Payable | Кредиторская задолженность | Accounts Payable, Счета к оплате |
| Accounts Receivable | Дебиторская задолженность | Accounts Receivable |
| General Ledger | Главная книга | General Ledger |
| Budget | Бюджет | Budget |
| Initial Budget | Первоначальный бюджет | Initial Budget |
| Revised Budget | Уточненный бюджет | Revised Budget |
| Committed Cost | Принятые обязательства | Committed Cost |
| Actual Cost | Фактическая себестоимость | Actual Cost |
| Paid Cost | Оплаченная себестоимость | Paid Cost |
| Forecast Cost | Прогнозная себестоимость | Forecast Cost |
| Remaining Budget | Остаток бюджета | Remaining Budget |
| Variance | Отклонение | Variance |
| Cash Flow | Денежный поток | Cash Flow |
| Task | Задача | Task |

## Навигация

| Внутреннее название | Пользовательское название |
|---|---|
| Dashboard | Главная |
| Construction | Строительство |
| Procurement | Закупки |
| Finance | Финансы |
| Projects | Проекты |
| Suppliers | Поставщики |
| Employees | Сотрудники |
| Reports | Отчеты |
| Settings | Настройки |

## Рабочие пространства и отчеты

| Внутренний источник | Стандарт ERA SOFT |
|---|---|
| Access | Доступ |
| Accounts Payable Summary | Сводка кредиторской задолженности |
| Bank Accounts | Банковские счета |
| Bank Transactions | Банковские операции |
| Budget Control | Контроль бюджета |
| Budget Variance Report | Отчет об отклонениях бюджета |
| Budgets | Бюджеты |
| Items | Номенклатура |
| Material Deliveries | Поставки материалов |
| Operations | Операции |
| Order and Receive | Заказы и приемка |
| Payables | Кредиторская задолженность |
| Payment Entries / Payments | Оплаты |
| Project Summary | Сводка по объектам |
| Project-wise Stock Tracking | Движение запасов по объектам |
| Purchase Analytics | Аналитика закупок |
| Purchase Invoices | Счета поставщиков |
| Purchase Order Analysis | Анализ заказов на закупку |
| Purchase Orders | Заказы на закупку |
| Purchase Receipts | Приемка материалов |
| Purchase Requests | Заявки на закупку |
| Request and Source | Заявки и выбор поставщика |
| Requests for Quotation | Запросы предложений |
| Role Permissions Manager | Управление правами ролей |
| Roles | Роли |
| Site Operations | Операции на объекте |
| Stock Entries | Движения запасов |
| Supplier Quotations | Предложения поставщиков |
| System | Система |
| System Settings | Системные настройки |
| Tasks | Задачи |
| Users | Пользователи |
| Warehouses | Склады |
| Website Settings | Настройки сайта |

## Тексты Workspace

| Английский исходник | Утвержденный русский текст |
|---|---|
| Executive overview using approved ERPNext records. Management indicators will be added only after their definitions are reviewed. | Обзор для руководства на основе утвержденных документов ERPNext. Управленческие показатели будут добавлены только после согласования их определений. |
| Primary operational workspace. This visual baseline links to standard ERPNext records and introduces no business automation. | Основное рабочее пространство. Визуальная версия использует стандартные документы ERPNext и не добавляет бизнес-автоматизацию. |

## Ежедневные действия, поля и статусы

| Внутренний источник | Стандарт ERA SOFT |
|---|---|
| Stock | Складской учет |
| Buying | Закупки |
| Home | Главная |
| Notification | Уведомления |
| Delivery Note | Накладная на отгрузку |
| Pick List | Лист комплектации |
| Tools | Инструменты |
| Setup | Настройка |
| Menu | Меню |
| Add | Добавить |
| Create New | Создать |
| Navigate to main content | Перейти к основному содержимому |
| name | Наименование |
| Clear all filters | Сбросить все фильтры |
| descending | По убыванию |
| Select All | Выбрать все |
| Click to sort by {0} | Сортировать по {0} |
| Click to sort by Supplier Name | Сортировать по поставщику |
| 0 Filter Applied | Фильтры не применены |
| You haven't created a {0} yet | Вы еще не создали: {0} |
| No {0} found with matching filters. Clear filters to see all {0}. | По заданным фильтрам не найдено: {0}. Сбросьте фильтры для просмотра всех записей. |
| Supplier Name | Поставщик |
| Title | Название |
| Date | Дата |
| Required By | Требуется к |
| Posting Date | Дата проведения |
| Due Date | Срок оплаты |
| Payment Type | Тип оплаты |
| Document has been submitted | Документ проведен |
| Draft | Черновик |
| Submitted | Проведено |
| Completed | Завершено |
| Cancelled | Отменено |
| Paid | Оплачено |
| Overdue | Просрочено |
| To Receive and Bill | Ожидает приемки и счета |
| Receive | Поступление |
| Pay | Выплата |
| Timesheet | Табель рабочего времени |
| Cancel | Отменить |
| Details | Основное |
| Terms | Условия |
| More Info | Дополнительно |
| Connections | Связи |
| Order Confirmation No | Номер подтверждения заказа |
| Is Subcontracted | Субподряд |
| Currency and Price List | Валюта и прайс-лист |
| Set Target Warehouse / Target Warehouse | Склад назначения |
| No. | № |
| Item Code | Код номенклатуры |
| Quantity | Количество |
| UOM | Ед. изм. |
| Rate | Цена |
| Amount | Сумма |
| Download | Скачать |
| Total Quantity | Общее количество |
| Total | Итого |
| Totals | Итоги |
| Grand Total | Общая сумма |
| In Words | Сумма прописью |
| Disable Rounded Total | Отключить округление итога |
| Rounded Total | Округленная сумма |
| Advance Paid (Company Currency) | Оплаченный аванс (в валюте компании) |
| Additional Discount | Дополнительная скидка |
| Comments | Комментарии |
| Type a reply / comment | Написать ответ / комментарий |
| Activity | Активность |
| New Email | Новое письмо |
| You last edited this | Вы редактировали последним |
| You created this | Вы создали документ |
| Assign | Назначить |
| Attachments | Вложения |
| Tags | Метки |
| Share | Поделиться |
| Last Edited By You | Последнее изменение вами |
| Created By You | Создано вами |

## Граница локализации и результаты проверки

Проверены ERA Workspace и ежедневные стандартные экраны `Material Request`,
`Purchase Order`, `Purchase Invoice`, `Payment Entry`, `Project` и `Supplier`.
ERA‑слой переводит их активные заголовки, поля, действия, вкладки и статусы.

Следующие английские значения не являются непереведенными UI‑терминами и в этой
фазе намеренно не изменяются:

- английские названия демонстрационных поставщиков, товаров, складов и единиц
  измерения — это данные справочников, а не labels;
- ранее сохраненный текст ленты Activity и сумма прописью в старых документах —
  данные существующих документов; их изменение было бы миграцией данных;
- `supplier`, `schedule_date`, `grand_total` и другие fieldname, видимые при
  включенном developer mode, — внутренние идентификаторы;
- бренд `ERPNext`, номера документов, коды номенклатуры и ISO‑коды валют не
  переводятся.

Frappe формирует некоторые счетчики доступности после подстановки числа
(`N Filters Applied`, `N of M`). Для нулевого состояния добавлен русский текст;
остальные динамические счетчики не являются бизнес-терминами и должны быть
исправлены upstream либо отдельным безопасным расширением, если станут видимым
пользовательским дефектом.

## Применение и восстановление

Миграция автоматически применяет русский baseline. Ручное применение:

```bash
cd ../frappe-bench
../toolchain/bin/bench --site era.localhost execute \
  era_soft.setup.localization.apply_russian_localization
../toolchain/bin/bench --site era.localhost clear-cache
```

Вернуть английский системный baseline, не меняя исходники ERPNext:

```bash
../toolchain/bin/bench --site era.localhost execute \
  era_soft.setup.localization.restore_russian_localization
../toolchain/bin/bench --site era.localhost clear-cache
```

## Техническая реализация

ERA‑слой находится в `era_soft/translations/ru.csv` и загружается после переводов
Frappe и ERPNext, поэтому может исправлять их формулировки без изменения upstream
файлов. Исходные английские строки должны оставаться стабильными: они являются
ключами перевода. Новая пользовательская строка считается готовой только после
добавления согласованного русского термина в этот документ и translation layer.
