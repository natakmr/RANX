import func
import sys

def main():
    source_dir = sys.argv[1]
    files = ['1.xlsx', '2.xlsx', '3.xlsx']
    path_to_files = list(map(lambda s: f"{source_dir}/{s}", files))
    tables = func.read_excel_files(path_to_files)
    updated_tables = func.reindex_tables(tables)

    destination_dir = sys.argv[2]
    updated_files = ['res_1.xlsx', 'res_2.xlsx', 'res_3.xlsx']
    path_to_results = list(map(lambda s: f"{destination_dir}/{s}", updated_files))

    for updated_table, filename in zip(updated_tables, path_to_results):
        updated_table.to_excel(filename, index=False)

if __name__ == "__main__":
    main()
