import os
import shutil
import pandas as pd

export_dir = 'documents'


def main():
    df = pd.read_csv('AppStoreReview.csv')

    for rate, grouped_df in df.groupby('rating'):
        rate = str(rate - 1)
        filename = 'sample.txt'
        dst_dir = os.path.join(export_dir, rate)
        dst_filepath = os.path.join(export_dir, rate, filename)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        grouped_df['content'] = grouped_df['content'].astype(str)
        grouped_df['content'] = grouped_df['content'].apply(lambda x: x.replace('\n', ''))
        grouped_df['all_content'] = grouped_df['id'].str.strip() + grouped_df['content'].str.strip()

        for i, (idx, txt) in enumerate(grouped_df['all_content'].items()):
            with open(os.path.join(dst_dir, f'sample_{idx}.txt'), 'w') as f:
                f.write(str(txt))

    shutil.make_archive(export_dir, 'zip', root_dir=export_dir)


if __name__ == '__main__':
    main()
