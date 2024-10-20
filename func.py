import pandas as pd

def read_excel_files(filenames):
    tables = [pd.read_excel(file) for file in filenames]
    return tables


def reindex_tables(tables):
    last_max_id = 0
    updated_tables = []

    for table in tables:
        table['id'] = range(last_max_id + 1, last_max_id + len(table) + 1)
        last_max_id = table['id'].max()
        updated_tables.append(table)

    return updated_tables
