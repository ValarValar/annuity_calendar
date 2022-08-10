class PaymentCalendar:
    def __init__(self, cr_sum, percent, month_count):
        self.cr_sum = cr_sum
        self.percent = percent
        self.month_count = month_count
        self.month_percent = self.percent / 12 / 100

    def annuity_coef(self):
        """
            Коэффициент аннуитета рассчитывается следующим образом:
            m × (1 + m)ⁿ  /  (1 + m)ⁿ — 1
            где m — процентная ставка в месяц, равная годовой ставке, поделённой на 12,
            а n — количество платежей.
        """
        value = (1 + self.month_percent) ** self.month_count
        ret_value = self.month_percent * value / (value - 1)
        return ret_value

    def annuity_payment(self):
        """
            Сумма кредита × Коэффициент аннуитета
        """
        return round(self.cr_sum * self.annuity_coef(), 2)

    def print_calendar(self):
        print(f"Сумма кредита: {self.cr_sum}")
        print(f"Процентная ставка: {self.percent}%")
        print(f"Срок: {self.month_count} месяцев")
        annuity_payment_value = self.annuity_payment()
        left_sum_main_debt = self.cr_sum
        for i in range(1, self.month_count + 1):
            percent_debt = round(self.month_percent * left_sum_main_debt, 2)
            main_debt_payment = round(annuity_payment_value - percent_debt, 2)
            print(
                f"Месяц: {i}|"
                f"Ежемесячный платеж: {annuity_payment_value} |"
                f" Основной долг: {main_debt_payment} |"
                f" Долг по процентам: {percent_debt}|"
                f" Остаток основного долга: {left_sum_main_debt}"
            )
            left_sum_main_debt = round(left_sum_main_debt - main_debt_payment, 2)


PC = PaymentCalendar(100000, 13, 12)
PC.print_calendar()
