import pandas as pd
import re

# affinity
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
        raise Exception("Ошибка при обработке датафрейма") from e


def get_cleared_channel(string: str):
    return re.sub(r'\([^()]*\)', '', string).strip()