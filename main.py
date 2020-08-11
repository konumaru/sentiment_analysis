import os
import shutil
import pandas as pd

export_dir = 'documents'


def main():
    # GASで収集したデータをロード
    df = pd.read_csv('AppStoreReview.csv')
    # レビューの Rating ごとにファイルを出力
    for rate, grouped_df in df.groupby('rating'):
        rate = str(rate - 1)
        dst_dir = os.path.join(export_dir, rate)
        # 出力先ディレクトリがなければ作成
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        # レビューのタイトルと本文を結合
        grouped_df['content'] = grouped_df['content'].astype(str)
        grouped_df['content'] = grouped_df['content'].apply(lambda x: x.replace('\n', ''))
        grouped_df['all_content'] = grouped_df['id'].str.strip() + grouped_df['content'].str.strip()
        # レビューデータを１レビュー１ファイルに出力
        for i, (idx, txt) in enumerate(grouped_df['all_content'].items()):
            with open(os.path.join(dst_dir, f'sample_{idx}.txt'), 'w') as f:
                f.write(str(txt))
    # すべてのファイルをzipで圧縮
    shutil.make_archive(export_dir, 'zip', root_dir=export_dir)


if __name__ == '__main__':
    main()
