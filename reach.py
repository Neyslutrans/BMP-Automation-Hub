from modules import paths
from modules.data_processing import reach_dataframe
from modules.excel_operations import create_workbook, save_workbook, format_sheet
from modules.dataframe_operations import import_dataframe, export_dataframe_to_sheet


def main() -> None:
    try:
        file_paths = paths.PathManager.open_file_dialog()
        wb = create_workbook()
        counter = 1

        for file in file_paths:
            try:
                print(f'Обрабатывается файл: {file}')
                df = import_dataframe(file)
                df = reach_dataframe(df)
                ws = wb.create_sheet(f'{df["target"]} - {counter}')
                counter += 1

                export_dataframe_to_sheet(df["dataframe"], ws)

                format_sheet(ws)

            except Exception as e:
                print(f"Ошибка при обработке файла: {file}")
                print(f"Тип ошибки: {type(e).__name__}")
                print(f"Сообщение об ошибке: {str(e)}")
                continue

        name = paths.PathManager.save_file_dialog()
        save_workbook(wb, name)

    except Exception as e:
        print("Произошла ошибка во время выполнения программы.")
        print(f"Тип ошибки: {type(e).__name__}")
        print(f"Сообщение об ошибке: {str(e)}")


if __name__ == '__main__':
    main()
