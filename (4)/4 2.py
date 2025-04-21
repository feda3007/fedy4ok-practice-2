import sqlite3


class BarDatabase:
    def __init__(self, db_name="bar.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS drinks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                alcohol_content REAL NOT NULL,
                volume INTEGER NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cocktails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                strength REAL NOT NULL,
                composition TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.connection.commit()

    #учет алкогольных напитков
    def add_drink(self, name, alcohol_content, volume, price, quantity):
        self.cursor.execute('''
            INSERT INTO drinks (name, alcohol_content, volume, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, alcohol_content, volume, price, quantity))
        self.connection.commit()

    def view_all_drinks(self):
        self.cursor.execute('SELECT * FROM drinks')
        return self.cursor.fetchall()

    def update_drink_quantity(self, drink_id, quantity_change):
        self.cursor.execute('''
            UPDATE drinks 
            SET quantity = quantity + ? 
            WHERE id = ?
        ''', (quantity_change, drink_id))
        self.connection.commit()

    # 1.2) Учет ингредиентов
    def add_ingredient(self, name, quantity):
        self.cursor.execute('''
            INSERT INTO ingredients (name, quantity)
            VALUES (?, ?)
        ''', (name, quantity))
        self.connection.commit()

    def view_all_ingredients(self):
        self.cursor.execute('SELECT * FROM ingredients')
        return self.cursor.fetchall()

    #управление коктейлями
    def add_cocktail(self, name, composition, price):
        #рассчёт крепости коктейля на основе состава
        total_alcohol = 0
        total_volume = 0
        components = composition.split(',')

        for component in components:
            drink_name, volume = component.split(':')
            volume = int(volume.strip())
            self.cursor.execute('SELECT alcohol_content FROM drinks WHERE name = ?', (drink_name.strip(),))
            result = self.cursor.fetchone()
            if result:
                alcohol_content = result[0]
                total_alcohol += (alcohol_content * volume) / 100
                total_volume += volume

        strength = (total_alcohol / total_volume) * 100 if total_volume > 0 else 0

        self.cursor.execute('''
            INSERT INTO cocktails (name, strength, composition, price)
            VALUES (?, ?, ?, ?)
        ''', (name, strength, composition, price))
        self.connection.commit()

    def view_all_cocktails(self):
        self.cursor.execute('SELECT * FROM cocktails')
        return self.cursor.fetchall()

    #продажа
    def sell_drink(self, drink_id, quantity):
        self.cursor.execute('SELECT quantity FROM drinks WHERE id = ?', (drink_id,))
        current = self.cursor.fetchone()[0]
        if current >= quantity:
            self.update_drink_quantity(drink_id, -quantity)
            return True
        return False

    def sell_cocktail(self, cocktail_id):
        self.cursor.execute('SELECT composition FROM cocktails WHERE id = ?', (cocktail_id,))
        composition = self.cursor.fetchone()[0]
        components = composition.split(',')

        for component in components:
            drink_name, volume = component.split(':')
            drink_name = drink_name.strip()
            volume = int(volume.strip())

            self.cursor.execute('SELECT id, quantity FROM drinks WHERE name = ?', (drink_name,))
            result = self.cursor.fetchone()
            if not result or result[1] < volume:
                return False

        for component in components:
            drink_name, volume = component.split(':')
            drink_name = drink_name.strip()
            volume = int(volume.strip())

            self.cursor.execute('UPDATE drinks SET quantity = quantity - ? WHERE name = ?', (volume, drink_name))

        self.connection.commit()
        return True

    def close(self):
        self.connection.close()


def main():
    db = BarDatabase()

    while True:
        print("\nМеню I love drink:")
        print("1. Учет напитков")
        print("2. Управление коктейлями")
        print("3. Операции")
        print("4. Выйти")

        choice = input("\nВыберите раздел (1-4): ")

        if choice == "1":
            print("\nУчет напитков:")
            print("1. Добавить алкогольный напиток")
            print("2. Просмотреть все напитки")
            print("3. Добавить ингредиент")
            print("4. Просмотреть все ингредиенты")
            print("5. Пополнить запас напитка")

            sub_choice = input("Выберите действие (1-5): ")

            if sub_choice == "1":
                name = input("Название напитка: ")
                alcohol = float(input("Крепость (%): "))
                volume = int(input("Объем (мл): "))
                price = float(input("Цена: "))
                quantity = int(input("Количество: "))
                db.add_drink(name, alcohol, volume, price, quantity)
                print("Напиток добавлен!")

            elif sub_choice == "2":
                drinks = db.view_all_drinks()
                print("\nСписок напитков:")
                for drink in drinks:
                    print(
                        f"ID: {drink[0]}, Название: {drink[1]}, Крепость: {drink[2]}%, Объем: {drink[3]}мл, Цена: {drink[4]}, Остаток: {drink[5]}")

            elif sub_choice == "3":
                name = input("Название ингредиента: ")
                quantity = int(input("Количество: "))
                db.add_ingredient(name, quantity)
                print("Ингредиент добавлен!")

            elif sub_choice == "4":
                ingredients = db.view_all_ingredients()
                print("\nСписок ингредиентов:")
                for ing in ingredients:
                    print(f"ID: {ing[0]}, Название: {ing[1]}, Остаток: {ing[2]}")

            elif sub_choice == "5":
                drink_id = int(input("ID напитка: "))
                quantity = int(input("Количество для пополнения: "))
                db.update_drink_quantity(drink_id, quantity)
                print("Запас пополнен!")

        elif choice == "2":
            print("\nУправление коктейлями:")
            print("1. Добавить коктейль")
            print("2. Просмотреть все коктейли")

            sub_choice = input("Выберите действие (1-2): ")

            if sub_choice == "1":
                name = input("Название коктейля: ")
                composition = input("Состав (напиток:мл, напиток:мл): ")
                price = float(input("Цена: "))
                db.add_cocktail(name, composition, price)
                print("Коктейль добавлен!")

            elif sub_choice == "2":
                cocktails = db.view_all_cocktails()
                print("\nСписок коктейлей:")
                for cocktail in cocktails:
                    print(
                        f"ID: {cocktail[0]}, Название: {cocktail[1]}, Крепость: {cocktail[2]:.1f}%, Состав: {cocktail[3]}, Цена: {cocktail[4]}")

        elif choice == "3":
            print("\nОперации:")
            print("1. Продажа алкогольного напитка")
            print("2. Продажа коктейля")

            sub_choice = input("Выберите действие (1-2): ")

            if sub_choice == "1":
                drink_id = int(input("ID напитка: "))
                quantity = int(input("Количество: "))
                if db.sell_drink(drink_id, quantity):
                    print("Продажа оформлена!")
                else:
                    print("Недостаточно напитка в наличии!")

            elif sub_choice == "2":
                cocktail_id = int(input("ID коктейля: "))
                if db.sell_cocktail(cocktail_id):
                    print("Коктейль продан!")
                else:
                    print("Недостаточно ингредиентов для приготовления!")

        elif choice == "4":
            db.close()
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()