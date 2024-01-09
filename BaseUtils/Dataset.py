import secrets
import string


class Dataset(object):

    def __init__(self, employee_count=1, user_count=1):

        unique_number = str(int(secrets.token_hex(5), 16) % 10000000000)
        alphabet = string.ascii_letters
        unique_string = ''.join(secrets.choice(alphabet) for _ in range(6))

        user_name = 'User name' + unique_number

        if employee_count > 1:
            self.last_names = list()
            self.first_names = list()
            self.middle_names = list()
            self.full_names = list()
            self.emp_ids = list()
            for index in range(0, employee_count):
                self.last_names.append('EmpLast' + str(index) + unique_number)
                self.first_names.append('EmpFirst' + str(index) + unique_number)
                self.middle_names.append('EmpMiddle' + str(index) + unique_number)
                self.full_names.append('EmpFirst' + str(index) + unique_number + ' EmpMiddle' + str(index) +
                                       unique_number + ' EmpLast' + str(index) + unique_number)
                self.emp_ids.append('EmpId' + str(index) + unique_number[:3])
        else:
            self.last_name = 'EmpLast' + unique_number
            self.first_name = 'EmpFirst' + unique_number
            self.middle_name = 'EmpMiddle' + unique_number
            self.full_name = 'EmpFirst' + unique_number + ' EmpMiddle' + unique_number + ' EmpLast' + unique_number
            self.emp_id = 'EmpId' + unique_number[:4]

        if user_count > 1:
            self.user_names = list()
            self.passwords = list()
            for index in range(0, employee_count):
                self.user_names.append('UserName' + str(index) + unique_number)
                self.passwords.append('Password@' + str(index) + unique_number)
        else:
            self.user_name = 'UserName' + unique_number
            self.password = 'Password@' + unique_number
