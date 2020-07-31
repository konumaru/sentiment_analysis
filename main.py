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

        grouped_df[['id', 'content']].to_csv(dst_filepath, header=None, index=None, sep=' ')

    shutil.make_archive(export_dir, 'zip', root_dir=export_dir)


if __name__ == '__main__':
    main()
