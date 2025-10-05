class Student:
    def __init__(self, name, grades):
        self.name = name              # نام دانش‌آموز
        self.grades = grades          # لیست نمرات

    def calculate_average(self):
        if not self.grades:
            return 0.0                # اگر لیست نمرات خالی باشد، معدل صفر است
        return sum(self.grades) / len(self.grades)  # محاسبه معدل
