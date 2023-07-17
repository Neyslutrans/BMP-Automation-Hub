import pandas as pd
import re

# Аффинити
def affinity_dataframe(df: pd.DataFrame):
    try:
        df.drop(df.columns[[0, 3, 4, 7]], axis=1, inplace=True)
        df.reset_index(inplace=True, drop=True)

        target = df.iloc[0, 3]
        df.drop([0, 1], axis=0, inplace=True)

        df.columns = ['Блок распространения', 'Телеканал', 'Sales TVR', f'{target} TVR']

        df[f'{target} TVR'] = df[f'{target} TVR'].apply(lambda x: str(x).replace(',', '.')).astype('float64')
        df['Sales TVR'] = df['Sales TVR'].apply(lambda x: str(x).replace(',', '.')).astype('float64')

        df[f'Affinity {target}'] = df[f'{target} TVR'] / df['Sales TVR']

        df['Телеканал'] = df['Телеканал'].apply(get_cleared_channel)

        df = df.round(4)

        return {
            'dataframe': df,
            'target': target
        }

    except Exception as e:
        raise Exception('Ошибка при обработке датафрейма') from e
    

# Рейтинг
def tvr_dataframe(df: pd.DataFrame):
    try:
        df.drop(df.columns[[0, 4]], axis=1, inplace=True)

        # Определяем целевую аудиторию
        target = df.iloc[0, 3]

        # Переименовываем столбцы
        df.columns = ['Блок распространения', 'Телеканал', 'PT / OP', target]
        df.drop([0, 1], axis=0, inplace=True)

        # Форматируем телеканалы и определяем формат чисел
        df['Телеканал'] = df['Телеканал'].apply(lambda x: get_cleared_channel(x))
        df[target] = df[target].apply(lambda x: str(x).replace(',', '.')).astype('float64')

        # Округляем значения до 4 знаков
        df = df.round(4)

        return {
            'dataframe': df,
            'target': target
        }

    except Exception as e:
        raise Exception('Ошибка при обработке датафрейма') from e


# Охват
def reach_dataframe(df: pd.DataFrame):
    
    REMAINS = 50

    try:
        df.drop(df.columns[[0, 3]], axis=1, inplace=True)

        target = df.iloc[0, 2]
        header = ['Рекламодатель', 'Дата', f'{target} TVR']

        for i in range(3, len(df.columns)):
            header.append(df.iloc[2, i])

        df.columns = header

        df.drop([0, 1, 2], axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)

        for column in header[2:]:
            df[column] = df[column].apply(lambda x: x.replace(',', '.')).astype('float64')

        df['Дата'] = df['Дата'].apply(lambda x: x.replace('/', '.'))

        df['Total TVR'] = None

        df.loc[0, 'Total TVR'] = df.loc[0, f'{target} TVR']

        for i in range(1, len(df['Total TVR'])):
                df.loc[i, 'Total TVR'] = df.loc[i, f'{target} TVR'] + df.loc[i - 1, 'Total TVR']
                

        df['Остаток'] = df['Total TVR'] % REMAINS
        df['Шаг'] = df['Total TVR'] - df['Остаток']

        df['Отсечка'] = None

        for i in range(1, len(df['Остаток'])):
                df.loc[i, 'Отсечка'] = 'yes' if df.loc[i - 1, 'Остаток'] > df.loc[i, 'Остаток'] else 'no'

        df.loc[len(df) - 1, 'Отсечка'] = 'yes'

        # Округляем значения до 4 знаков
        df = df.round(4)

        return {
            'dataframe': df,
            'target': target
        }

    except Exception as e:
        raise Exception('Ошибка при обработке датафрейма') from e


# Позиционирование
def positioning_dataframe(df: pd.DataFrame):
    try:
        df.drop(df.columns[[0, 4]], axis=1, inplace=True)

        # Определяем целевую аудиторию
        target = df.iloc[0, 3]

        # Переименовываем столбцы
        df.columns = ['Блок распространения', 'Телеканал', 'Позиция', target]
        df.drop([0, 1], axis=0, inplace=True)

        # Форматируем телеканалы и определяем формат чисел
        df['Телеканал'] = df['Телеканал'].apply(lambda x: get_cleared_channel(x))
        df[target] = df[target].apply(lambda x: str(x).replace(',', '.').replace('\xa0', '')).astype('float64')

        # Округляем значения до 4 знаков
        df = df.round(4)

        return {
            'dataframe': df,
            'target': target
        }

    except Exception as e:
        raise Exception('Ошибка при обработке датафрейма') from e


def get_cleared_channel(string: str):
    return re.sub(r'\([^()]*\)', '', string).strip()
