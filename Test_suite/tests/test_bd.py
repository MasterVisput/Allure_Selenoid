from Test_suite.DB.client import DBClient


def test():
    data_1 = {'language_id': '1',
              'name': 'Mouse',
              'tag': 'Per',
              'meta_title': 'Per',
              'meta_description': 'Perr',
              'meta_keyword': 'perr'}
    data_2 = {'name': 'Vouse+21'}
    client = DBClient()
    client.insert_entity(table_name='oc_product_description', data=data_1)
    client.update_entity(table_name='oc_product_description', data=data_2, condition='name="Mouse"')
    l = client.select_entity(table_name='oc_product_description',
                             column='name',
                             conditions='name="Vouse+21"')

    client.commit()
    assert len(l) != 0
    client.delete_rows(table_name='oc_product_description', condition="name='Mouse'")
