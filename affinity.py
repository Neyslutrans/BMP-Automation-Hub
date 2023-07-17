from modules import paths
from modules.data_processing import affinity_dataframe
from modules.excel_operations import WorkbookManager
from modules.dataframe_operations import import_dataframe, export_dataframe_to_sheet


def main() -> None:
    try:
        file_paths = paths.PathManager.open_file_dialog()
        workbook = WorkbookManager.create_workbook()
        counter = 1

        for file in file_paths:
            try:
                print(f'Обрабатывается файл: {file}')
                df = import_dataframe(file)
                df = affinity_dataframe(df)
                sheet_name = f'{df["target"]} - {counter}'
                sheet = WorkbookManager.create_sheet(workbook, sheet_name)
                counter += 1

                export_dataframe_to_sheet(df['dataframe'], sheet)

                WorkbookManager.format_sheet(sheet, 'affinity')

            except Exception as e:
                print(f'Ошибка при обработке файла: {file}')
                print(f'Тип ошибки: {type(e).__name__}')
                print(f'Сообщение об ошибке: {str(e)}')
                continue

        name = paths.PathManager.save_file_dialog()
        WorkbookManager.save_workbook(workbook, name)

    except Exception as e:
        print('Произошла ошибка во время выполнения программы.')
        print(f'Тип ошибки: {type(e).__name__}')
        print(f'Сообщение об ошибке: {str(e)}')


if __name__ == '__main__':
    main()
