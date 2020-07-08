import mariadb


class DBClient():
    def __init__(self):
        self.connect = mariadb.connect(
            user='bn_opencart',
            password='',
            host='localhost',
            port=3306,
            database='bitnami_opencart'
        )

    def select_entity(self, table_name: str, column: str, conditions: str):
        cursor = self.connect.cursor()
        select_script = f'SELECT {column} FROM {table_name} WHERE {conditions}'
        cursor.execute(select_script)
        resp = cursor.fetchall()
        lst = []
        for i in range(len(resp)):
            lst.append(resp[i][0])
        return lst

    def commit(self):
        self.connect.commit()

    def close(self):
        self.connect.close()

    def insert_entity(self, table_name: str, data: dict):
        cursor = self.connect.cursor()
        columns = ','.join(list(data.keys()))
        new = []
        for item in list(data.values()):
            if isinstance(item, int):
                new.append(f'{item}')
            if isinstance(item, str):
                value = item.replace("'", "''") if "'" in item else item
                new.append(f"'{value}'")
        new = ','.join(new)
        insert_str = f'INSERT INTO {table_name} ({columns}) VALUES ' f'({new})'
        cursor.execute(insert_str)


    def delete_rows(self, table_name: str, condition: str = None):
        cursor = self.connect.cursor()
        if condition:
            delete_str = f'DELETE FROM {table_name} WHERE {condition}'
        else:
            delete_str = f'DELETE FROM {table_name}'
        cursor.execute(delete_str)

    def update_entity(self, table_name: str, condition: str, data: dict):
        cursor = self.connect.cursor()
        new = []
        for key, val in data.items():
            if isinstance(val, str):
                value = val.replace("'", "''") if "'" in val else val
                new.append(f"{key}='{value}'")
            else:
                new.append(f'{key}={val}')
        query = ','.join(new)

        upd_query = f'UPDATE {table_name} SET {query}  WHERE {condition}'
        cursor.execute(upd_query)

