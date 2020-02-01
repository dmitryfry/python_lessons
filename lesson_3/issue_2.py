def user_data(firstname, surname, birth_year, town, email, phone):
    print(firstname, surname, birth_year, town, email, phone)

firstname, surname, birth_year, town, email, phone = input("введите имя, фамилию, год рождения, город почту и телефон через пробел: ").split()

user_data(firstname=firstname, surname=surname, birth_year=birth_year, town=town, email=email, phone=phone)
